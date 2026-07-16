#!/usr/bin/env python3
"""Recover questions from a booklet PDF while discarding answer overlays first."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


MARKER = re.compile(
    r"\[?Question ID\s*=\s*(\d+)\]?\s*"
    r"\[?Question Description\s*=\s*([^\]\n]+)",
    re.I,
)
OPTION = re.compile(
    r"(?m)^\s*([1-4])\.\s*(.*?)\s*\[Option ID\s*=\s*\d+\]\s*$"
)
ANSWER_OVERLAY = re.compile(
    r"Correct Answer\s*[:‐-]+.*?\[Option ID\s*=\s*\d+\]",
    re.I | re.S,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    reader = PdfReader(args.source_file)
    pages = [(page.extract_text() or "") for page in reader.pages]
    text = "\n".join(pages)
    # This is deliberately the first semantic operation.  Answer overlays are
    # removed, never copied into the question recovery or used for selection.
    text = ANSWER_OVERLAY.sub("\n", text)
    markers = list(MARKER.finditer(text))
    recovered = {}
    previous_option_end = 0
    for marker in markers:
        description = marker.group(2)
        number_match = re.search(r"_Q(\d{1,3})\b", description, re.I)
        if not number_match:
            continue
        number = int(number_match.group(1))
        stem = text[previous_option_end:marker.start()].strip()
        stem = re.sub(r"(?m)^\s*\d{1,3}\)\s*", "", stem)
        stem = re.sub(r"\s+", " ", stem).strip()

        following = text[marker.end():]
        options = []
        option_end = None
        for option in OPTION.finditer(following):
            expected = len(options) + 1
            if int(option.group(1)) != expected:
                if options:
                    break
                continue
            options.append(re.sub(r"\s+", " ", option.group(2)).strip())
            option_end = marker.end() + option.end()
            if len(options) == 4:
                break
        if len(options) == 4 and stem and all(options):
            key = f"{args.source_file}#{number}"
            recovered.setdefault(key, {
                "questionNumber": number,
                "questionId": marker.group(1),
                "rawText": stem + " " + " ".join(
                    f"{i}. {value}" for i, value in enumerate(options, 1)
                ),
            })
        if option_end is not None:
            previous_option_end = option_end

    if any(re.search(r"Correct Answer\s*[:‐-]", row["rawText"], re.I) for row in recovered.values()):
        raise ValueError("Answer overlay survived question-only recovery")
    args.output.write_text(json.dumps(recovered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Recovered {len(recovered)} questions after discarding answer overlays")


if __name__ == "__main__":
    main()
