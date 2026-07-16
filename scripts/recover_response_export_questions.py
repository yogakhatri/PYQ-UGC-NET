#!/usr/bin/env python3
"""Recover MCQs from NTA response-export PDFs using Vision OCR boxes.

The exports repeat option text and include response/option identifiers.  This
parser deliberately retains only the first visible question-and-option set in
each Question Description block and never imports response metadata.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DESCRIPTION = re.compile(r"Question\s+Description", re.I)
QBID = re.compile(r"QBID\s*:\s*([0-9]+)", re.I)
SERIAL = re.compile(r"S[Il1][. ]*\s*No[.: ]*\s*([0-9]+)", re.I)
VISIBLE_OPTION = re.compile(r"^\s*([1-4])[.)]\s*(.*)$")
MAPPING = re.compile(r"^\s*\(([1-4])\)\s*[1-4]\s*$")
OPTION_ID = re.compile(r"Option\s*ID", re.I)
SPACE = re.compile(r"\s+")


def clean(text: str) -> str:
    return SPACE.sub(" ", text).strip()


def ordered_rows(path: Path) -> list[dict]:
    pages: dict[int, list[dict]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        pages.setdefault(row["page"], []).append(row)
    result = []
    for page in sorted(pages):
        result.extend(sorted(pages[page], key=lambda row: (-row["y"], row["x"])))
    return result


def option_group_before_mapping(rows: list[dict]) -> tuple[int, list[str]] | None:
    """Return the option group nearest the first complete response mapping."""
    mapping_starts = []
    for index in range(len(rows) - 3):
        matches = [MAPPING.match(rows[index + offset]["text"]) for offset in range(4)]
        if all(matches) and [match.group(1) for match in matches] == ["1", "2", "3", "4"]:
            mapping_starts.append(index)

    for mapping_start in mapping_starts:
        markers: list[tuple[int, int, str]] = []
        for index in range(mapping_start):
            match = VISIBLE_OPTION.match(rows[index]["text"])
            if match:
                markers.append((index, int(match.group(1)), match.group(2)))
        for marker_pos in range(len(markers) - 4, -1, -1):
            group = markers[marker_pos:marker_pos + 4]
            if [item[1] for item in group] != [1, 2, 3, 4]:
                continue
            if group[-1][0] >= mapping_start:
                continue
            options = []
            for offset, (start, _, first) in enumerate(group):
                end = group[offset + 1][0] if offset < 3 else mapping_start
                parts = [first]
                parts.extend(row["text"] for row in rows[start + 1:end])
                options.append(clean(" ".join(parts)))
            if all(options):
                return group[0][0], options
    return None


def question_start(rows: list[dict], option_start: int) -> tuple[int, str]:
    qbid = ""
    start = 0
    for index, row in enumerate(rows[:option_start]):
        match = QBID.search(row["text"])
        if match:
            qbid = match.group(1)
            start = index + 1
        elif SERIAL.search(row["text"]):
            start = index + 1
        elif OPTION_ID.search(row["text"]):
            start = index + 1
    while start < option_start and (
        rows[start]["text"].startswith("National Testing Agency")
        or rows[start]["text"].startswith("Test Date")
        or rows[start]["text"].startswith("Test Slot")
        or rows[start]["text"].startswith("Subject:")
        or rows[start]["text"].startswith("Paper I")
        or rows[start]["text"].startswith("Paper II")
    ):
        start += 1
    return start, qbid


def parse_block(rows: list[dict]) -> dict | None:
    parsed = option_group_before_mapping(rows)
    if not parsed:
        return None
    option_start, options = parsed
    start, qbid = question_start(rows, option_start)
    stem = clean(" ".join(row["text"] for row in rows[start:option_start]))
    if not stem:
        return None
    raw_text = stem + " " + " ".join(
        f"({number}) {option}" for number, option in enumerate(options, 1)
    )
    return {
        "sourcePage": rows[start]["page"] if start < len(rows) else rows[0]["page"],
        "questionId": qbid,
        "rawText": raw_text,
    }


def described_number(text: str) -> int | None:
    """Read the section-local q-number despite common OCR q/9/4 swaps."""
    match = re.search(r"_(?:q|9|4)([0-9]+)\s*$", text, re.I)
    if not match:
        return None
    local = int(match.group(1))
    lowered = text.lower()
    if "computer_science" in lowered or "_cms_" in lowered:
        return 50 + local
    if "general_paper" in lowered or "_gp30_" in lowered:
        return local
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("boxes_jsonl", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    rows = ordered_rows(args.boxes_jsonl)
    ends = [index for index, row in enumerate(rows) if DESCRIPTION.search(row["text"])]
    blocks = []
    start = 0
    for end in ends:
        blocks.append((rows[start:end], rows[end]["text"]))
        start = end + 1

    recovered = {}
    failures = []
    previous_number = 0
    for ordinal, (block, description) in enumerate(blocks, 1):
        expected = described_number(description)
        number = expected if expected is not None else previous_number + 1
        if number > previous_number + 1:
            # A missing description merges several questions into one block.
            # parse_block returns its first question; preserve the gap for a
            # later visual recovery rather than silently shifting all records.
            number = previous_number + 1
        record = parse_block(block)
        if record:
            recovered[f"{args.source_file}#{number}"] = record
        else:
            failures.append(number)
        previous_number = expected if expected is not None else number

    args.output.write_text(
        json.dumps(recovered, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Descriptions: {len(ends)}; recovered: {len(recovered)}; "
        f"failed blocks: {failures}"
    )


if __name__ == "__main__":
    main()
