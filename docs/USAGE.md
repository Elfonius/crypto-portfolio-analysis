# Usage

## Choose a mode

| Mode | Use when | Output |
|---|---|---|
| Quick Screen | You need a fast risk read | 1–2 pages, top positions, concentration, red flags |
| Full Review | You need an investment-grade review | 8–15 pages, all 16 lenses, scenarios, decision record |
| Monitoring | You already have a baseline | Delta, breaches, falsifiers, next review |

## Minimum input

- Wallet addresses or an exported positions file.
- Base currency.
- Horizon, liquidity needs, maximum drawdown, and loss floor.
- Benchmark or “none.”
- Cost basis if P&L is required.
- Tax/legal constraints if implementation is discussed.

Do not send a seed phrase, private key, password, or 2FA code.

## Prompt pattern

> Review this crypto portfolio as a full review. Base currency USD. Horizon 2 years. Maximum drawdown 35%. I need $20k liquidity within 12 months. Benchmark: BTC. Use only live sources and label anything you cannot verify.

## Quick Screen prompt

> Give me a quick screen of these positions. Flag the top three risks and tell me what data is missing. Do not recommend a trade.

## Monitoring prompt

> Compare this snapshot with the previous one. Show weight changes, threshold breaches, and whether the original thesis is still intact.

## Deterministic math

```bash
python scripts/portfolio_math.py --input my-portfolio.json --output result.json --pretty
```

Input fields:

- `as_of`, `base_currency`
- `positions[]`: `id` or `symbol`, `value`, optional `asset_class`, `chain`, `protocol`, `cluster`
- `returns{}`: symbol → list of periodic returns
- `benchmark_returns[]`
- `equity_curve[]`
- `scenarios[]`: `{name, shocks}`
- `target_weights{}`
- `policy{}`: `top1_limit`, `top2_limit`, `top3_limit`, `cluster_limit`, `stablecoin_limit`
- `defi[]`: `{id, collateral_value, debt_value, liquidation_threshold}`

## What the output means

- Weight and HHI are as-of the input snapshot.
- VaR/CVaR are historical and depend on the supplied window.
- Stress results are linear shocks, not forecasts.
- A `DataError` means a required input is missing; do not replace it with zero.

## Privacy

Use public addresses or redacted exports. Keep private keys and API secrets out of the chat and repository. The skill does not need them.
