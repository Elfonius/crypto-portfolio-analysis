# Install

## Hermes

```bash
mkdir -p ~/.hermes/skills/research/crypto-portfolio-analysis
cp -R skill/. ~/.hermes/skills/research/crypto-portfolio-analysis
```

Windows:

```powershell
New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills\research" | Out-Null
Copy-Item -Recurse skill "$env:LOCALAPPDATA\hermes\skills\research\crypto-portfolio-analysis"
```

Start a new session so the skill index refreshes. The skill is loaded by its `SKILL.md` frontmatter.

## Claude Code / Codex / Cursor

Copy `skill/` into the agent’s skills directory, or use its skill manager if it supports `SKILL.md` packages. The installable skill is plain Markdown; the repository also includes an optional stdlib Python helper.

## Python helper

`scripts/portfolio_math.py` requires Python 3.10+ and no third-party packages.

```bash
python scripts/portfolio_math.py --help
```

## Optional validator

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py . --strict
```

`requirements-dev.txt` contains only `tiktoken`; tests use the standard library `unittest`.

## Data access

No API key is required for the free sources used in the examples. Optional paid sources (Dune, Token Terminal, Glassnode) are not assumed. If you use them, keep keys in your own environment and never commit them.

## Uninstall

Remove the skill directory. The repository does not install services, daemons, or scheduled jobs.
