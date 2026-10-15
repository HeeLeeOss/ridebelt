#!/usr/bin/env python3
"""RideBelt traceability and consistency checker.

Checks (all IDs are matched in the markdown tables under docs/):
  1. Every requirement defined in docs/requirements.md appears in the
     traceability table of docs/testing/test-plan.md.
  2. Every test ID referenced anywhere (requirements, hazards, FMEA,
     traceability table) is defined in the test plan or RAS standard.
  3. Every requirement ID referenced in the hazard analysis is defined.
  4. Every FMEA row with severity S >= 9 lists a mitigation and a test.
  5. Every safety document carries the DRAFT banner unless a sign-off
     record for it exists in review/.

Stdlib only. Exit code 0 = pass, 1 = violations found.
Run from the repository root:  python tools/check_traceability.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REQUIREMENTS = DOCS / "requirements.md"
TEST_PLAN = DOCS / "testing" / "test-plan.md"
HAZARDS = DOCS / "safety" / "hazard-analysis.md"
FMEA = DOCS / "safety" / "fmea.md"
STANDARD_DIR = DOCS / "standard"
REVIEW_DIR = ROOT / "review"
SAFETY_DOC_DIRS = ["safety", "design", "standard", "analysis", "testing"]
DRAFT_MARKER = "DRAFT: not reviewed"

REQ_RE = r"REQ-[A-Z]\d+"
TEST_RE = r"(?:T-[SDFE]\d+|RAS-CT\d+)"
# "REQ-A1 to REQ-A3", "T-D1–T-D3", "RAS-CT0 to RAS-CT5", "REQ-F1 to F3"
RANGE_RE = re.compile(r"((?:REQ-[A-Z]|T-[SDFE]|RAS-CT))(\d+)\s*(?:to|–|-)\s*(?:\1)?(\d+)\b")


def table_rows(source: Path | str) -> list[list[str]]:
    """Return markdown table rows (cells stripped) from a file or text, skipping header separators."""
    text = source.read_text(encoding="utf-8") if isinstance(source, Path) else source
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.fullmatch(r"\|[\s:|-]+\|", line):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def expand_ids(text: str, pattern: str) -> set[str]:
    """All IDs matching pattern in text, with ranges like 'REQ-A1 to REQ-A3' expanded."""
    ids = set(re.findall(pattern, text))
    for prefix, lo, hi in RANGE_RE.findall(text):
        lo_i, hi_i = int(lo), int(hi)
        if lo_i <= hi_i <= lo_i + 50:
            ids.update(f"{prefix}{n}" for n in range(lo_i, hi_i + 1))
    return {i for i in ids if re.fullmatch(pattern, i)}


def first_cell_ids(path: Path, pattern: str) -> set[str]:
    """IDs defined as the first cell of a table row, e.g. '| REQ-L1 | ...'."""
    return {row[0] for row in table_rows(path) if row and re.fullmatch(pattern, row[0])}


def traceability_section(text: str) -> str:
    m = re.search(r"^## Traceability.*?(?=^## |\Z)", text, re.M | re.S)
    return m.group(0) if m else ""


def main() -> int:
    errors: list[str] = []

    # --- definitions ---
    reqs = first_cell_ids(REQUIREMENTS, REQ_RE)
    tests = first_cell_ids(TEST_PLAN, TEST_RE)
    for std in STANDARD_DIR.glob("*.md"):
        tests |= first_cell_ids(std, TEST_RE)
    if not reqs:
        errors.append(f"{REQUIREMENTS.relative_to(ROOT)}: no requirement rows found")
    if not tests:
        errors.append(f"{TEST_PLAN.relative_to(ROOT)}: no test rows found")

    plan_text = TEST_PLAN.read_text(encoding="utf-8")
    trace = traceability_section(plan_text)
    if not trace:
        errors.append(f"{TEST_PLAN.relative_to(ROOT)}: no '## Traceability' section")

    # 1. every requirement is traced
    traced_reqs = set()
    for row in table_rows(trace):
        if row:
            traced_reqs |= expand_ids(row[0], REQ_RE)
    for r in sorted(reqs - traced_reqs, key=_natural):
        errors.append(f"[1] {r} is defined in requirements.md but missing from the test-plan traceability table")
    for r in sorted(traced_reqs - reqs, key=_natural):
        errors.append(f"[1] {r} is in the traceability table but not defined in requirements.md")

    # 2. every referenced test exists
    sources = {
        "requirements.md": REQUIREMENTS.read_text(encoding="utf-8"),
        "test-plan.md (traceability)": trace,
        "hazard-analysis.md": HAZARDS.read_text(encoding="utf-8"),
        "fmea.md": FMEA.read_text(encoding="utf-8"),
    }
    for name, text in sources.items():
        for tid in sorted(expand_ids(text, TEST_RE) - tests, key=_natural):
            errors.append(f"[2] {name} references test {tid}, which is not defined in the test plan or RAS standard")

    # 3. hazard requirement references exist
    for row in table_rows(HAZARDS):
        if not row or not re.fullmatch(r"H\d+", row[0]):
            continue
        for r in sorted(expand_ids(" ".join(row[1:]), REQ_RE) - reqs, key=_natural):
            errors.append(f"[3] hazard {row[0]} references {r}, which is not defined in requirements.md")

    # 4. FMEA S >= 9 rows need a mitigation and a test
    rows = table_rows(FMEA)
    header = next((r for r in rows if "S" in r and "Mitigation" in r), None)
    if header is None:
        errors.append("[4] fmea.md: could not find the table header (S, Mitigation, Test)")
    else:
        si, mi, ti = header.index("S"), header.index("Mitigation"), header.index("Test")
        for row in rows:
            if row is header or len(row) <= max(si, mi, ti):
                continue
            s = re.sub(r"\D", "", row[si])
            if s and int(s) >= 9:
                label = f"{row[0]} / {row[1]}"
                if not row[mi].strip("-— "):
                    errors.append(f"[4] FMEA row '{label}' has S={s} but no mitigation")
                if not row[ti].strip("-— "):
                    errors.append(f"[4] FMEA row '{label}' has S={s} but no verifying test")

    # 5. DRAFT banner on safety docs unless signed off in review/
    review_text = " ".join(p.read_text(encoding="utf-8") for p in REVIEW_DIR.glob("*.md")
                           if p.name.lower() != "readme.md") if REVIEW_DIR.exists() else ""
    safety_docs = [REQUIREMENTS] + [p for d in SAFETY_DOC_DIRS for p in sorted((DOCS / d).rglob("*.md"))]
    for doc in safety_docs:
        rel = doc.relative_to(ROOT).as_posix()
        if DRAFT_MARKER in doc.read_text(encoding="utf-8"):
            continue
        if rel in review_text:
            continue
        errors.append(f"[5] {rel} has no DRAFT banner and no sign-off record in review/")

    print(f"RideBelt traceability check: {len(reqs)} requirements, {len(tests)} tests, "
          f"{len(safety_docs)} safety docs")
    if errors:
        print(f"\nFAILED with {len(errors)} problem(s):")
        for e in errors:
            print("  - " + e)
        return 1
    print("PASSED")
    return 0


def _natural(s: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


if __name__ == "__main__":
    sys.exit(main())
