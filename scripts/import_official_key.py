#!/usr/bin/env python3
"""Import an official NTA Question-ID/Option-ID key into the public registry."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "official-answer-keys.json"


def pdf_text(path: Path) -> str:
    return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)


def question_option_ids(path: Path, first_id: int, last_id: int) -> dict[int, list[int]]:
    text = pdf_text(path)
    markers = [
        marker for marker in re.finditer(r"\[?Question ID\s*[=:-]+\s*(\d+)", text, re.I)
        if first_id <= int(marker.group(1)) <= last_id
    ]
    result = {}
    for index, marker in enumerate(markers):
        question_id = int(marker.group(1))
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        option_ids = [
            int(value) for value in re.findall(r"\[Option ID\s*[=:-]+\s*(\d+)\]", text[marker.end():end], re.I)
        ][:4]
        if len(option_ids) == 4:
            result[question_id] = option_ids
    return result


def official_pairs(path: Path, page_number: int, first_id: int, last_id: int) -> dict[int, str]:
    reader = PdfReader(path)
    if not 1 <= page_number <= len(reader.pages):
        raise SystemExit(f"Official-key page {page_number} is outside the PDF")
    text = reader.pages[page_number - 1].extract_text() or ""
    if "Computer Science" not in text or "(087)" not in text:
        raise SystemExit(f"Official-key page {page_number} is not labelled Subject 087 Computer Science")
    pairs = {}
    for question, answer in re.findall(r"(?m)^\s*(\d+)\s+([0-9%,&]+)\s*$", text):
        question_id = int(question)
        if first_id <= question_id <= last_id:
            pairs[question_id] = answer
    return pairs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--key-pdf", type=Path, required=True)
    parser.add_argument("--key-page", type=int, required=True, help="One-based page containing Subject 087")
    parser.add_argument("--question-pdf", type=Path, required=True)
    parser.add_argument("--source-file", required=True)
    parser.add_argument("--first-id", type=int, required=True)
    parser.add_argument("--last-id", type=int, required=True)
    parser.add_argument("--registry-key", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--exam-date", required=True)
    parser.add_argument("--official-url", required=True)
    args = parser.parse_args()

    official = official_pairs(args.key_pdf, args.key_page, args.first_id, args.last_id)
    option_ids = question_option_ids(args.question_pdf, args.first_id, args.last_id)
    expected = args.last_id - args.first_id + 1
    if len(official) != expected:
        raise SystemExit(f"Official key has {len(official)} entries; expected {expected}")

    entries = {}
    for question_id in range(args.first_id, args.last_id + 1):
        raw_answer = official[question_id]
        key_status = "single-option"
        correct_ids: list[int] = []
        correct_options: list[int] = []
        if raw_answer == "%":
            key_status = "marks-awarded-to-all"
        elif raw_answer == "&":
            key_status = "not-evaluated"
        else:
            correct_ids = [int(value) for value in raw_answer.split(",")]
            choices = option_ids.get(question_id, [])
            correct_options = [choices.index(value) + 1 for value in correct_ids if value in choices]
            if len(correct_ids) > 1:
                key_status = "multiple-options-accepted"
            if len(correct_options) != len(correct_ids):
                raise SystemExit(f"Could not map official Option ID for Question ID {question_id}")
        entries[str(question_id - args.first_id + 1)] = {
            "questionId": question_id,
            "correctOptionIds": correct_ids,
            "correctOptions": correct_options,
            "keyStatus": key_status,
        }

    registry = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}
    registry[args.registry_key] = {
        "authority": "National Testing Agency (NTA)",
        "title": args.title,
        "examDate": args.exam_date,
        "subject": "087 Computer Science and Applications",
        "sourceFile": args.source_file,
        "officialUrl": args.official_url,
        "officialKeyPdfPage": args.key_page,
        "entries": entries,
    }
    REGISTRY.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    statuses = {}
    for entry in entries.values():
        statuses[entry["keyStatus"]] = statuses.get(entry["keyStatus"], 0) + 1
    print(json.dumps({"imported": len(entries), "statuses": statuses}, indent=2))


if __name__ == "__main__":
    main()
