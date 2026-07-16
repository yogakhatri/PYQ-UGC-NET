#!/usr/bin/env python3
"""Render independently derived solutions as one learner-focused Markdown file per question."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "data" / "question-corpus.json"
SOLUTION_GLOB = "independent-solutions*.json"
OUTPUT = ROOT / "docs" / "solutions"


def slug(source_file: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", Path(source_file).stem.lower()).strip("-")


def main() -> None:
    questions = {row["id"]: row for row in json.loads(CORPUS.read_text(encoding="utf-8"))}
    solutions = {}
    for path in sorted((ROOT / "data").glob(SOLUTION_GLOB)):
        batch = json.loads(path.read_text(encoding="utf-8"))
        duplicates = sorted(set(solutions) & set(batch))
        if duplicates:
            raise ValueError(f"Duplicate independent solutions in {path}: {duplicates}")
        solutions.update(batch)
    unknown = sorted(set(solutions) - set(questions))
    if unknown:
        raise KeyError(f"Solutions without question records: {unknown}")

    index = ["# Independent solutions", "", "These solutions were derived from the questions-only corpus without importing repository answer keys.", ""]
    rendered = 0
    ordered_solutions = sorted(
        solutions.items(),
        key=lambda item: (questions[item[0]]["sourceFile"], questions[item[0]]["questionNumber"]),
    )
    for question_id, solution in ordered_solutions:
        question = questions[question_id]
        answer_label = solution.get("answerLabel")
        chosen = next(
            (option for option in question["options"] if option["label"] == answer_label),
            None,
        )
        if answer_label is not None and chosen is None:
            raise ValueError(f"Invalid answer label for {question_id}: {answer_label}")
        answer_display = (
            f"{answer_label}. {chosen['text']}" if chosen is not None
            else solution["answerText"]
        )

        directory = OUTPUT / slug(question["sourceFile"])
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"q{question['questionNumber']:03d}.md"
        lines = [
            f"# Question {question['questionNumber']}", "",
            solution.get("questionText", question["stem"]), "",
        ]
        normalized_options = solution.get("optionTexts", {})
        lines.extend(
            f"- **{option['label']}.** {normalized_options.get(option['label'], option['text'])}"
            for option in question["options"]
        )
        lines.extend([
            "", "## Answer", "",
            f"**{answer_display}**", "",
            "## Detailed solution", "", solution["explanation"].strip(), "",
            "## Why the other options do not work", "", solution["whyOthersFail"].strip(), "",
            "## Key idea to remember", "", solution["keyIdea"].strip(), "",
        ])
        if question.get("visualAsset"):
            lines.extend(["## Source visual", "", f"![Source question]({question['visualAsset']})", ""])
        sources = solution.get("sources", [])
        if sources:
            lines.extend(["## References", ""])
            lines.extend(f"- [{item['title']}]({item['url']})" for item in sources)
            lines.append("")
        path.write_text("\n".join(lines), encoding="utf-8")
        rel = path.relative_to(OUTPUT).as_posix()
        index.append(f"- [{question_id}]({rel})")
        rendered += 1

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Rendered {rendered} independent solution files")


if __name__ == "__main__":
    main()
