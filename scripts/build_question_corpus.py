#!/usr/bin/env python3
"""Build a questions-only corpus without reading answer or solution data."""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_remaining_unit_guides import (
    display_question,
    split_damaged_options,
    split_options,
    truncate_merged_next_question,
)


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "all-unit-question-index.json"
OUT = ROOT / "data" / "question-corpus.json"
REJECTED_OUT = ROOT / "data" / "rejected-extraction-blocks.json"

VISUAL_PATTERN = re.compile(
    r"\b(?:figure|diagram|graph shown|circuit|image|transition diagram|"
    r"table given|matrix shown|following graph|shown below)\b",
    re.IGNORECASE,
)
OCR_PATTERN = re.compile(
    r"(?:\bform\s*[<>]{1,2}|\bIform\b|\.{3,}|_{5,}|"
    r"\b(?:ili|seimigroup|donot|dec sription)\b)",
    re.IGNORECASE,
)
NON_QUESTION_PATTERN = re.compile(
    r"\b(?:write your roll number|this paper consists of|return the (?:original )?omr sheet|"
    r"use of any calculator or log table|faulty booklets|if you write your name|"
    r"do not accept a booklet|tear off the paper seal|outside the examination hall)\b",
    re.IGNORECASE,
)


def remove_answer_artifacts(text: str) -> str:
    """Remove answer overlays if extraction accidentally retained one."""
    text = re.split(
        r"(?im)^\s*(?:Correct Answer|Answer|Solution)\s*[:：]",
        text,
        maxsplit=1,
    )[0]
    text = re.sub(r"\[Option ID[^\]]*\]", " ", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def parsed_question(record: dict) -> dict:
    cleaned = display_question(
        truncate_merged_next_question(record["rawText"], record["questionNumber"])
    )
    cleaned = remove_answer_artifacts(cleaned)
    parsed = split_options(cleaned)
    extraction_status = "complete-four-options"
    if parsed is None:
        parsed = split_damaged_options(cleaned)
        extraction_status = "damaged-four-options" if parsed else "no-four-option-set"
    if (
        extraction_status == "no-four-option-set"
        and record["sourceFile"].endswith("ugc-net-cs-2011-dec-paper-3.pdf")
    ):
        extraction_status = "complete-descriptive"

    if parsed:
        stem, labels, values = parsed
        options = [
            {"label": label, "text": value}
            for label, value in zip(labels, values)
        ]
    else:
        stem = cleaned
        options = []

    return {
        "id": f"{record['sourceFile']}#{record['questionNumber']}",
        "exam": record["exam"],
        "sourceFile": record["sourceFile"],
        "sourcePage": record["sourcePage"],
        "questionNumber": record["questionNumber"],
        "questionId": record.get("questionId"),
        "suggestedUnit": record["suggestedUnit"],
        "classificationStatus": record["classificationStatus"],
        "context": remove_answer_artifacts(record.get("questionContext", "")),
        "visualAsset": record.get("visualAsset"),
        "stem": stem,
        "options": options,
        "extractionStatus": extraction_status,
        "needsVisualReview": bool(VISUAL_PATTERN.search(stem)),
        "possibleOcrDamage": bool(OCR_PATTERN.search(cleaned)),
    }


def main() -> None:
    records = json.loads(INDEX.read_text(encoding="utf-8"))
    rejected = [
        {
            "id": f"{record['sourceFile']}#{record['questionNumber']}",
            "sourceFile": record["sourceFile"],
            "sourcePage": record["sourcePage"],
            "questionNumber": record["questionNumber"],
            "reason": "instruction-or-cover-page-text",
            "rawText": record["rawText"],
        }
        for record in records
        if NON_QUESTION_PATTERN.search(record["rawText"])
    ]
    rejected_ids = {record["id"] for record in rejected}
    corpus = [
        parsed_question(record) for record in records
        if f"{record['sourceFile']}#{record['questionNumber']}" not in rejected_ids
    ]
    ids = [record["id"] for record in corpus]
    if len(ids) != len(set(ids)):
        raise ValueError("Question corpus contains duplicate source/question IDs")
    if len(corpus) + len(rejected) != len(records):
        raise ValueError("Question corpus accounting does not match source index")
    if any("answer" in key.lower() for record in corpus for key in record):
        raise ValueError("Questions-only corpus unexpectedly contains an answer field")

    OUT.write_text(
        json.dumps(corpus, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    REJECTED_OUT.write_text(
        json.dumps(rejected, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    totals: dict[str, int] = {}
    for record in corpus:
        status = record["extractionStatus"]
        totals[status] = totals.get(status, 0) + 1
    print(f"Wrote {len(corpus)} questions without answers; rejected {len(rejected)} non-question blocks")
    print(json.dumps(totals, indent=2))


if __name__ == "__main__":
    main()
