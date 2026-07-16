#!/usr/bin/env python3
"""Recover numbered booklet questions from spatial OCR JSONL."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


QUESTION_START = re.compile(r"^\s*(\d{1,3})\)\s*(.*)$")
QUESTION_ID = re.compile(r"\[?Question ID\s*=\s*(\d+)", re.I)
OPTION_START = re.compile(r"^\s*([1-4])\.\s*(.*)$")
OPTION_ID = re.compile(r"\[?Option ID\s*=", re.I)
NOISE = re.compile(r"(?:UGC NET \d{4}|Topic\s*:|Personal Exam|prepp|www\.)", re.I)
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("boxes_jsonl", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    index_rows = json.loads((ROOT / "data" / "all-unit-question-index.json").read_text(encoding="utf-8"))
    expected_pages = {
        int(row["questionNumber"]): int(row["sourcePage"])
        for row in index_rows
        if row["sourceFile"] == args.source_file
    }

    pages: dict[int, list[dict]] = {}
    for line in args.boxes_jsonl.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        pages.setdefault(row["page"], []).append(row)
    rows = []
    for page in sorted(pages):
        ordered = sorted(pages[page], key=lambda row: (-row["y"], row["x"]))
        rows.extend([{**row, "page": page} for row in ordered])

    starts = [i for i, row in enumerate(rows) if QUESTION_START.match(row["text"].strip())]
    recovered = {}
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(rows)
        block = rows[start:end]
        match = QUESTION_START.match(block[0]["text"].strip())
        number = int(match.group(1))
        if not 1 <= number <= 150:
            continue
        qid_index = next((i for i, row in enumerate(block) if QUESTION_ID.search(row["text"])), None)
        if qid_index is None:
            continue
        qid_match = QUESTION_ID.search(block[qid_index]["text"])
        stem_parts = [match.group(2).strip()]
        stem_parts.extend(
            row["text"].strip() for row in block[1:qid_index]
            if not NOISE.search(row["text"])
        )
        stem = " ".join(part for part in stem_parts if part).strip()

        option_rows = block[qid_index + 1:]
        next_qid = next((i for i, row in enumerate(option_rows) if QUESTION_ID.search(row["text"])), None)
        if next_qid is not None:
            option_rows = option_rows[:next_qid]
        label_positions = []
        for i, row in enumerate(option_rows):
            label = OPTION_START.match(row["text"].strip())
            if label:
                label_positions.append((i, label))
        sequences = []
        for i in range(len(label_positions) - 3):
            seq = label_positions[i:i + 4]
            if [entry[1].group(1) for entry in seq] == ["1", "2", "3", "4"]:
                sequences.append(seq)
        if not sequences:
            continue
        seq = sequences[0]
        options = []
        for i, (option_start, label) in enumerate(seq):
            option_end = seq[i + 1][0] if i < 3 else len(option_rows)
            parts = [label.group(2).strip()]
            for row in option_rows[option_start + 1:option_end]:
                text = row["text"].strip()
                if OPTION_ID.search(text):
                    continue
                if NOISE.search(text) or QUESTION_START.match(text):
                    continue
                parts.append(text)
            options.append(" ".join(part for part in parts if part).strip())
        if not stem or not all(options):
            continue
        key = f"{args.source_file}#{number}"
        candidate = {
            "questionNumber": number,
            "sourcePage": block[0]["page"],
            "questionId": qid_match.group(1),
            "rawText": stem + " " + " ".join(f"{i}. {value}" for i, value in enumerate(options, 1)),
        }
        if number in expected_pages and abs(candidate["sourcePage"] - expected_pages[number]) > 2:
            continue
        old = recovered.get(key)
        candidate_rank = (
            -abs(candidate["sourcePage"] - expected_pages.get(number, candidate["sourcePage"])),
            len(candidate["rawText"]),
        )
        old_rank = (-10**9, -1) if old is None else (
            -abs(old["sourcePage"] - expected_pages.get(number, old["sourcePage"])),
            len(old["rawText"]),
        )
        if candidate_rank > old_rank:
            recovered[key] = candidate

    args.output.write_text(json.dumps(recovered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Recovered {len(recovered)} complete booklet questions")


if __name__ == "__main__":
    main()
