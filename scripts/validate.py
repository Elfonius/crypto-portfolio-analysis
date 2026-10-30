#!/usr/bin/env python3
"""Validate the crypto-portfolio-analysis skill package.

Usage:
    python scripts/validate.py . --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REFERENCE_COUNT = 13
TEMPLATE_COUNT = 10
LENS_COUNT = 16
STEP_COUNT = 14
MAX_LINES = 500
MAX_TOKENS = 5000
FORBIDDEN = [
    "skill_view",
    "related_skills",
    "C:\\Users\\",
    "/Users/",
    "AppData",
]
PERSONAL: list[str] = []
ADDRESS_PATTERNS = [
    re.compile(r"\b0x[a-fA-F0-9]{40}\b"),
    re.compile(r"\b5[1-9A-HJ-NP-Za-km-z]{47}\b"),
]
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{16,}"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9]{16,}"),
]


def token_count(text: str) -> tuple[int, str]:
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text)), "tiktoken:cl100k_base"
    except Exception:
        return max(1, len(text) // 4), "fallback:len/4"


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in block:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def scan(path: Path, patterns: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    hits = []
    for pattern in patterns:
        if pattern in text:
            hits.append(f"{path.name}: contains forbidden marker {pattern!r}")
    return hits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    skill = root / "skill"
    skill_md = skill / "SKILL.md"
    errors: list[str] = []
    warnings: list[str] = []

    if not skill_md.exists():
        print(f"FAIL: missing {skill_md}")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        errors.append(f"SKILL.md has {len(lines)} lines; max {MAX_LINES}")
    tokens, token_method = token_count(text)
    if tokens > MAX_TOKENS:
        errors.append(f"SKILL.md has {tokens} tokens ({token_method}); max {MAX_TOKENS}")

    meta = frontmatter(text)
    for key in ("name", "description", "version", "author", "license"):
        if not meta.get(key):
            errors.append(f"frontmatter missing {key}")
    desc = meta.get("description", "")
    if len(desc) > 60:
        errors.append(f"description is {len(desc)} chars; max 60")
    if not desc.startswith("Use when"):
        errors.append("description must start with 'Use when'")
    version = meta.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"version is not semver: {version!r}")

    lens_rows = [line for line in lines if re.match(r"^\|\s*\d+\s*\|", line)]
    if len(lens_rows) != LENS_COUNT:
        errors.append(f"expected {LENS_COUNT} lens rows, found {len(lens_rows)}")
    for row in lens_rows:
        if row.count("|") != 5:
            errors.append(f"lens row has wrong column count: {row[:80]}")
            break

    procedure = re.search(r"## Procedure[^\n]*\n(.*?)(?=\n## )", text, re.S)
    if not procedure:
        errors.append("missing Procedure section")
    else:
        steps = re.findall(r"^\d+\.\s+\*\*", procedure.group(1), re.M)
        if len(steps) != STEP_COUNT:
            errors.append(f"expected {STEP_COUNT} procedure steps, found {len(steps)}")

    refs = sorted((skill / "references").glob("*.md"))
    if len(refs) != REFERENCE_COUNT:
        errors.append(f"expected {REFERENCE_COUNT} references, found {len(refs)}")
    for ref in refs:
        body = ref.read_text(encoding="utf-8")
        for section in ("## Purpose", "## Inputs", "## Method", "## Failure modes"):
            if section not in body:
                errors.append(f"{ref.name}: missing {section}")
        if "{{" in body:
            errors.append(f"{ref.name}: unresolved placeholder in reference")

    for linked in re.findall(r"`((?:references|templates)/[^`]+)`", text):
        if not (skill / linked).is_file():
            errors.append(f"SKILL.md links to missing file: {linked}")

    templates = sorted((skill / "templates").glob("*.md"))
    if len(templates) != TEMPLATE_COUNT:
        errors.append(f"expected {TEMPLATE_COUNT} templates, found {len(templates)}")
    for template in templates:
        body = template.read_text(encoding="utf-8")
        for placeholder in ("{{AS_OF}}", "{{BASE_CURRENCY}}", "{{DATA_COVERAGE}}"):
            if placeholder not in body:
                errors.append(f"{template.name}: missing {placeholder}")
    required_templates = (
        "investment-policy.md",
        "portfolio-review-tr.md",
        "portfolio-review-en.md",
        "quick-screen.md",
        "risk-dashboard.md",
        "scenario-analysis.md",
        "rebalancing-plan.md",
        "data-request.md",
        "monitoring.md",
        "visual-dashboard.md",
    )
    for required in required_templates:
        if not (skill / "templates" / required).exists():
            errors.append(f"missing template {required}")

    for path in sorted(skill.rglob("*.md")):
        for finding in scan(path, FORBIDDEN + PERSONAL):
            errors.append(finding)
        body = path.read_text(encoding="utf-8")
        for pattern in ADDRESS_PATTERNS:
            if pattern.search(body):
                errors.append(f"{path.name}: looks like a real wallet address")
        for pattern in SECRET_PATTERNS:
            if pattern.search(body):
                errors.append(f"{path.name}: looks like a secret/API key")

    for path in [root / "README.md", root / "docs", root / "examples"]:
        if not path.exists():
            continue
        paths = [path] if path.is_file() else list(path.rglob("*.md"))
        for item in paths:
            for finding in scan(item, FORBIDDEN + PERSONAL):
                errors.append(finding)

    script = root / "scripts" / "portfolio_math.py"
    if not script.exists():
        errors.append("missing scripts/portfolio_math.py")
    else:
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    if list((skill / "scripts").glob("*.py")):
        errors.append("skill contains executable code; keep the skill text-only")

    if warnings and args.strict:
        errors.extend(warnings)
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: 0 error(s), {len(warnings)} warning(s)")
    print(f"SKILL.md: {len(lines)} lines, {tokens} tokens ({token_method})")
    print(f"references: {len(refs)}, templates: {len(templates)}, lenses: {len(lens_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
