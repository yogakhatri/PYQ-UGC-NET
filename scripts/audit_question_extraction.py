#!/usr/bin/env python3
"""Audit questions-only extraction completeness without reading answer data."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "data" / "question-corpus.json"
REJECTED = ROOT / "data" / "rejected-extraction-blocks.json"
OUT_JSON = ROOT / "data" / "question-extraction-audit.json"
OUT_MD = ROOT / "data" / "question-extraction-audit.md"


def expected_range(source: str) -> tuple[int, int] | None:
    name = Path(source).name
    if "2011-dec-paper-3" in name:
        return 1, 19  # This source is the 19-question descriptive Paper III format.
    if "paper-3" in name:
        return 1, 75
    if "paper-2" in name and "2018-july" not in name and "2023-june" not in name:
        return 1, 50
    if "2018-july-paper-2" in name:
        return 1, 100
    if any(year in name for year in ("2018-dec", "2019-dec", "2019-june", "2020-nov", "2024-aug", "2025-june", "2026-jan")):
        return 51, 150
    if any(year in name for year in ("2021-nov", "2022-oct")):
        return 1, 100
    return None


def main() -> None:
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    rejected = json.loads(REJECTED.read_text(encoding="utf-8"))
    sources = sorted({row["sourceFile"] for row in corpus} | {row["sourceFile"] for row in rejected})
    rows = []
    for source in sources:
        source_rows = [row for row in corpus if row["sourceFile"] == source]
        source_rejected = [row for row in rejected if row["sourceFile"] == source]
        numbers = {int(row["questionNumber"]) for row in source_rows}
        expected = expected_range(source)
        missing = [] if expected is None else sorted(set(range(expected[0], expected[1] + 1)) - numbers)
        rows.append({
            "sourceFile": source,
            "expectedRange": list(expected) if expected else None,
            "validQuestionRecords": len(source_rows),
            "statusCounts": dict(Counter(row["extractionStatus"] for row in source_rows)),
            "rejectedNonQuestionBlocks": len(source_rejected),
            "missingExpectedQuestionNumbers": missing,
        })

    summary = {
        "validQuestionRecords": len(corpus),
        "rejectedNonQuestionBlocks": len(rejected),
        "statusCounts": dict(Counter(row["extractionStatus"] for row in corpus)),
        "knownMissingExpectedPositions": sum(len(row["missingExpectedQuestionNumbers"]) for row in rows),
        "sources": rows,
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Questions-only extraction audit",
        "",
        "This audit is generated only from the question corpus and PDF extraction metadata. It does not read answer keys or solution files.",
        "",
        f"- Valid question records: **{len(corpus)}**",
        f"- Complete four-option records: **{summary['statusCounts'].get('complete-four-options', 0)}**",
        f"- Complete descriptive records: **{summary['statusCounts'].get('complete-descriptive', 0)}**",
        f"- Damaged four-option records: **{summary['statusCounts'].get('damaged-four-options', 0)}**",
        f"- Records still lacking a parsed four-option set: **{summary['statusCounts'].get('no-four-option-set', 0)}**",
        f"- Rejected instruction/cover-page blocks: **{len(rejected)}**",
        f"- Missing positions in papers with a known expected range: **{summary['knownMissingExpectedPositions']}**",
        "",
        "| Source | Valid | Complete | Damaged/no options | Rejected | Missing expected positions |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        counts = row["statusCounts"]
        complete = counts.get("complete-four-options", 0) + counts.get("complete-descriptive", 0)
        damaged = counts.get("damaged-four-options", 0) + counts.get("no-four-option-set", 0)
        missing = row["missingExpectedQuestionNumbers"]
        missing_text = ", ".join(map(str, missing)) if missing else "—"
        if row["expectedRange"] is None:
            missing_text = "range not asserted"
        lines.append(
            f"| `{Path(row['sourceFile']).name}` | {row['validQuestionRecords']} | {complete} | {damaged} | "
            f"{row['rejectedNonQuestionBlocks']} | {missing_text} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in summary.items() if key != "sources"}, indent=2))


if __name__ == "__main__":
    main()
