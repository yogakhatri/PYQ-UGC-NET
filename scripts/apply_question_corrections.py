#!/usr/bin/env python3
"""Apply visually reviewed stem/option corrections to the broad index."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "all-unit-question-index.json"
CORRECTIONS = ROOT / "data" / "manual-question-corrections.json"
ADDITIONS = ROOT / "data" / "manual-question-additions.json"
SPATIAL_CORRECTIONS = ROOT / "data" / "spatial-question-corrections.json"
EXCLUSIONS = ROOT / "data" / "manual-question-exclusions.json"


def main() -> None:
    records = json.loads(INDEX.read_text(encoding="utf-8"))
    exclusions = set(json.loads(EXCLUSIONS.read_text(encoding="utf-8"))) if EXCLUSIONS.exists() else set()
    records = [
        record for record in records
        if f"{record['sourceFile']}#{record['questionNumber']}" not in exclusions
    ]
    corrections = json.loads(CORRECTIONS.read_text(encoding="utf-8"))
    additions = json.loads(ADDITIONS.read_text(encoding="utf-8")) if ADDITIONS.exists() else []
    by_key = {
        f"{record['sourceFile']}#{record['questionNumber']}": record
        for record in records
    }
    if SPATIAL_CORRECTIONS.exists():
        spatial = json.loads(SPATIAL_CORRECTIONS.read_text(encoding="utf-8"))
        corrections = {
            **{key: value for key, value in spatial.items() if key in by_key},
            **corrections,  # Deliberate visual corrections take precedence.
        }
    correction_targets = {}
    missing = []
    for key, correction in corrections.items():
        target = by_key.get(key)
        if target is None and "questionNumber" in correction:
            source_file = key.rsplit("#", 1)[0]
            target = by_key.get(f"{source_file}#{correction['questionNumber']}")
        if target is None:
            missing.append(key)
        else:
            correction_targets[key] = target
    missing.sort()
    if missing:
        raise KeyError(f"Corrections have no matching question records: {missing}")

    added = 0
    for addition in additions:
        key = f"{addition['sourceFile']}#{addition['questionNumber']}"
        if key in by_key:
            continue
        records.append(addition)
        by_key[key] = addition
        added += 1

    changed = 0
    for key, correction in corrections.items():
        record = correction_targets[key]
        for field in ("questionNumber", "rawText", "sourcePage", "questionId", "questionContext", "visualAsset"):
            if field in correction and record.get(field) != correction[field]:
                record[field] = correction[field]
                changed += 1

    records.sort(key=lambda record: (record["sourceFile"], record["questionNumber"]))
    INDEX.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Applied {len(corrections)} question corrections; "
        f"changed {changed} fields; added {added} recovered questions"
    )


if __name__ == "__main__":
    main()
