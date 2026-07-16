#!/usr/bin/env python3
"""Validate scope, coverage and referential integrity of the study index."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> None:
    corpus = load("question-corpus.json")
    index = load("study-question-index.json")
    taxonomy = load("study-taxonomy.json")
    review = load("study-classification-review.json")
    audit = load("study-index-audit.json")
    overrides = load("study-classification-overrides.json")

    corpus_ids = [record["id"] for record in corpus]
    index_ids = [record["id"] for record in index]
    assert len(corpus_ids) == len(set(corpus_ids)) == 2461
    assert len(index_ids) == len(set(index_ids)) == 2461
    assert set(corpus_ids) == set(index_ids)

    tracks = Counter(record["track"] for record in index)
    assert tracks == {"computer-science": 2361, "paper-1": 100}

    paper1 = [record for record in index if record["track"] == "paper-1"]
    assert all(record["primaryUnit"] is None for record in paper1)
    assert all(record["chapter"] is None for record in paper1)

    subject = [record for record in index if record["track"] == "computer-science"]
    assert all(1 <= record["primaryUnit"] <= 10 for record in subject)
    assert all(
        len(record["secondaryUnits"]) == len(set(record["secondaryUnits"]))
        and record["primaryUnit"] not in record["secondaryUnits"]
        and all(1 <= unit <= 10 for unit in record["secondaryUnits"])
        for record in subject
    )
    assert audit["unresolvedUnitCandidates"] == 0
    assert len(taxonomy["units"]) == 10
    assert sum(len(unit["chapters"]) for unit in taxonomy["units"]) == 90
    chapters_by_unit = {
        unit["number"]: {chapter["title"] for chapter in unit["chapters"]}
        for unit in taxonomy["units"]
    }
    assert all(
        record["chapter"] in chapters_by_unit[record["primaryUnit"]]
        for record in subject
    )

    by_id = {record["id"]: record for record in index}
    assert set(overrides) <= set(by_id)
    for qid, override in overrides.items():
        record = by_id[qid]
        assert record["track"] == "computer-science"
        if "unit" in override:
            assert record["primaryUnit"] == override["unit"]
            assert record["unitStatus"] == "manual-reviewed-override"
        if "chapter" in override:
            assert record["chapter"] == override["chapter"]
            assert record["chapterStatus"] == "manual-reviewed-override"
        if "subtopic" in override:
            assert record["subtopic"] == override["subtopic"]
            assert record["subtopicStatus"] == "manual-reviewed-override"
        assert record["secondaryUnits"] == override.get("secondaryUnits", [])

    solved = sum(record["solutionStatus"] == "independent-complete" for record in index)
    assert solved == audit["independentSolutions"] == 300
    assert audit["pendingIndependentSolutions"] == 2161
    assert audit["subjectQuestions"] + audit["paper1Questions"] == 2461

    review_ids = [record["id"] for record in review]
    assert len(review_ids) == len(set(review_ids))
    assert set(review_ids) <= set(corpus_ids)

    print(
        "Study index checks passed: "
        f"{tracks['computer-science']} subject, {tracks['paper-1']} Paper 1, "
        f"{solved} independently solved, {len(review)} review records."
    )


if __name__ == "__main__":
    main()
