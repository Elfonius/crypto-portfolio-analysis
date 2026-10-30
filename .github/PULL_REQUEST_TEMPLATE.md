## Summary

## What changed

## Evidence

- Source/date:
- Tests run:
- Validator output:

## Safety check

- [ ] No wallet address, seed phrase, private key, password, or API secret.
- [ ] No execution, signing, approval, bridge, or deposit instruction.
- [ ] No personal dependency or private-skill reference.
- [ ] Skill remains read-only and portable.

## Checklist

- [ ] `python -m unittest discover -s tests -q`
- [ ] `python scripts/validate.py . --strict`
- [ ] Docs/templates updated if output changed
