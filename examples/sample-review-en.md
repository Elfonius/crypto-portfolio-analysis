# Example Portfolio Review (Synthetic)

**As of:** 2026-10-30 14:00 UTC  
**Base currency:** USD  
**Data coverage:** 92% (four live positions; small-cap price six hours old)  
**Benchmark:** BTC  
**Mode:** Full Review

> Synthetic example. No real wallet, person, or investment recommendation.

## 1. Executive Summary

- **Main finding:** 65% of the portfolio sits in BTC and ETH, so it behaves like a high-beta crypto index with a small illiquid tail.
- **Why it matters:** The portfolio trails BTC; the gap must be separated into selection, beta, fees, and liquidity risk.
- **Verified:** Prices from two sources; balances reconciled within 0.4%.
- **Not verified:** True exit depth for the small-cap; cost basis is missing.
- **Decision:** Review the small-cap and cap the single-position weight. This is not a trade instruction.
- **What would change the view:** Small-cap exit time under five days, or beta above 1.4.

## 2. Mandate and IPS-lite

| Item | Detail |
|---|---|
| Purpose | Growth over three years |
| Return objective | Long-term growth with BTC-like risk, not maximum yield |
| Risk tolerance | Maximum 35% drawdown |
| Liquidity | $20,000 within 12 months |
| Constraints | 30% single-position cap; no leverage |
| Review | Quarterly; monthly risk check |

## 3. Portfolio Snapshot

| Position | Value | Weight | Source/time | Evidence |
|---|---:|---:|---|---|
| BTC | $42,000 | 42.0% | Two venues, 14:00 UTC | VERIFIED |
| ETH | $23,000 | 23.0% | Two venues, 14:00 UTC | VERIFIED |
| SOL | $15,000 | 15.0% | Venue + aggregator | VERIFIED |
| USDC | $12,000 | 12.0% | Issuer + market | VERIFIED |
| SMALL | $8,000 | 8.0% | One DEX, 08:00 UTC | ESTIMATED |
| **Total** | **$100,000** | **100%** | — | — |

**Top-1 / Top-2 / Top-3:** 42.0% / 65.0% / 80.0%  
**HHI:** 0.2726; **effective positions:** 3.67  
**Cluster map:** BTC 42%, ETH 23%, SOL 15%, stablecoin 12%, small-cap 8%.

## 4. Performance and Attribution

| Measure | Value | Window | Benchmark | Evidence |
|---|---:|---|---|---|
| TWR | +18.4% | 2026-01-01 to 2026-10-30 | BTC +24.1% | VERIFIED |
| MWR | +16.9% | Same | — | ESTIMATED |
| Contribution | BTC +9.8; ETH +5.1; SOL +4.2; other −0.7 | Same | — | ESTIMATED |

The portfolio trails BTC by 5.7 points. With no cost basis, this is a value-change analysis, not P&L.

## 5. Risk Dashboard

| Measure | Value | Window | Method | Limit |
|---|---:|---|---|---|
| Volatility | 58% | 365d | Historical | 50% |
| Max drawdown | −34% | 2 years | Daily marks | −35% |
| VaR 95% 1d | 4.8% | 365d | Historical | 4.0% |
| CVaR 95% 1d | 7.1% | 365d | Historical | 6.0% |
| Beta vs BTC | 1.12 | 365d | OLS | 1.20 |
| Top risk contribution | BTC 46% | 365d | Component CVaR | — |

VaR is not a maximum loss. The portfolio is close to its drawdown limit and above its volatility and CVaR limits.

## 6. Liquidity and Exit

| Position | Value | Daily executable volume | 5% exit days | Stressed exit days | Gate |
|---|---:|---:|---:|---:|---|
| BTC | $42,000 | $8.0B | 0.01 | 0.01 | None |
| ETH | $23,000 | $4.0B | 0.01 | 0.01 | None |
| SOL | $15,000 | $600M | 0.01 | 0.03 | None |
| USDC | $12,000 | $2.0B | 0.01 | 0.01 | Issuer redemption |
| SMALL | $8,000 | $180,000 | 0.9 | 17.8 | None |

The small-cap is not a liquidity problem at 8% of this portfolio, but it is the first position that cannot be exited quickly in stress.

## 7. Asset-Level Findings

### BTC

Reserve asset; deep liquidity; no cash flow. Main risks: regulation, custody, beta.

### ETH

Smart-contract infrastructure; staking yield and burn; validator/MEV and L2 value migration risks.

### SOL

High-performance L1; staking and network usage; outage history, validator concentration, competition.

### USDC

Liquidity buffer, not cash. Issuer, reserve, and redemption-gate risk. A 12% weight is a policy choice, not a risk-free allocation.

### SMALL

Low float, one DEX price, no independent second source. Tokenomics and unlock schedule need verification. Treat the position as `ESTIMATED`, not verified.

## 8. DeFi and On-chain

No lending or LP positions in this example. Recent BTC/ETH exchange outflows are mildly negative; this is context, not a thesis. Entity labels are probabilistic.

## 9. Scenarios

| Scenario | Shocks | Portfolio loss | Worst position | First breach |
|---|---|---:|---|---|
| Risk-off | BTC −30%, ETH −40%, SOL −50%, SMALL −70% | $30,900 / 30.9% | SMALL | Near drawdown limit |
| Stablecoin depeg | USDC −20% | $2,400 / 2.4% | USDC | Liquidity gate |
| Liquidity shock | Small-cap volume −75% | 17.8 exit days | SMALL | Not the 12-month need |
| Reverse stress | BTC −45%, ETH −55%, SOL −65%, SMALL −85% | $47,500 / 47.5% | SMALL | 35% drawdown breach |

## 10. Alternatives and Rebalancing

| Alternative | Risk | Liquidity | Concentration | Cost/tax | What would make it wrong? |
|---|---|---|---|---|---|
| Current | High beta | Good except small-cap | Top-2 65% | Low | BTC rally continues |
| Risk-reduced | Lower beta | Better | Top-2 55% | Medium | Bull market missed |
| Diversified-within-thesis | Similar beta | Medium | Top-2 50% | Medium | Correlations rise |

**Bands:** ±5 percentage points; ±3 for the small-cap.  
**Tax note:** Cost basis missing; tax impact not assessable.

## 11. Decision Record

- **Decision:** Review the small-cap; enforce the 30% single-position cap; classify USDC as a counterparty-bearing liquidity buffer.
- **Rationale:** Top-2 65%, weak small-cap liquidity, underperformance vs BTC.
- **Size/implementation:** No size without constraints.
- **Falsifiers:** Small-cap exit time below five days, or beta above 1.4.
- **Review:** 2027-01-30; monthly liquidity and beta check.

## 12. Sources and Limitations

- Prices: two independent venues/aggregators, 2026-10-30 14:00 UTC.
- Balances: wallet plus second source; 0.4% difference.
- Small-cap: one DEX, 08:00 UTC; no independent confirmation.
- Cost basis missing; value change is not P&L.
- Not investment, tax, or legal advice.

## 13. Visual Pack

- [Allocation](charts/V1-allocation.png) — BTC 42%; top-2 65%.
- [Concentration](charts/V2-concentration.png) — top-2 and cluster limits breached.
- [Risk-return](charts/V6-risk-return.png) — most risk budget in BTC and ETH.
- [Scenarios](charts/V9-scenarios.png) — reverse stress breaches the 35% loss floor.

> Charts are synthetic; each shows one finding.
