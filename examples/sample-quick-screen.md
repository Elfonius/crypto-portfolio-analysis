# Quick Screen — Synthetic Example

**As of:** 2026-10-30 14:00 UTC  
**Base currency:** USD  
**Data coverage:** 92%  
**Mode:** Quick Screen

## Snapshot

| Position | Value | Weight | Source |
|---|---:|---:|---|
| BTC | $42,000 | 42.0% | Two venues |
| ETH | $23,000 | 23.0% | Two venues |
| SOL | $15,000 | 15.0% | Venue + aggregator |
| USDC | $12,000 | 12.0% | Issuer + market |
| SMALL | $8,000 | 8.0% | One DEX, stale |
| **Total** | **$100,000** | **100%** | — |

**Top-1 / Top-2 / Top-3:** 42% / 65% / 80%. **HHI:** 0.2726.

## Five red flags

1. **Top-2 = 65%** — above the 60% policy limit; BTC/ETH beta dominates.
2. **Volatility 58%** and **CVaR 7.1%** — above the stated limits.
3. **Small-cap price is six hours stale** and only one venue is available.
4. **USDC is treated as cash**, but issuer/redemption risk is not zero.
5. **No cost basis** — P&L and tax impact are not assessable.

## Verified

- BTC, ETH, SOL, USDC prices from two sources.
- Balances reconciled within 0.4%.
- Total value reproducible.

## Not verified

- Small-cap exit depth and independent price.
- Cost basis, tax lots, and realized gains.
- The small-cap unlock schedule and holder concentration.

## Verdict

The portfolio is a liquid, high-beta crypto book with a small illiquid tail. Its main risk is not the number of positions; it is the **65% top-2 concentration plus a volatility/CVaR level above the mandate**. Review the small-cap and the single-position cap before adding risk.

**What would change the view:** small-cap exit time below five days and beta below 1.0.

## Visual pack

- [Allocation](charts/V1-allocation.png)
- [Concentration](charts/V2-concentration.png)
- [Risk-return](charts/V6-risk-return.png)

> Quick screen only. Not investment advice. No execution.
