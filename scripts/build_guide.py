#!/usr/bin/env python3
"""Build the minimal 45-day guide and Testbook-style Markdown learning cards."""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
UNITS = DOCS / "units"

UNIT_TITLES = {
    1: "Discrete Structures and Optimization",
    2: "Computer System Architecture",
    3: "Programming Languages and Computer Graphics",
    4: "Database Management Systems",
    5: "System Software and Operating System",
    6: "Software Engineering",
    7: "Data Structures and Algorithms",
    8: "Theory of Computation and Compilers",
    9: "Data Communication and Computer Networks",
    10: "Artificial Intelligence",
}

DAY_RANGES = {
    1: "Days 1–3",
    2: "Days 4–10",
    3: "Days 11–13",
    4: "Days 14–16",
    5: "Days 17–19",
    6: "Days 20–22",
    7: "Days 23–27",
    8: "Days 28–31",
    9: "Days 32–36",
    10: "Days 37–38",
}


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def unit_directory(unit: int) -> Path:
    return UNITS / f"unit-{unit:02d}-{slug(UNIT_TITLES[unit])}"


def source_label(question: dict) -> str:
    stem = Path(question["sourceFile"]).stem
    label = stem.replace("ugc-net-cs-", "").replace("-combined", "")
    return "UGC NET CS · " + label.replace("-", " ").title()


def key_points(value: str) -> list[str]:
    points = [part.strip() for part in re.split(r"(?<=[.!?])\s+", value.strip()) if part.strip()]
    return points or [value.strip()]


def answer_display(question: dict, solution: dict) -> str:
    label = solution.get("answerLabel")
    if label is None:
        return solution["answerText"]
    normalized_options = solution.get("optionTexts", {})
    chosen = next((option for option in question.get("options", []) if option["label"] == label), None)
    if chosen is None:
        raise ValueError(f"Invalid answer label for {question['id']}: {label}")
    return f"{label}. {normalized_options.get(label, chosen['text'])}"


def card_path(question: dict, placement: dict) -> Path:
    source = slug(Path(question["sourceFile"]).stem)
    return unit_directory(placement["unit"]) / f"{source}-q{question['questionNumber']:03d}.md"


def render_card(question: dict, placement: dict, solution: dict) -> str:
    normalized_options = solution.get("optionTexts", {})
    lines = [
        f"# Question {question['questionNumber']}",
        "",
        f"*{source_label(question)} · {placement['chapter']} · {placement['subtopic']}*",
        "",
        solution.get("questionText", question["stem"]).strip(),
        "",
    ]
    lines.extend(
        f"- **{option['label']}.** {normalized_options.get(option['label'], option['text'])}"
        for option in question.get("options", [])
    )
    review_heading = (
        "## Why the other options are incorrect"
        if question.get("options")
        else "## Common mistakes to avoid"
    )
    lines.extend([
        "",
        "> [!TIP]",
        f"> **Correct answer: {answer_display(question, solution)}**",
        "",
        "## Solution",
        "",
        solution["explanation"].strip(),
        "",
        "## Key Points",
        "",
    ])
    lines.extend(f"- {point}" for point in key_points(solution["keyIdea"]))
    lines.extend([
        "",
        review_heading,
        "",
        solution["whyOthersFail"].strip(),
        "",
    ])
    additional = solution.get("additionalInformation", "").strip()
    if additional:
        lines.extend(["## Additional Information", "", additional, ""])
    if question.get("visualAsset"):
        asset = Path(question["visualAsset"].lstrip("/"))
        if asset.parts and asset.parts[0] == "docs":
            asset = Path(*asset.parts[1:])
        lines.extend(["## Question Figure", "", f"![Question figure](../../{asset.as_posix()})", ""])
    sources = solution.get("sources", [])
    if sources:
        lines.extend(["## References", ""])
        lines.extend(f"- [{item['title']}]({item['url']})" for item in sources)
        lines.append("")
    return "\n".join(lines)


def render_unit_index(
    unit: int,
    total: int,
    grouped: dict[str, dict[str, list[tuple[dict, Path]]]],
) -> str:
    ready = sum(len(items) for topics in grouped.values() for items in topics.values())
    lines = [
        f"# Unit {unit}: {UNIT_TITLES[unit]}",
        "",
        f"**{total} questions in the corpus · {ready} complete learning cards**",
        "",
        "Attempt each question first. Read the full card whenever your answer is wrong or uncertain.",
        "",
    ]
    for chapter in sorted(grouped):
        lines.extend([f"## {chapter}", ""])
        for topic in sorted(grouped[chapter]):
            lines.extend([f"### {topic}", ""])
            for question, path in sorted(
                grouped[chapter][topic],
                key=lambda item: (item[0]["sourceFile"], item[0]["questionNumber"]),
            ):
                label = f"{source_label(question)} · Question {question['questionNumber']}"
                lines.append(f"- [{label}]({path.name})")
            lines.append("")
    return "\n".join(lines)


def render_home(total_counts: Counter, ready_counts: Counter, solved: int, total: int) -> str:
    lines = [
        "# UGC NET Computer Science: 45-Day Question Guide",
        "",
        "Start with the [45-day study plan](45-day-plan.md). Questions are grouped by unit, chapter and subtopic. Each completed card gives the correct answer, a clear solution, key points and distractor analysis.",
        "",
        f"**Current complete cards: {solved} of {total}.** Remaining cards are not shown until their answers and explanations are independently completed.",
        "",
        "## Units",
        "",
        "| Unit | Guide | Questions | Complete cards |",
        "|---:|---|---:|---:|",
    ]
    for unit in range(1, 11):
        rel = unit_directory(unit).relative_to(DOCS).as_posix() + "/README.md"
        lines.append(
            f"| {unit} | [{UNIT_TITLES[unit]}]({rel}) | {total_counts[unit]} | {ready_counts[unit]} |"
        )
    lines.extend([
        "",
        "## How to use a learning card",
        "",
        "1. Attempt the question without viewing the answer.",
        "2. If correct and confident, read only **Key Points**.",
        "3. If wrong or uncertain, read the complete **Solution** and distractor analysis.",
        "4. Reattempt wrong questions after 1, 3 and 7 days.",
        "",
    ])
    return "\n".join(lines)


def render_plan(total_counts: Counter) -> str:
    total_questions = sum(total_counts.values()) + 100
    lines = [
        "# 45-Day Study Plan",
        "",
        f"This route covers the complete {total_questions:,}-question bank by attempting every question and reading the full explanation only for wrong or uncertain answers. Plan for approximately **5–6 hours per day**.",
        "",
        "## Coverage schedule",
        "",
        "| Days | Unit | Questions |",
        "|---|---|---:|",
    ]
    for unit in range(1, 11):
        rel = unit_directory(unit).relative_to(DOCS).as_posix() + "/README.md"
        lines.append(
            f"| {DAY_RANGES[unit]} | [Unit {unit}: {UNIT_TITLES[unit]}]({rel}) | {total_counts[unit]} |"
        )
    lines.extend([
        "| Days 39–40 | Paper 1 | 100 |",
        "| Day 41 | Mixed revision: Units 1–5 | — |",
        "| Day 42 | Mixed revision: Units 6–10 and Paper 1 | — |",
        "| Day 43 | Reattempt every wrong or uncertain question | — |",
        "| Day 44 | Full mock and weak-subtopic repair | — |",
        "| Day 45 | Formulas, key points and final recall | — |",
        "",
        "## Daily routine",
        "",
        "1. **20 minutes:** recall yesterday’s key points.",
        "2. **90 minutes:** attempt the first question block.",
        "3. **60–90 minutes:** study the cards for wrong or uncertain answers.",
        "4. **90 minutes:** attempt the second question block.",
        "5. **60–90 minutes:** review mistakes and record only the rule you missed.",
        "6. **20 minutes:** reattempt questions due after 1, 3 or 7 days.",
        "",
        "Aim for **55–70 questions daily** during Days 1–40. Do not read every explanation from beginning to end: deep review is reserved for mistakes and uncertainty.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    questions = {row["id"]: row for row in load_json("question-corpus.json")}
    classification_data = load_json("question-classification.json")
    placements = {row["id"]: row for row in classification_data["questions"]}
    solutions = load_json("solutions.json")

    if set(questions) != set(placements):
        raise ValueError("Question and classification IDs do not match")
    if not set(solutions) <= set(questions):
        raise ValueError("A solution has no matching question")

    if UNITS.exists():
        shutil.rmtree(UNITS)
    UNITS.mkdir(parents=True)

    total_counts = Counter(
        placement["unit"]
        for placement in placements.values()
        if placement["track"] == "computer-science"
    )
    ready_counts = Counter()
    grouped = {
        unit: defaultdict(lambda: defaultdict(list))
        for unit in range(1, 11)
    }

    for question_id, solution in sorted(solutions.items()):
        question = questions[question_id]
        placement = placements[question_id]
        if placement["track"] != "computer-science" or placement["unit"] not in UNIT_TITLES:
            raise ValueError(f"Solved question has no CS unit: {question_id}")
        path = card_path(question, placement)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_card(question, placement, solution), encoding="utf-8")
        chapter = placement["chapter"] or "Other"
        topic = placement["subtopic"] or "General"
        grouped[placement["unit"]][chapter][topic].append((question, path))
        ready_counts[placement["unit"]] += 1

    for unit in range(1, 11):
        directory = unit_directory(unit)
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "README.md").write_text(
            render_unit_index(unit, total_counts[unit], grouped[unit]),
            encoding="utf-8",
        )

    paper1_count = sum(p["track"] == "paper-1" for p in placements.values())
    total = len(questions)
    (DOCS / "README.md").write_text(
        render_home(total_counts, ready_counts, len(solutions), total),
        encoding="utf-8",
    )
    (DOCS / "45-day-plan.md").write_text(render_plan(total_counts), encoding="utf-8")
    print(
        f"Built {len(solutions)} cards across 10 units from {sum(total_counts.values())} "
        f"CS and {paper1_count} Paper 1 questions"
    )


if __name__ == "__main__":
    main()
