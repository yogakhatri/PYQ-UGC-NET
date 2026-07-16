#!/usr/bin/env python3
"""Merge old and rebuilt extraction per source/question without adding unreviewed keys."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOILERPLATE = re.compile(
    r"this paper consists|if you write your name|name, roll number, phone number|"
    r"instructions for the candidates|test booklet, except|commencement of examination|"
    r"rough work is to be done|negative marks for incorrect answers",
    re.IGNORECASE,
)
EXPLANATION = re.compile(
    r"^\s*\d+[.)]?\s*(?:Answer|Explanation)\s*:|"
    r"\b(?:Download Prepp APP|Collegedunia)\b",
    re.IGNORECASE,
)
OPTIONS = re.compile(
    r"(?:\([A-D]\)|\([1-4]\)|(?<!\w)[A-D]\.\s|(?<!\w)[1-4]\.\s)",
    re.IGNORECASE,
)


def key(record: dict) -> tuple[str, int]:
    return record["sourceFile"], int(record["questionNumber"])


def quality(record: dict) -> tuple[int, int]:
    text = record["rawText"]
    score = 0
    if BOILERPLATE.search(text):
        score -= 10_000
    if EXPLANATION.search(text):
        score -= 5_000
    option_count = len(OPTIONS.findall(text))
    score += min(option_count, 4) * 100
    if "?" in text:
        score += 40
    if re.search(r"\b(?:which|what|find|consider|given|match|let|calculate|identify)\b", text, re.I):
        score += 20
    if 40 <= len(text) <= 2500:
        score += 10
    if len(text) > 6000:
        score -= 100
    return score, len(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("old", type=Path)
    parser.add_argument("rebuilt", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("review", type=Path)
    args = parser.parse_args()

    old = json.loads(args.old.read_text(encoding="utf-8"))
    rebuilt = json.loads(args.rebuilt.read_text(encoding="utf-8"))
    old_by = {key(record): record for record in old}
    rebuilt_by = {key(record): record for record in rebuilt}

    merged = []
    changed = []
    for record in old:
        record_key = key(record)
        candidate = rebuilt_by.get(record_key)
        selected = record
        if candidate:
            old_score = quality(record)[0]
            candidate_score = quality(candidate)[0]
            # Automatic replacement is intentionally conservative. A rebuilt
            # block must look like a complete MCQ and improve the semantic
            # score, not merely be a longer OCR fragment.
            if candidate_score >= 400 and candidate_score > old_score:
                selected = candidate
        merged.append(selected)
        if selected is candidate and candidate["rawText"] != record["rawText"]:
            changed.append({
                "id": f"{record_key[0]}#{record_key[1]}",
                "oldQuality": quality(record),
                "newQuality": quality(candidate),
            })

    new_only = [
        record for record_key, record in rebuilt_by.items()
        if record_key not in old_by
    ]
    lost = [
        record for record_key, record in old_by.items()
        if record_key not in rebuilt_by
    ]
    review = {
        "changedExistingRecords": changed,
        "newOnlyRequiresManualReview": new_only,
        "notRecoveredByRebuild": lost,
    }

    args.output.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.review.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Merged {len(merged)} existing positions; selected rebuilt text for {len(changed)}")
    print(f"Manual review: {len(new_only)} new-only, {len(lost)} old-only")


if __name__ == "__main__":
    main()
