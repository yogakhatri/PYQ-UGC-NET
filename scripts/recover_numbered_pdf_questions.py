#!/usr/bin/env python3
"""Recover four-option questions from text-layer exam booklets.

The input is Poppler ``pdftotext -layout`` output.  This utility only
reconstructs question text and choices; it never reads answer keys.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


QUESTION = re.compile(r"(?m)^\s*(\d{1,3})\.\s+(?=\S)")
OPTION = re.compile(r"\(([1-4])\)")
SPACE = re.compile(r"\s+")


def clean(value: str) -> str:
    return SPACE.sub(" ", value).strip()


def parse_options(block: str) -> tuple[str, list[str]] | None:
    markers = list(OPTION.finditer(block))
    for start in range(len(markers) - 3):
        group = markers[start : start + 4]
        if [item.group(1) for item in group] != ["1", "2", "3", "4"]:
            continue
        stem = clean(block[: group[0].start()])
        options = []
        for index, marker in enumerate(group):
            end = group[index + 1].start() if index < 3 else len(block)
            options.append(clean(block[marker.end() : end]))
        if stem and all(options):
            return stem, options
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("layout_text", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--maximum", type=int, default=150)
    args = parser.parse_args()

    pages = args.layout_text.read_text(encoding="utf-8", errors="replace").split("\f")
    recovered: dict[str, dict] = {}
    for page_number, page in enumerate(pages, 1):
        starts = list(QUESTION.finditer(page))
        for index, match in enumerate(starts):
            number = int(match.group(1))
            if not 1 <= number <= args.maximum:
                continue
            end = starts[index + 1].start() if index + 1 < len(starts) else len(page)
            parsed = parse_options(page[match.end() : end])
            if not parsed:
                continue
            stem, options = parsed
            raw_text = stem + " " + " ".join(
                f"({position}) {option}" for position, option in enumerate(options, 1)
            )
            key = f"{args.source_file}#{number}"
            candidate = {
                "sourcePage": page_number,
                "rawText": raw_text,
            }
            # Cover-page instructions can look numbered. Prefer later pages and
            # then the candidate containing more question content.
            rank = (page_number > 1, len(raw_text))
            previous = recovered.get(key)
            previous_rank = (-1, -1) if previous is None else (
                previous["sourcePage"] > 1,
                len(previous["rawText"]),
            )
            if rank > previous_rank:
                recovered[key] = candidate

    args.output.write_text(
        json.dumps(recovered, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Recovered {len(recovered)} complete numbered questions")


if __name__ == "__main__":
    main()
