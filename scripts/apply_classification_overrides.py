#!/usr/bin/env python3
"""Apply reviewed unit overrides to the existing broad question index."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "all-unit-question-index.json"
OVERRIDES = ROOT / "data" / "manual-classification-overrides.json"


def main() -> None:
    records = json.loads(INDEX.read_text(encoding="utf-8"))
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    by_key = {
        f"{record['sourceFile']}#{record['questionNumber']}": record
        for record in records
    }
    missing = sorted(set(overrides) - set(by_key))
    if missing:
        raise KeyError(f"Overrides have no matching question records: {missing}")

    changed = 0
    for key, override in overrides.items():
        record = by_key[key]
        unit = int(override["unit"])
        if record["suggestedUnit"] != unit or record["classificationStatus"] != "manual-reviewed-override":
            record["suggestedUnit"] = unit
            record["classificationStatus"] = "manual-reviewed-override"
            changed += 1

    INDEX.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Applied {len(overrides)} overrides; changed {changed} index records")


if __name__ == "__main__":
    main()
