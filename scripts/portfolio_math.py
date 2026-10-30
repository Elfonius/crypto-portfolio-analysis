#!/usr/bin/env python3
"""Deterministic portfolio calculations for the crypto-portfolio-analysis skill.

Stdlib only. No network. No transaction execution.
Input and output are JSON so every number can be reproduced.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any

VERSION = "1.0.0"


class DataError(ValueError):
    """Raised when an input cannot be valued without guessing."""


def _finite(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise DataError(f"{name} must be a number, got {type(value).__name__}")
    number = float(value)
    if not math.isfinite(number):
        raise DataError(f"{name} must be finite")
    return number


def _positive_positions(positions: list[dict[str, Any]]) -> dict[str, float]:
    if not positions:
        raise DataError("positions must not be empty")
    values: dict[str, float] = {}
    for index, position in enumerate(positions):
        key = position.get("id") or position.get("symbol") or f"position-{index}"
        value = position.get("value")
        if value is None:
            raise DataError(f"{key}: missing value; valuation is not assessable")
        number = _finite(value, f"{key}.value")
        if number < 0:
            raise DataError(f"{key}: value must be non-negative")
        values[str(key)] = number
    total = sum(values.values())
    if total <= 0:
        raise DataError("total portfolio value must be positive")
    return values


def weights(positions: list[dict[str, Any]]) -> dict[str, float]:
    values = _positive_positions(positions)
    total = sum(values.values())
    return {key: value / total for key, value in values.items()}


def hhi(weight_map: dict[str, float]) -> float:
    if not weight_map:
        raise DataError("weights must not be empty")
    return sum(max(0.0, float(value)) ** 2 for value in weight_map.values())


def effective_n(weight_map: dict[str, float]) -> float:
    concentration = hhi(weight_map)
    if concentration <= 0:
        raise DataError("HHI must be positive")
    return 1.0 / concentration


def top_n(weight_map: dict[str, float], n: int) -> float:
    if n < 1:
        raise DataError("n must be at least 1")
    return sum(sorted(weight_map.values(), reverse=True)[:n])


def annualized_volatility(returns: list[float], periods_per_year: int = 365) -> float:
    if len(returns) < 2:
        raise DataError("at least two returns are required")
    clean = [_finite(r, "return") for r in returns]
    if periods_per_year <= 0:
        raise DataError("periods_per_year must be positive")
    return statistics.stdev(clean) * math.sqrt(periods_per_year)


def max_drawdown(equity_curve: list[float]) -> dict[str, Any]:
    if len(equity_curve) < 2:
        raise DataError("at least two equity values are required")
    values = [_finite(v, "equity") for v in equity_curve]
    if any(v <= 0 for v in values):
        raise DataError("equity values must be positive")
    peak = values[0]
    peak_index = 0
    worst = 0.0
    trough_index = 0
    worst_peak_index = 0
    for index, value in enumerate(values):
        if value > peak:
            peak = value
            peak_index = index
        drawdown = value / peak - 1.0
        if drawdown < worst:
            worst = drawdown
            trough_index = index
            worst_peak_index = peak_index
    return {
        "max_drawdown": worst,
        "peak_index": worst_peak_index,
        "trough_index": trough_index,
        "peak_value": values[worst_peak_index],
        "trough_value": values[trough_index],
        "method": "daily equity curve",
    }


def historical_var_cvar(returns: list[float], level: float = 0.95) -> dict[str, Any]:
    if len(returns) < 2:
        raise DataError("at least two returns are required")
    if not 0.0 < level < 1.0:
        raise DataError("level must be between 0 and 1")
    clean = sorted(_finite(r, "return") for r in returns)
    index = max(0, min(len(clean) - 1, math.ceil((1.0 - level) * len(clean))))
    if index == 0:
        index = 1 if len(clean) > 1 else 0
    threshold = clean[index]
    tail = clean[: index + 1]
    var = max(0.0, -threshold)
    cvar = max(0.0, -sum(tail) / len(tail))
    return {
        "level": level,
        "observations": len(clean),
        "var": var,
        "cvar": cvar,
        "tail_count": len(tail),
        "method": "historical simulation; VaR is the loss at the lower quantile",
        "limitation": "VaR is not a maximum loss; history may not repeat",
    }


def correlation(x: list[float], y: list[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise DataError("correlation series must have equal length >= 2")
    xs = [_finite(v, "x") for v in x]
    ys = [_finite(v, "y") for v in y]
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    cov = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    vx = sum((a - mx) ** 2 for a in xs)
    vy = sum((b - my) ** 2 for b in ys)
    if vx == 0 or vy == 0:
        raise DataError("correlation is undefined for a constant series")
    return cov / math.sqrt(vx * vy)


def correlation_matrix(series: dict[str, list[float]]) -> dict[str, dict[str, float]]:
    names = list(series)
    if len(names) < 2:
        raise DataError("at least two series are required")
    lengths = {len(series[name]) for name in names}
    if len(lengths) != 1:
        raise DataError("all correlation series must have equal length")
    return {
        a: {b: (1.0 if a == b else correlation(series[a], series[b])) for b in names}
        for a in names
    }


def portfolio_returns(returns: dict[str, list[float]], weight_map: dict[str, float]) -> list[float]:
    if not returns:
        raise DataError("returns must not be empty")
    lengths = {len(series) for series in returns.values()}
    if len(lengths) != 1:
        raise DataError("all return series must have equal length")
    missing = [key for key in weight_map if key not in returns]
    if missing:
        raise DataError(f"missing return series: {', '.join(sorted(missing))}")
    total_weight = sum(weight_map.values())
    if total_weight <= 0:
        raise DataError("weights must sum to a positive value")
    return [
        sum(weight_map[key] / total_weight * returns[key][index] for key in weight_map)
        for index in range(next(iter(lengths)))
    ]


def beta(portfolio: list[float], benchmark: list[float]) -> float:
    if len(portfolio) != len(benchmark) or len(portfolio) < 2:
        raise DataError("beta series must have equal length >= 2")
    p = [_finite(v, "portfolio") for v in portfolio]
    b = [_finite(v, "benchmark") for v in benchmark]
    mp = statistics.mean(p)
    mb = statistics.mean(b)
    cov = sum((x - mp) * (y - mb) for x, y in zip(p, b))
    var = sum((y - mb) ** 2 for y in b)
    if var == 0:
        raise DataError("benchmark variance is zero")
    return cov / var


def stress_loss(
    positions: list[dict[str, Any]], shocks: dict[str, float]
) -> dict[str, Any]:
    values = _positive_positions(positions)
    total = sum(values.values())
    losses: dict[str, float] = {}
    for position in positions:
        key = str(position.get("id") or position.get("symbol"))
        symbol = str(position.get("symbol") or key)
        shock = shocks.get(key, shocks.get(symbol, 0.0))
        shock = _finite(shock, f"{key}.shock")
        losses[key] = values[key] * shock
    total_pnl = sum(losses.values())
    return {
        "scenario": shocks,
        "pnl_impact": total_pnl,
        "loss": -total_pnl,
        "loss_pct": -total_pnl / total if total else None,
        "losses": losses,
        "method": "linear shock applied to current market value; loss is positive",
    }


def rebalance_delta(
    current: dict[str, float], target: dict[str, float], total_value: float | None = None
) -> dict[str, Any]:
    if not current or not target:
        raise DataError("current and target weights are required")
    keys = sorted(set(current) | set(target))
    deltas = {key: float(target.get(key, 0.0)) - float(current.get(key, 0.0)) for key in keys}
    result: dict[str, Any] = {
        "deltas": deltas,
        "current_sum": sum(current.values()),
        "target_sum": sum(target.values()),
    }
    if total_value is not None:
        result["value_deltas"] = {key: delta * float(total_value) for key, delta in deltas.items()}
    return result


def health_factor(collateral_value: float, debt_value: float, liquidation_threshold: float) -> dict[str, Any]:
    collateral = _finite(collateral_value, "collateral_value")
    debt = _finite(debt_value, "debt_value")
    threshold = _finite(liquidation_threshold, "liquidation_threshold")
    if collateral < 0 or debt < 0:
        raise DataError("collateral and debt must be non-negative")
    if debt == 0:
        return {"health_factor": None, "status": "no debt"}
    if not 0 < threshold <= 1:
        raise DataError("liquidation_threshold must be in (0, 1]")
    value = collateral * threshold / debt
    return {
        "health_factor": value,
        "status": "liquidatable" if value < 1 else "above threshold",
        "liquidation_threshold": threshold,
    }


def liquidation_price(
    collateral_quantity: float, debt_value: float, liquidation_threshold: float
) -> float:
    quantity = _finite(collateral_quantity, "collateral_quantity")
    debt = _finite(debt_value, "debt_value")
    threshold = _finite(liquidation_threshold, "liquidation_threshold")
    if quantity <= 0 or debt < 0 or not 0 < threshold <= 1:
        raise DataError("invalid liquidation inputs")
    return debt / (quantity * threshold)


def exit_days(position_value: float, daily_executable_volume: float, participation: float = 0.05) -> float:
    value = _finite(position_value, "position_value")
    volume = _finite(daily_executable_volume, "daily_executable_volume")
    rate = _finite(participation, "participation")
    if value < 0 or volume <= 0 or not 0 < rate <= 1:
        raise DataError("invalid exit inputs")
    return value / (volume * rate)


def component_cvar(
    returns: dict[str, list[float]], weight_map: dict[str, float], level: float = 0.95
) -> dict[str, float]:
    """Approximate component CVaR: each position's average tail contribution.

    Contributions sum to the portfolio CVaR when the same tail observations
    and weights are used. This is a tail decomposition, not a causal model.
    """
    if not 0.0 < level < 1.0:
        raise DataError("level must be between 0 and 1")
    portfolio = portfolio_returns(returns, weight_map)
    clean = sorted((r, i) for i, r in enumerate(portfolio))
    index = max(0, min(len(clean) - 1, math.ceil((1.0 - level) * len(clean))))
    tail_indices = [i for _, i in clean[: index + 1]]
    total_weight = sum(weight_map.values())
    contributions: dict[str, float] = {}
    for key, series in returns.items():
        if key not in weight_map:
            continue
        tail_mean = sum(series[i] for i in tail_indices) / len(tail_indices)
        contributions[key] = -weight_map[key] / total_weight * tail_mean
    return {
        "contributions": contributions,
        "sum": sum(contributions.values()),
        "level": level,
        "method": "historical tail contribution; not causal",
    }


def risk_flags(
    weight_map: dict[str, float],
    positions: list[dict[str, Any]],
    policy: dict[str, float] | None = None,
) -> list[dict[str, Any]]:
    policy = policy or {}
    limits = {
        "top1": policy.get("top1_limit", 0.30),
        "top2": policy.get("top2_limit", 0.60),
        "top3": policy.get("top3_limit", 0.80),
        "cluster": policy.get("cluster_limit", 0.50),
        "stablecoin": policy.get("stablecoin_limit", 0.20),
        "max_exit_days": policy.get("max_exit_days", 5.0),
    }
    flags: list[dict[str, Any]] = []
    top1 = top_n(weight_map, 1)
    top2 = top_n(weight_map, 2)
    top3 = top_n(weight_map, 3)
    for name, value, limit in (
        ("top1", top1, limits["top1"]),
        ("top2", top2, limits["top2"]),
        ("top3", top3, limits["top3"]),
    ):
        if value > limit:
            flags.append({"flag": name, "value": value, "limit": limit, "severity": "high"})
    cluster_weights: dict[str, float] = {}
    stable_weight = 0.0
    for position in positions:
        key = str(position.get("id") or position.get("symbol"))
        cluster = str(position.get("cluster") or position.get("chain") or "unclustered")
        cluster_weights[cluster] = cluster_weights.get(cluster, 0.0) + weight_map.get(key, 0.0)
        if str(position.get("asset_class", "")).lower() in {"stablecoin", "cash"}:
            stable_weight += weight_map.get(key, 0.0)
        if position.get("liquidity_days") is not None:
            days = _finite(position["liquidity_days"], f"{key}.liquidity_days")
            if days > limits["max_exit_days"]:
                flags.append({"flag": "liquidity", "position": key, "value": days, "limit": limits["max_exit_days"], "severity": "high"})
    for cluster, value in cluster_weights.items():
        if value > limits["cluster"]:
            flags.append({"flag": "cluster", "cluster": cluster, "value": value, "limit": limits["cluster"], "severity": "high"})
    if stable_weight > limits["stablecoin"]:
        flags.append({"flag": "stablecoin", "value": stable_weight, "limit": limits["stablecoin"], "severity": "medium"})
    return flags


def analyze(payload: dict[str, Any]) -> dict[str, Any]:
    positions = payload.get("positions") or []
    weight_map = weights(positions)
    total = sum(_positive_positions(positions).values())
    result: dict[str, Any] = {
        "engine": {"name": "portfolio_math", "version": VERSION, "method": "stdlib"},
        "as_of": payload.get("as_of"),
        "base_currency": payload.get("base_currency"),
        "total_value": total,
        "data_coverage": payload.get("data_coverage"),
        "weights": weight_map,
        "concentration": {
            "hhi": hhi(weight_map),
            "effective_n": effective_n(weight_map),
            "top1": top_n(weight_map, 1),
            "top2": top_n(weight_map, 2),
            "top3": top_n(weight_map, 3),
            "top5": top_n(weight_map, 5),
        },
        "flags": risk_flags(weight_map, positions, payload.get("policy")),
    }
    returns = payload.get("returns")
    if returns:
        portfolio = portfolio_returns(returns, weight_map)
        result["risk"] = {
            "volatility": annualized_volatility(portfolio, int(payload.get("periods_per_year", 365))),
            "var_cvar": historical_var_cvar(portfolio, float(payload.get("var_level", 0.95))),
            "component_cvar": component_cvar(returns, weight_map, float(payload.get("var_level", 0.95))),
            "correlation": correlation_matrix(returns),
        }
        benchmark = payload.get("benchmark_returns")
        if benchmark:
            result["risk"]["beta"] = beta(portfolio, benchmark)
    equity_curve = payload.get("equity_curve")
    if equity_curve:
        result["drawdown"] = max_drawdown(equity_curve)
    scenarios = payload.get("scenarios")
    if scenarios:
        result["scenarios"] = [
            {"name": s.get("name", f"scenario-{i}"), **stress_loss(positions, s.get("shocks", {}))}
            for i, s in enumerate(scenarios)
        ]
    target = payload.get("target_weights")
    if target:
        result["rebalance"] = rebalance_delta(weight_map, target, total)
    if payload.get("defi"):
        result["defi"] = []
        for item in payload["defi"]:
            if "collateral_value" in item:
                result["defi"].append({"id": item.get("id"), **health_factor(item["collateral_value"], item["debt_value"], item["liquidation_threshold"])})
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic crypto portfolio calculations (no network, no execution).")
    parser.add_argument("--input", required=True, help="Input JSON path")
    parser.add_argument("--output", help="Output JSON path; default stdout")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args(argv)
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = analyze(payload)
    except (OSError, json.JSONDecodeError, DataError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
