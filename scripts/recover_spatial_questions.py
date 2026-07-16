#!/usr/bin/env python3
"""Recover question text and four choices from Vision OCR bounding boxes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HEADER = re.compile(r"\bQuestion Number\s*:\s*(\d+)\b", re.I)
QUESTION_ID = re.compile(r"\bQuestion Id\s*:\s*(\d+)\b", re.I)
OPTION_ID = re.compile(r"^\D*(\d{8,})\s*\.?\s*$")
MAPPING_ID = re.compile(r"^\D*\d{8,}\s*\.\s*[1-4]\s*$")
CHOICE_LABEL = re.compile(r"^\s*([1-4])\s*[.)]\s*(.*)$")
METADATA = re.compile(
    r"Question (?:Number|Id|Type)|Option Shuffling|Display Question|"
    r"Single Line Question|Option Orientation|Correct Marks|Wrong Marks",
    re.I,
)
NOISE = re.compile(r"prepp|Personal Exams Guide|www\.", re.I)


def option_text(rows: list[dict], ids: list[dict], index: int, options_y: float) -> str:
    current = ids[index]
    upper = options_y if index == 0 else (ids[index - 1]["y"] + current["y"]) / 2
    lower = -1.0 if index == len(ids) - 1 else (current["y"] + ids[index + 1]["y"]) / 2
    min_x = max(0.16, current["x"] + current["w"] + 0.003)
    values = [
        row for row in rows
        if lower < row["y"] < upper
        and row["x"] >= min_x
        and not OPTION_ID.match(row["text"].strip())
        and not NOISE.search(row["text"])
    ]
    values.sort(key=lambda row: (-row["y"], row["x"]))
    tokens = [row["text"].strip() for row in values if row["text"].strip() not in {"Options", "Options:"}]
    numeric = [token for token in tokens if re.fullmatch(r"[+−-]?\d+(?:\.\d+)?", token)]
    if len(numeric) == 2 and len(tokens) <= 3:
        return f"{numeric[0]}/{numeric[1]}"
    return " ".join(token for token in tokens if token not in {"-", "―", "—"}).strip()


def recover_block(page: int, rows: list[dict], question_id_offset: int | None = None) -> dict | None:
    header = rows[0]["text"]
    number_match = HEADER.search(header)
    id_match = QUESTION_ID.search(header)
    if number_match:
        question_number = int(number_match.group(1))
    elif id_match and question_id_offset is not None:
        question_number = int(id_match.group(1)) - question_id_offset
    else:
        return None
    options_index = next(
        (i for i, row in enumerate(rows) if re.fullmatch(r"\s*(?:Code\s*:\s*)?Options?\s*:\s*", row["text"], re.I)),
        None,
    )
    if options_index is None:
        return None
    options_y = rows[options_index]["y"]
    ids = [row for row in rows[options_index + 1:] if OPTION_ID.match(row["text"].strip())]
    ids.sort(key=lambda row: -row["y"])
    if len(ids) == 4:
        stem_rows = [
            row for row in rows[1:options_index]
            if not METADATA.search(row["text"])
            and not NOISE.search(row["text"])
        ]
        options = [option_text(rows, ids, i, options_y) for i in range(4)]
    else:
        # Some exports print the visible choices first, followed by four
        # ``option-id.choice-number`` mapping rows.  Recover the visible columns.
        mappings = [row for row in rows[options_index + 1:] if MAPPING_ID.match(row["text"].strip())]
        labels = [
            (i, row, CHOICE_LABEL.match(row["text"].strip()))
            for i, row in enumerate(rows[:options_index])
            if CHOICE_LABEL.match(row["text"].strip())
        ]
        sequences = []
        for i in range(len(labels) - 3):
            seq = labels[i:i + 4]
            if [entry[2].group(1) for entry in seq] == ["1", "2", "3", "4"]:
                sequences.append(seq)
        if len(mappings) != 4 or not sequences:
            return None
        sequence = sequences[-1]
        first_label_index = sequence[0][0]
        stem_rows = [
            row for row in rows[1:first_label_index]
            if not METADATA.search(row["text"]) and not NOISE.search(row["text"])
        ]
        options = []
        for i, (start, label_row, _) in enumerate(sequence):
            end = sequence[i + 1][0] if i < 3 else options_index
            values = ([sequence[i][2].group(2).strip()] if sequence[i][2].group(2).strip() else []) + [
                row["text"].strip() for row in rows[start + 1:end]
                if row["x"] > label_row["x"] + 0.015
                and not NOISE.search(row["text"])
            ]
            options.append(" ".join(values).strip())

    stem_rows.sort(key=lambda row: (-row["y"], row["x"]))
    stem = " ".join(row["text"].strip() for row in stem_rows).strip()
    if not stem or not all(options):
        return None
    return {
        "questionNumber": question_number,
        "sourcePage": page,
        "questionId": id_match.group(1) if id_match else None,
        "rawText": stem + " " + " ".join(f"{i}. {value}" for i, value in enumerate(options, 1)),
        "_score": len(stem) + 20 * sum(bool(value) for value in options),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("boxes_jsonl", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--question-id-offset", type=int)
    args = parser.parse_args()

    by_page: dict[int, list[dict]] = {}
    for line in args.boxes_jsonl.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        by_page.setdefault(row["page"], []).append(row)

    best: dict[int, dict] = {}
    for page, page_rows in by_page.items():
        ordered = sorted(page_rows, key=lambda row: (-row["y"], row["x"]))
        starts = [
            i for i, row in enumerate(ordered)
            if HEADER.search(row["text"])
            or (args.question_id_offset is not None and QUESTION_ID.search(row["text"]))
        ]
        for position, start in enumerate(starts):
            end = starts[position + 1] if position + 1 < len(starts) else len(ordered)
            candidate = recover_block(page, ordered[start:end], args.question_id_offset)
            if candidate and candidate["_score"] > best.get(candidate["questionNumber"], {"_score": -1})["_score"]:
                best[candidate["questionNumber"]] = candidate

    output = {}
    for number, record in sorted(best.items()):
        record.pop("_score", None)
        output[f"{args.source_file}#{number}"] = record
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Recovered {len(output)} complete four-option questions")


if __name__ == "__main__":
    main()
