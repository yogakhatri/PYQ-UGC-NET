#!/usr/bin/env python3
"""Validate the minimal learner guide, canonical data and generated cards."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def check_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if re.match(r"https?://", target):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (path.parent / clean).resolve().exists():
            raise AssertionError(f"Broken link in {path}: {target}")


def main() -> None:
    corpus = load("question-corpus.json")
    classifications = load("question-classification.json")["questions"]
    solutions = load("solutions.json")

    question_ids = [row["id"] for row in corpus]
    classification_ids = [row["id"] for row in classifications]
    assert len(question_ids) == len(set(question_ids)) == 2460
    assert len(classification_ids) == len(set(classification_ids)) == 2460
    assert set(question_ids) == set(classification_ids)
    assert set(solutions) <= set(question_ids)

    cards = sorted((DOCS / "units").glob("unit-*/**/*.md"))
    cards = [path for path in cards if path.name != "README.md"]
    assert len(cards) == len(solutions)
    required = [
        "> [!TIP]",
        "## Solution",
        "## Key Points",
    ]
    for path in cards:
        text = path.read_text(encoding="utf-8")
        assert all(section in text for section in required), path
        assert (
            "## Why the other options are incorrect" in text
            or "## Common mistakes to avoid" in text
        ), path

    markdown = [DOCS / "README.md", DOCS / "45-day-plan.md"]
    markdown.extend((DOCS / "units").glob("unit-*/README.md"))
    markdown.extend(cards)
    for path in markdown:
        check_links(path)

    print(f"Guide checks passed: 2,460 questions, {len(solutions)} complete learning cards")


if __name__ == "__main__":
    main()
