# Architecture

## Design goals

- Portable: no private skills, personal paths, or local services.
- Read-only: no keys, signing, approvals, swaps, or deposits.
- Auditable: every material number has a source, date, and evidence class.
- Reproducible: deterministic math helper with tests.
- Small: one skill file, 13 references, 10 templates, one optional script.

## Layers

| Layer | Purpose |
|---|---|
| `skill/` | Installable text-only skill: `SKILL.md`, 13 references, 10 templates |
| `scripts/portfolio_math.py` | Optional deterministic math helper; no network |
| `scripts/validate.py` | Structure, token, privacy, and placeholder checks |
| `tests/` | Unit tests and synthetic fixtures |
| `docs/` | Install, usage, methodology, architecture, FAQ |
| `examples/` | Synthetic sample outputs |

## Why one script

Portfolio analysis has many numbers that should not be invented. The script centralizes the repeatable math:

- weights, HHI, effective N, top-N;
- volatility, max drawdown, historical VaR/CVaR;
- correlation and beta;
- stress loss;
- rebalancing deltas;
- DeFi health factor.

It is stdlib-only so users can audit it and run it without pandas or numpy.

## Why text-first

The judgment — mandate, materiality, source quality, scenario choice, falsifiers — belongs in the skill, not hidden in code. The script computes; the analyst decides.

## Data flow

```text
User inputs / wallet exports
        ↓
Source plan and evidence classes
        ↓
Valuation and reconciliation
        ↓
Portfolio math (JSON in/out)
        ↓
Asset and risk research
        ↓
Scenario and alternative analysis
        ↓
Report + decision record + monitoring
```

## Failure behavior

- Missing value → `DataError` or `not assessable`.
- Unreconciled balance → lower data coverage; no full verdict.
- Missing mandate → Data Request Memo.
- Paid API unavailable → degrade; do not fabricate coverage.

## Extension points

- Add a reference for a new chain or protocol class.
- Add a template for a new deliverable.
- Add a function and test for a new deterministic metric.
- Do not add execution, custody, or signing code.
