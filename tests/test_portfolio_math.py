"""Unit tests for the deterministic portfolio math helper.

Run from the repository root:
    python -m unittest discover -s tests -q
"""

from __future__ import annotations

import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import portfolio_math as pm  # noqa: E402


def load_fixture(name: str) -> dict:
    return json.loads((ROOT / "tests" / "fixtures" / name).read_text(encoding="utf-8"))


class TestCoreMath(unittest.TestCase):
    def test_weights(self):
        positions = [{"id": "A", "value": 60}, {"id": "B", "value": 40}]
        result = pm.weights(positions)
        self.assertAlmostEqual(result["A"], 0.6)
        self.assertAlmostEqual(result["B"], 0.4)
        self.assertAlmostEqual(sum(result.values()), 1.0)

    def test_hhi_and_effective_n(self):
        w = {"A": 0.6, "B": 0.4}
        self.assertAlmostEqual(pm.hhi(w), 0.52)
        self.assertAlmostEqual(pm.effective_n(w), 1 / 0.52)
        self.assertAlmostEqual(pm.top_n(w, 1), 0.6)
        self.assertAlmostEqual(pm.top_n(w, 2), 1.0)

    def test_volatility(self):
        returns = [0.01, 0.02, -0.01]
        expected = __import__("statistics").stdev(returns) * math.sqrt(365)
        self.assertAlmostEqual(pm.annualized_volatility(returns), expected)

    def test_max_drawdown(self):
        result = pm.max_drawdown([100, 120, 90, 110])
        self.assertAlmostEqual(result["max_drawdown"], -0.25)
        self.assertEqual(result["peak_index"], 1)
        self.assertEqual(result["trough_index"], 2)

    def test_historical_var_cvar(self):
        result = pm.historical_var_cvar([-0.10, -0.05, 0.0, 0.05, 0.10], 0.80)
        self.assertAlmostEqual(result["var"], 0.05)
        self.assertAlmostEqual(result["cvar"], 0.075)
        self.assertEqual(result["tail_count"], 2)

    def test_correlation_and_beta(self):
        self.assertAlmostEqual(pm.correlation([1, 2, 3], [1, 2, 3]), 1.0)
        self.assertAlmostEqual(pm.correlation([1, 2, 3], [3, 2, 1]), -1.0)
        self.assertAlmostEqual(pm.beta([0.01, 0.02, -0.01], [0.01, 0.02, -0.01]), 1.0)

    def test_portfolio_returns(self):
        returns = {"A": [0.01, 0.02], "B": [0.03, -0.01]}
        result = pm.portfolio_returns(returns, {"A": 0.6, "B": 0.4})
        self.assertAlmostEqual(result[0], 0.018)
        self.assertAlmostEqual(result[1], 0.008)

    def test_missing_value_raises(self):
        with self.assertRaises(pm.DataError):
            pm.weights([{"id": "A", "value": None}])

    def test_stress(self):
        positions = [{"id": "BTC", "value": 600}, {"id": "ETH", "value": 400}]
        result = pm.stress_loss(positions, {"BTC": -0.30, "ETH": -0.40})
        self.assertAlmostEqual(result["pnl_impact"], -340)
        self.assertAlmostEqual(result["loss"], 340)
        self.assertAlmostEqual(result["loss_pct"], 0.34)

    def test_component_cvar(self):
        returns = {"A": [-0.10, 0.0, 0.10], "B": [-0.05, 0.02, 0.05]}
        result = pm.component_cvar(returns, {"A": 0.6, "B": 0.4}, 0.80)
        self.assertAlmostEqual(result["sum"], 0.036)
        self.assertAlmostEqual(result["contributions"]["A"], 0.03)
        self.assertAlmostEqual(result["contributions"]["B"], 0.006)

    def test_liquidity_flag(self):
        result = pm.risk_flags(
            {"A": 1.0},
            [{"id": "A", "value": 100, "liquidity_days": 10}],
            {"max_exit_days": 5},
        )
        self.assertTrue(any(item["flag"] == "liquidity" for item in result))

    def test_rebalance(self):
        result = pm.rebalance_delta({"A": 0.6, "B": 0.4}, {"A": 0.5, "B": 0.5}, 1000)
        self.assertAlmostEqual(result["deltas"]["A"], -0.1)
        self.assertAlmostEqual(result["value_deltas"]["A"], -100)

    def test_defi(self):
        hf = pm.health_factor(1000, 700, 0.8)
        self.assertAlmostEqual(hf["health_factor"], 1000 * 0.8 / 700)
        self.assertEqual(hf["status"], "above threshold")
        self.assertAlmostEqual(pm.liquidation_price(1, 700, 0.8), 875)

    def test_exit_days(self):
        self.assertAlmostEqual(pm.exit_days(1000, 1000, 0.05), 20.0)


class TestFixtures(unittest.TestCase):
    def test_simple_60_40(self):
        result = pm.analyze(load_fixture("simple-60-40.json"))
        self.assertAlmostEqual(result["weights"]["BTC"], 0.6)
        self.assertAlmostEqual(result["concentration"]["top2"], 1.0)
        self.assertIn("risk", result)
        self.assertIn("drawdown", result)
        self.assertIn("beta", result["risk"])

    def test_concentrated_flags(self):
        result = pm.analyze(load_fixture("concentrated.json"))
        flags = {item["flag"] for item in result["flags"]}
        self.assertIn("top1", flags)
        self.assertIn("top2", flags)
        self.assertIn("cluster", flags)

    def test_bittensor_flags(self):
        result = pm.analyze(load_fixture("bittensor-snapshot.json"))
        self.assertAlmostEqual(result["concentration"]["top1"], 0.4922, places=4)
        self.assertAlmostEqual(result["concentration"]["top2"], 0.7559, places=4)
        self.assertAlmostEqual(result["concentration"]["top3"], 0.8171, places=4)
        flags = {item["flag"] for item in result["flags"]}
        self.assertIn("top1", flags)
        self.assertIn("top2", flags)
        self.assertIn("top3", flags)
        self.assertIn("cluster", flags)

    def test_missing_data_raises(self):
        with self.assertRaises(pm.DataError):
            pm.analyze(load_fixture("missing-data.json"))

    def test_defi_fixture(self):
        result = pm.analyze(load_fixture("defi-lending.json"))
        self.assertIn("defi", result)
        self.assertAlmostEqual(result["defi"][0]["health_factor"], 1000 * 0.8 / 700)


if __name__ == "__main__":
    unittest.main()
