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
    "unit-2-computer-system-architecture.md": 391,
    "unit-3-programming-languages-and-computer-graphics.md": 184,
    "unit-4-database-management-systems.md": 176,
    "unit-5-system-software-and-operating-system.md": 184,
    "unit-6-software-engineering.md": 180,
    "unit-7-data-structures-and-algorithms.md": 251,
    "unit-8-theory-of-computation-and-compilers.md": 220,
    "unit-9-data-communication-and-computer-networks.md": 256,
    "unit-10-artificial-intelligence.md": 97,
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
    "data/official-answer-keys.json",
    "data/verified-solutions.json",
    "data/manual-classification-overrides.json",
)
QUESTION_HEADING = re.compile(r"^#### Question (\d+)$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
BANNED_GUIDE_TEXT = re.compile(
    r"/Users/|file\+|vscode-resource|vscode-cdn|"
    r"\*\*Classification:\*\*|\*\*Source:\*\*|"
    r"\*\*Question ID:\*\*|\*\*Answer status:\*\*",
    re.IGNORECASE,
)
FLATTENED_OPTIONS = re.compile(
    r"(?:\(\s*A\s*\).*\(\s*B\s*\).*\(\s*C\s*\).*\(\s*D\s*\)|"
    r"\(\s*1\s*\).*\(\s*2\s*\).*\(\s*3\s*\).*\(\s*4\s*\))",
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
        if path.name != "unit-1-discrete-structures-and-optimization.md":
            blocks = re.split(r"(?=^#### Question \d+$)", text, flags=re.MULTILINE)[1:]
            for question_number, block in enumerate(blocks, 1):
                has_flat_line = any(
                    line.startswith("> ")
                    and not line.startswith("> - ")
                    and not re.match(r"^> [1-4]\. ", line)
                    and FLATTENED_OPTIONS.search(line)
                    for line in block.splitlines()
                )
                has_formatted_choices = (
                    "**Options**" in block
                    or "**Additional extracted choices — check the source page:**" in block
                )
                if has_flat_line and not has_formatted_choices:
                    fail(
                        errors,
                        f"{path.relative_to(ROOT)} question {question_number} has four options flattened into the question line",
                    )


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
    if len(records) != 2103:
        fail(errors, f"Master extraction index has {len(records)} records; expected 2103")

    record_keys = {
        f"{record['sourceFile']}#{record['questionNumber']}" for record in records
    }
    solution_path = ROOT / "data/verified-solutions.json"
    with solution_path.open(encoding="utf-8") as handle:
        solutions = json.load(handle)
    for key, solution in solutions.items():
        if key not in record_keys:
            fail(errors, f"Verified solution has no matching master question: {key}")
        required = {
            "correctOption", "correctText", "answerStatus", "steps",
            "optionAnalysis", "conceptualLesson", "similarQuestionMethod",
            "verificationSources",
        }
        missing = required - solution.keys()
        if missing:
            fail(errors, f"Verified solution {key} is missing fields: {sorted(missing)}")
        if len(solution.get("steps", [])) < 3:
            fail(errors, f"Verified solution {key} needs at least three reasoning steps")
        if len(solution.get("optionAnalysis", [])) != 4:
            fail(errors, f"Verified solution {key} must analyse exactly four options")
        if len(solution.get("conceptualLesson", [])) < 2:
            fail(errors, f"Verified solution {key} needs a multi-part conceptual lesson")
        if len(solution.get("verificationSources", [])) < 2:
            fail(errors, f"Verified solution {key} needs answer-key and concept references")

    official_keys = json.loads((ROOT / "data/official-answer-keys.json").read_text())
    for session_key, session in official_keys.items():
        matching_records = {
            str(record["questionNumber"]): record
            for record in records if record["sourceFile"] == session["sourceFile"]
        }
        for question_number, entry in session["entries"].items():
            record = matching_records.get(question_number)
            if record is None:
                fail(errors, f"Official key {session_key} Q{question_number} has no master record")
            elif record.get("questionId") != entry["questionId"]:
                fail(errors, f"Official key {session_key} Q{question_number} has a Question ID mismatch")
            if entry["keyStatus"] in {"single-option", "multiple-options-accepted"} and not entry["correctOptions"]:
                fail(errors, f"Official key {session_key} Q{question_number} has no mapped option number")

    guide_total = sum(EXPECTED_GUIDES.values())
    if guide_total != 2082:
        fail(errors, f"Expected guide-count table totals {guide_total}; expected 2082")

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
