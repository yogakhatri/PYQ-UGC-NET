#!/usr/bin/env python3
"""Recover numbered MCQs from image-collage papers using Vision OCR boxes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


START = re.compile(r"^\s*(\d{2,3})\.\s*(.*)$")
OPTION = re.compile(r"\(([1-4])\)")
SPACE = re.compile(r"\s+")
NOISE = re.compile(r"UGC NET .*Unofficial|PAPER\s*-\s*II", re.I)


def clean(text: str) -> str:
    return SPACE.sub(" ", text).strip()


def parse(text: str) -> tuple[str, list[str]] | None:
    markers = list(OPTION.finditer(text))
    choices = []
    for index in range(len(markers) - 3):
        group = markers[index:index + 4]
        if [marker.group(1) for marker in group] == ["1", "2", "3", "4"]:
            choices.append(group)
    for group in reversed(choices):
        stem = clean(text[:group[0].start()])
        options = []
        for index, marker in enumerate(group):
            end = group[index + 1].start() if index < 3 else len(text)
            options.append(clean(text[marker.end():end]))
        if stem and all(options):
            return stem, options
    return None


def reading_order(rows: list[dict], tolerance: float = 0.021) -> list[dict]:
    """Order slightly skewed photographed lines before reading left-to-right."""
    remaining = sorted(rows, key=lambda row: -row["y"])
    ordered = []
    while remaining:
        top = remaining[0]["y"]
        line = [row for row in remaining if top - row["y"] <= tolerance]
        remaining = [row for row in remaining if top - row["y"] > tolerance]
        ordered.extend(sorted(line, key=lambda row: row["x"]))
    return ordered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("boxes_jsonl", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--minimum", type=int, required=True)
    parser.add_argument("--maximum", type=int, required=True)
    parser.add_argument("--line-tolerance", type=float, default=0.021)
    args = parser.parse_args()

    pages: dict[int, list[dict]] = {}
    for line in args.boxes_jsonl.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        pages.setdefault(row["page"], []).append(row)

    best: dict[int, dict] = {}
    for page, rows in pages.items():
        ordered = reading_order(rows, args.line_tolerance)
        starts = []
        for index, row in enumerate(ordered):
            match = START.match(row["text"].strip())
            if match and args.minimum <= int(match.group(1)) <= args.maximum:
                starts.append((index, int(match.group(1)), match.group(2)))
        for position, (start, number, first_text) in enumerate(starts):
            end = starts[position + 1][0] if position + 1 < len(starts) else len(ordered)
            parts = [first_text]
            parts.extend(
                row["text"].strip() for row in ordered[start + 1:end]
                if not NOISE.search(row["text"])
            )
            parsed = parse(clean(" ".join(parts)))
            if not parsed:
                continue
            stem, options = parsed
            raw_text = stem + " " + " ".join(
                f"({index}) {option}" for index, option in enumerate(options, 1)
            )
            candidate = {
                "sourcePage": page,
                "rawText": raw_text,
            }
            if len(raw_text) > len(best.get(number, {}).get("rawText", "")):
                best[number] = candidate

    output = {
        f"{args.source_file}#{number}": record
        for number, record in sorted(best.items())
    }
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Recovered {len(output)} complete collage questions")


if __name__ == "__main__":
    main()
