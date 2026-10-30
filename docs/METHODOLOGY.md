# Methodology

## Standard being emulated

The skill follows the structure of professional portfolio management:

1. **Planning:** IPS, objectives, constraints, benchmark, risk budget.
2. **Execution:** valuation, allocation, risk measurement, asset review.
3. **Feedback:** performance, attribution, monitoring, rebalancing.

It borrows the evidence discipline of GIPS, the risk framework of CFA Institute, the DeFi vulnerability taxonomy of the FSB, crypto tail-risk research, and incident evidence from Chainalysis.

## The 16 lenses

The lenses are not a checklist to fill mechanically. Each one must answer a decision-relevant question, or be marked `not material` / `not assessable`.

1. Mandate, IPS and constraints.
2. Data integrity and valuation.
3. Allocation and concentration.
4. Performance and attribution.
5. Risk, tail and risk budget.
6. Correlation and factors.
7. Liquidity and exit.
8. Stablecoin and counterparty.
9. Chain, protocol, custody and contract.
10. Tokenomics and supply overhang.
11. Fundamental value capture.
12. DeFi positions and leverage.
13. On-chain flows and holder behavior.
14. Market regime and macro.
15. Scenarios and reverse stress.
16. Construction, behavior, tax and monitoring.

## The 14 steps

1. Intake and IPS-lite.
2. Source plan.
3. Normalize.
4. Value and reconcile.
5. Allocation and concentration.
6. Performance and attribution.
7. Risk, correlation and risk budget.
8. Liquidity and exit.
9. Asset fundamentals and tokenomics.
10. DeFi and on-chain.
11. Market regime.
12. Scenarios, stress and reverse stress.
13. Alternatives and rebalancing.
14. Report and monitor.

## Non-compensatory gates

- **G1 Input completeness:** at least 80% of value has a live price and balance source.
- **G2 Source/date:** every material number has a source and date.
- **G3 Reconciliation:** balance/price difference ≤2%, or explained.
- **G4 Suitability:** horizon, liquidity, loss limit, and constraints supplied.
- **G5 Read-only:** no signing, approval, bridge, deposit, or transaction step.

A high yield, a large TVL, or a strong chart cannot compensate for a failed gate.

## Performance rules

- Use TWR for most portfolios; use MWR only with cash-flow data or illiquid/closed-end positions.
- Report net of fees and transaction costs when data exist.
- Do not annualize a period shorter than one year.
- Do not compare a gross return with a net benchmark.
- If cost basis is missing, report value change, not P&L.

## Risk rules

- Use historical VaR/CVaR with a stated window and level.
- Add stress, reverse stress, and liquidity stress.
- State that VaR is not a maximum loss.
- Test correlation instability; do not assume it is stable.
- Compare risk consumption with the IPS risk budget.

## Tokenomics rules

- Separate fees, revenue, gross profit, incentives, tokenholder revenue, buybacks, and burns.
- Show the value-capture waterfall.
- Check emissions and unlocks against buybacks.
- Do not treat TVL or volume as revenue.

## DeFi rules

- Resolve the exact chain, contract, market, and position.
- Compute LTV, health factor, and liquidation distance.
- Check the oracle, close factor, liquidation penalty, and incidents.
- Map shared stablecoin, bridge, oracle, curator, and validator dependencies.

## Report rules

- Lead with the finding and the decision.
- Separate verified, reported, estimated, modeled, and unverified.
- State the limits before the recommendation.
- Include falsifiers and a review date.
- No single health score.

## Visualization

A full review includes 6–10 charts. The chart must answer a decision question; exact values belong in tables.

- Title states the finding, not the topic.
- Every chart carries unit, as-of date, source, window, and limitation.
- Bars start at zero; log scales are labeled.
- No 3D, no pie with more than five slices, no unlabeled dual axis.
- Color is secondary; check grayscale and colorblind readability.
- Use `skill/references/13-visualization-and-charts.md` and `skill/templates/visual-dashboard.md`.

## Sources

See `skill/references/12-methodology-and-sources.md` for the source matrix and limitations.
