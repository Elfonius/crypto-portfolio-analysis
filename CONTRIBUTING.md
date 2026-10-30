# Contributing

## What belongs here

- Method notes that make portfolio analysis more rigorous.
- Templates that improve decision quality without adding decoration.
- Deterministic calculations with tests.
- Data-source notes with a live probe, date, and limitation.

## What does not belong here

- Personal wallet addresses, names, paths, API keys, or account data.
- Trading execution, signing, approval, bridge, or deposit instructions.
- Price predictions, guaranteed returns, or “best coin” lists.
- Dependencies on private skills or paid APIs presented as available.

## Workflow

1. Open an issue describing the gap and the evidence.
2. Keep `SKILL.md` under 5,000 tokens and 500 lines.
3. Put depth in `skill/references/`; keep the main file procedural.
4. Add or update a template if the output changes.
5. Add a test if the math changes.
6. Run:

```bash
python -m unittest discover -s tests -q
python scripts/validate.py . --strict
```

7. Open a pull request with the test output and the source/date for any new claim.

## Style

- English for repository docs and code.
- Turkish and English templates are both welcome.
- Plain language; define jargon on first use.
- One rule per paragraph; no marketing copy.
- Label evidence classes; never present a report claim as verified.
