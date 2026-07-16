#!/usr/bin/env python3
"""Import independently recovered question-only records missing from the index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "all-unit-question-index.json"
ADDITIONS = ROOT / "data" / "manual-question-additions.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("recovered", nargs="+", type=Path)
    args = parser.parse_args()

    index = json.loads(INDEX.read_text(encoding="utf-8"))
    additions = json.loads(ADDITIONS.read_text(encoding="utf-8"))
    known = {
        f"{row['sourceFile']}#{row['questionNumber']}"
        for row in [*index, *additions]
    }
    imported = 0
    for path in args.recovered:
        candidates = json.loads(path.read_text(encoding="utf-8"))
        for key, candidate in candidates.items():
            if key in known:
                continue
            source_file, number = key.rsplit("#", 1)
            addition = {
                "exam": "UGC NET Computer Science and Applications",
                "sourceFile": source_file,
                "questionNumber": int(number),
                "sourcePage": candidate["sourcePage"],
                "questionId": candidate.get("questionId", ""),
                "rawText": candidate["rawText"],
                "suggestedUnit": None,
                "classificationStatus": "text-layer-recovery-needs-classification",
            }
            if candidate.get("visualAsset"):
                addition["visualAsset"] = candidate["visualAsset"]
            additions.append(addition)
            known.add(key)
            imported += 1
    additions.sort(key=lambda row: (row["sourceFile"], row["questionNumber"]))
    ADDITIONS.write_text(
        json.dumps(additions, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Imported {imported} missing recovered questions")


if __name__ == "__main__":
    main()
