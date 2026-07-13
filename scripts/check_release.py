#!/usr/bin/env python3
"""Run lightweight structural checks before publishing the repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_GUIDES = {
    "unit-1-discrete-structures-and-optimization.md": 143,
    "unit-2-computer-system-architecture.md": 394,
    "unit-3-programming-languages-and-computer-graphics.md": 176,
    "unit-4-database-management-systems.md": 178,
    "unit-5-system-software-and-operating-system.md": 184,
    "unit-6-software-engineering.md": 178,
    "unit-7-data-structures-and-algorithms.md": 250,
    "unit-8-theory-of-computation-and-compilers.md": 223,
    "unit-9-data-communication-and-computer-networks.md": 257,
    "unit-10-artificial-intelligence.md": 98,
}
REQUIRED_PUBLIC_FILES = (
    "README.md",
    "LICENSE",
    "CONTENT_LICENSE.md",
    "NOTICE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".gitignore",
    ".gitattributes",
    "requirements.txt",
    "sources/README.md",
)
QUESTION_HEADING = re.compile(r"^#### Question (\d+)$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
BANNED_GUIDE_TEXT = re.compile(
    r"/Users/|file\+|vscode-resource|vscode-cdn|"
    r"\*\*Classification:\*\*|\*\*Source:\*\*|"
    r"\*\*Question ID:\*\*|\*\*Answer status:\*\*",
    re.IGNORECASE,
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_guides(errors: list[str]) -> None:
    guides = sorted((ROOT / "docs").glob("unit-*.md"))
    actual_names = {path.name for path in guides}
    expected_names = set(EXPECTED_GUIDES)
    if actual_names != expected_names:
        fail(
            errors,
            "Unit guide set differs from the expected ten files: "
            f"missing={sorted(expected_names - actual_names)}, "
            f"extra={sorted(actual_names - expected_names)}",
        )

    for path in guides:
        text = path.read_text(encoding="utf-8")
        numbers = [int(value) for value in QUESTION_HEADING.findall(text)]
        expected_count = EXPECTED_GUIDES.get(path.name)
        if expected_count is None:
            continue
        if numbers != list(range(1, expected_count + 1)):
            fail(errors, f"{path.relative_to(ROOT)} has missing or repeated question numbers")
        if len(re.findall(r"^\*UGC NET .+\*$", text, re.MULTILINE)) != expected_count:
            fail(errors, f"{path.relative_to(ROOT)} does not have one short reference per question")
        match = BANNED_GUIDE_TEXT.search(text)
        if match:
            fail(errors, f"{path.relative_to(ROOT)} contains banned reading-flow text: {match.group(0)}")


def check_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^(?:https?|mailto):", target, re.IGNORECASE):
                continue
            # The project uses paths without link titles; reject a missing target
            # instead of guessing whether whitespace belongs to a title.
            destination = (path.parent / unquote(target)).resolve()
            try:
                public_relative = destination.relative_to(ROOT)
            except ValueError:
                public_relative = None
            if (
                public_relative is not None
                and public_relative.parts
                and public_relative.parts[0] == "sources"
                and destination.suffix.lower() == ".pdf"
            ):
                fail(
                    errors,
                    f"Public Markdown links to an ignored source PDF in {path.relative_to(ROOT)}: {raw_target}",
                )
                continue
            if not destination.exists():
                fail(
                    errors,
                    f"Broken link in {path.relative_to(ROOT)}: {raw_target}",
                )


def check_repository_contract(errors: list[str]) -> None:
    for relative in REQUIRED_PUBLIC_FILES:
        if not (ROOT / relative).is_file():
            fail(errors, f"Required public file is missing: {relative}")

    master_path = ROOT / "data/all-unit-question-index.json"
    with master_path.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if len(records) != 2102:
        fail(errors, f"Master extraction index has {len(records)} records; expected 2102")

    guide_total = sum(EXPECTED_GUIDES.values())
    if guide_total != 2081:
        fail(errors, f"Expected guide-count table totals {guide_total}; expected 2081")

    ignore_text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    if "sources/*.pdf" not in ignore_text:
        fail(errors, "Source PDFs are not protected by .gitignore")

    for path in ROOT.rglob("*.md"):
        if path.stat().st_size > 2 * 1024 * 1024:
            fail(errors, f"Markdown file exceeds the 2 MiB release target: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_guides(errors)
    check_links(errors)
    check_repository_contract(errors)
    if errors:
        print("Release checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Structural release checks passed: ten guides, continuous numbering, short references, links and public files are valid. Academic accuracy is not certified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
