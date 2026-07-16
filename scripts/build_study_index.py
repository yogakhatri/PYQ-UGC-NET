#!/usr/bin/env python3
"""Build the canonical planning/classification layer for the learner guide.

This script does not generate or infer answers.  It separates Paper 1 from the
Computer Science subject corpus, attaches official-syllabus classification
candidates, records independent-solution coverage, and emits an explicit review
queue.  Existing guide files remain untouched until the new study layer passes
its own completeness checks.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from build_all_unit_index import COMPILED
from build_remaining_unit_guides import choose_chapter, syllabus_units


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CORPUS = DATA / "question-corpus.json"
STUDY_INDEX = DATA / "study-question-index.json"
TAXONOMY = DATA / "study-taxonomy.json"
REVIEW_QUEUE = DATA / "study-classification-review.json"
AUDIT_JSON = DATA / "study-index-audit.json"
AUDIT_MD = DATA / "study-index-audit.md"
OVERRIDES = DATA / "study-classification-overrides.json"
STUDY_HOME = ROOT / "docs" / "study" / "README.md"

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

# These are the only Paper 1 blocks present in the current combined-paper
# corpus.  Keeping the source ranges explicit prevents aptitude/data-
# interpretation text from being forced into a Computer Science unit merely
# because an option happens to contain a technical keyword.
PAPER_1_RANGES = {
    "sources/ugc-net-cs-2023-mar-11-shift-2-dec-2022-session-combined.pdf": range(1, 51),
    "sources/ugc-net-cs-2023-mar-15-shift-1-dec-2022-session-combined.pdf": range(1, 51),
}

TRUSTED_UNIT_STATUSES = {
    "high-confidence-keyword",
    "manual-reviewed-override",
    "manual-visual-recovery",
}
FALLBACK_UNIT_STATUSES = {
    "statistical-fallback",
    "manual-review-fallback",
    "text-layer-recovery-needs-classification",
}
REVIEWED_PLACEMENT_STATUSES = {
    "accepted-existing-candidate",
    "manual-reviewed-override",
}

STOPWORDS = {
    "about", "after", "also", "among", "answer", "below", "choose",
    "correct", "from", "given", "into", "list", "more", "option",
    "question", "statement", "than", "that", "their", "then", "there",
    "these", "this", "which", "with", "would",
}


def words(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9+#*.-]+", text.lower())
        if len(token) > 2 and token not in STOPWORDS
    }


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def is_paper_1(question: dict) -> bool:
    allowed = PAPER_1_RANGES.get(question["sourceFile"])
    return allowed is not None and int(question["questionNumber"]) in allowed


def question_text(question: dict) -> str:
    return " ".join(
        [question.get("context", ""), question["stem"]]
        + [option["text"] for option in question.get("options", [])]
    )


def unit_keyword_scores(text: str) -> dict[int, int]:
    return {
        unit: len(list(pattern.finditer(text)))
        for unit, pattern in COMPILED.items()
    }


def ranked_scores(scores: dict[int, int]) -> list[dict]:
    return [
        {"unit": unit, "score": score}
        for unit, score in sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        if score > 0
    ]


def choose_unit(question: dict, text: str) -> tuple[int | None, str, list[dict]]:
    current = question.get("suggestedUnit")
    current_status = question.get("classificationStatus", "")
    scores = unit_keyword_scores(text)
    ranked = ranked_scores(scores)

    if current is not None and current_status in TRUSTED_UNIT_STATUSES:
        return int(current), "accepted-existing-candidate", ranked[:3]
    if current is not None:
        return int(current), "review-existing-fallback", ranked[:3]
    if ranked and (len(ranked) == 1 or ranked[0]["score"] > ranked[1]["score"]):
        return ranked[0]["unit"], "review-new-keyword-candidate", ranked[:3]
    return None, "manual-review-required", ranked[:3]


def chapter_candidates(text: str, chapters: list[dict[str, str]]) -> list[dict]:
    qwords = words(text)
    candidates = []
    for position, chapter in enumerate(chapters, 1):
        title_score = len(qwords & words(chapter["title"]))
        scope_score = len(qwords & words(chapter["scope"]))
        score = 4 * title_score + scope_score
        candidates.append({
            "position": position,
            "title": chapter["title"],
            "score": score,
        })
    return sorted(candidates, key=lambda item: (-item["score"], item["position"]))


def atomic_topics(scope: str) -> list[str]:
    """Split the official scope into candidate concepts without inventing topics."""
    parts = []
    for semicolon_part in re.split(r";\s*", scope):
        # Commas in a short official list normally separate individual concepts.
        comma_parts = [part.strip(" .") for part in semicolon_part.split(",")]
        parts.extend(part for part in comma_parts if part)
    return parts or [scope]


def choose_atomic_topic(text: str, chapter: dict[str, str]) -> tuple[str, int]:
    qwords = words(text)
    choices = []
    for topic in atomic_topics(chapter["scope"]):
        score = len(qwords & words(topic))
        choices.append((score, topic))
    score, topic = max(choices, key=lambda item: (item[0], len(item[1])))
    return topic, score


def independent_solution_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(DATA.glob("independent-solutions*.json")):
        batch = json.loads(path.read_text(encoding="utf-8"))
        duplicate = ids & set(batch)
        if duplicate:
            raise ValueError(f"Duplicate independent solution IDs in {path}: {sorted(duplicate)}")
        ids.update(batch)
    return ids


def load_overrides(corpus_by_id: dict[str, dict]) -> dict[str, dict]:
    """Load human-reviewed placement decisions without mutating source data."""
    if not OVERRIDES.exists():
        return {}
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    if not isinstance(overrides, dict):
        raise TypeError(f"{OVERRIDES} must contain a JSON object keyed by question ID")
    unknown = set(overrides) - set(corpus_by_id)
    if unknown:
        raise KeyError(f"Study overrides have no matching questions: {sorted(unknown)}")
    for qid, override in overrides.items():
        if not isinstance(override, dict):
            raise TypeError(f"Override for {qid} must be a JSON object")
        if not str(override.get("reason", "")).strip():
            raise ValueError(f"Override for {qid} requires a non-empty reason")
        unit = override.get("unit")
        if unit is not None and (not isinstance(unit, int) or not 1 <= unit <= 10):
            raise ValueError(f"Override for {qid} has invalid unit: {unit!r}")
        secondary_units = override.get("secondaryUnits", [])
        if (
            not isinstance(secondary_units, list)
            or any(not isinstance(value, int) or not 1 <= value <= 10 for value in secondary_units)
            or len(secondary_units) != len(set(secondary_units))
            or unit in secondary_units
        ):
            raise ValueError(f"Override for {qid} has invalid secondaryUnits")
        if any(key in override for key in ("chapter", "subtopic")) and "unit" not in override:
            raise ValueError(f"Fine-grained override for {qid} must also declare its unit")
    return overrides


def build_taxonomy(chapters_by_unit: dict[int, list[dict[str, str]]]) -> dict:
    units = []
    for unit in range(1, 11):
        chapters = []
        for number, chapter in enumerate(chapters_by_unit[unit], 1):
            chapters.append({
                "id": f"u{unit:02d}-c{number:02d}-{slug(chapter['title'])}",
                "number": number,
                "title": chapter["title"],
                "officialScope": chapter["scope"],
                "atomicTopicCandidates": atomic_topics(chapter["scope"]),
                "groupingStatus": "pending-concept-cluster-review",
            })
        units.append({
            "id": f"unit-{unit:02d}",
            "number": unit,
            "title": UNIT_TITLES[unit],
            "chapters": chapters,
        })
    return {
        "version": 1,
        "source": "docs/syllabus.md",
        "status": "official-chapters-with-provisional-atomic-topics",
        "units": units,
    }


def markdown_audit(audit: dict) -> str:
    unit_rows = "\n".join(
        f"| {unit} | {audit['subjectUnitCandidates'].get(str(unit), 0)} |"
        for unit in range(1, 11)
    )
    return f"""# Study Index Audit

This audit describes the new taxonomy-first study layer.  It does not certify
that provisional unit, chapter or subtopic candidates are academically final.

## Scope

| Track | Questions |
|---|---:|
| Computer Science subject | {audit['subjectQuestions']} |
| Paper 1 aptitude | {audit['paper1Questions']} |
| Total | {audit['totalQuestions']} |

## Independent solution coverage

| Status | Questions |
|---|---:|
| Newly independently solved | {audit['independentSolutions']} |
| Pending independent solution | {audit['pendingIndependentSolutions']} |

## Provisional subject placement

| Unit | Candidate questions |
|---:|---:|
{unit_rows}
| Unresolved | {audit['unresolvedUnitCandidates']} |

## Review requirements

- Manual unit/chapter/subtopic overrides completed: **{audit['manualPlacementOverrides']}**
- Unit placement review records: **{audit['unitReviewRequired']}**
- Chapter/subtopic review records: **{audit['chapterOrTopicReviewRequired']}**
- Multi-unit questions recorded: **{audit['multiUnitQuestions']}**
- Visual-review flags: **{audit['visualReviewQuestions']}**
- Possible OCR-damage flags: **{audit['possibleOcrDamageQuestions']}**
- Descriptive questions: **{audit['descriptiveQuestions']}**

The Paper 1 records are deliberately excluded from Computer Science units.
No legacy answer key or legacy solution value is imported by this build.
"""


def markdown_study_home(audit: dict) -> str:
    return f"""# Taxonomy-first study guide

This is the new learner-guide workspace. It is being built from the
questions-only corpus and does not import legacy answers or answer-key values.

> [!CAUTION]
> Classification and solution writing are still in progress. This directory is
> not yet the final 45-day reading route.

## Current verified inventory

| Item | Count |
|---|---:|
| Computer Science questions | {audit['subjectQuestions']} |
| Paper 1 questions, kept as a separate track | {audit['paper1Questions']} |
| Independently solved questions | {audit['independentSolutions']} |
| Questions still needing an independent solution | {audit['pendingIndependentSolutions']} |
| Computer Science questions without a unit | {audit['unresolvedUnitCandidates']} |
| Manually reviewed placement overrides | {audit['manualPlacementOverrides']} |
| Remaining unit placements requiring review | {audit['unitReviewRequired']} |

## Build order

1. Review unit placement for every Computer Science question.
2. Review chapter and reusable concept-subtopic placement.
3. Assign difficulty, prerequisites, study tier and realistic minutes.
4. Write one concise theory lesson per concept group.
5. Attach detailed, independently derived solutions to that lesson.
6. Generate the 45-day route only after its prerequisite and time checks pass.
7. Remove superseded temporary/legacy material only after complete parity checks.

## Evidence and working data

- [Scope and progress audit](../../data/study-index-audit.md)
- [Official-syllabus taxonomy](../../data/study-taxonomy.json)
- [Question placement index](../../data/study-question-index.json)
- [Classification review queue](../../data/study-classification-review.json)
- [Reasoned manual overrides](../../data/study-classification-overrides.json)

The final learner files will avoid repeating the same theory under every
question: each concept group will teach the idea once, then present worked
examples and question-specific traps.
"""


def main() -> None:
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    corpus_by_id = {question["id"]: question for question in corpus}
    if len(corpus_by_id) != len(corpus):
        raise ValueError("Question corpus contains duplicate IDs")
    overrides = load_overrides(corpus_by_id)
    solution_ids = independent_solution_ids()
    corpus_ids = {question["id"] for question in corpus}
    unknown_solutions = solution_ids - corpus_ids
    if unknown_solutions:
        raise KeyError(f"Independent solutions missing from corpus: {sorted(unknown_solutions)}")

    chapters_by_unit = syllabus_units()
    taxonomy = build_taxonomy(chapters_by_unit)
    index = []
    review = []

    for question in corpus:
        qid = question["id"]
        text = question_text(question)
        solved = qid in solution_ids
        override = overrides.get(qid)
        source_risks = []
        if question.get("needsVisualReview"):
            source_risks.append("visual-review")
        if question.get("possibleOcrDamage"):
            source_risks.append("possible-ocr-damage")

        if is_paper_1(question):
            if override and any(
                key in override for key in ("unit", "chapter", "subtopic", "secondaryUnits")
            ):
                raise ValueError(f"Paper 1 question {qid} cannot receive a CS placement override")
            record = {
                "id": qid,
                "track": "paper-1",
                "scopeReason": "Known Paper 1 range in combined examination PDF",
                "primaryUnit": None,
                "unitTitle": None,
                "unitStatus": "scope-reviewed",
                "unitCandidates": [],
                "chapter": None,
                "chapterStatus": "not-applicable",
                "subtopic": None,
                "subtopicStatus": "pending-paper-1-taxonomy",
                "solutionStatus": "independent-complete" if solved else "pending-independent-solution",
                "sourceRisks": source_risks,
            }
            index.append(record)
            continue

        unit, unit_status, unit_candidates = choose_unit(question, text)
        if override and "unit" in override:
            unit = override["unit"]
            unit_status = "manual-reviewed-override"
        chapter = None
        chapter_status = "manual-review-required"
        subtopic = None
        subtopic_status = "manual-review-required"
        chapter_ranked = []
        topic_score = 0
        if unit is not None:
            chapters = chapters_by_unit[unit]
            chapter_ranked = chapter_candidates(text, chapters)
            # Preserve the existing guide's special-case routing while still
            # retaining ranked evidence and review state.
            chosen_index, special_score = choose_chapter(text, chapters)
            chosen = chapters[chosen_index]
            if chapter_ranked and chapter_ranked[0]["score"] > special_score:
                chosen = chapters[chapter_ranked[0]["position"] - 1]
            if override and "chapter" in override:
                by_title = {candidate["title"]: candidate for candidate in chapters}
                requested = override["chapter"]
                if requested not in by_title:
                    raise ValueError(
                        f"Override for {qid} requests chapter {requested!r}, "
                        f"which is not in Unit {unit}"
                    )
                chosen = by_title[requested]
            chapter = chosen["title"]
            selected_score = next(
                (candidate["score"] for candidate in chapter_ranked if candidate["title"] == chapter),
                special_score,
            )
            chapter_status = (
                "manual-reviewed-override"
                if override and "chapter" in override
                else "review-candidate" if selected_score > 0
                else "manual-review-required"
            )
            subtopic, topic_score = choose_atomic_topic(text, chosen)
            if override and "subtopic" in override:
                subtopic = str(override["subtopic"]).strip()
                if not subtopic:
                    raise ValueError(f"Override for {qid} has an empty subtopic")
                subtopic_status = "manual-reviewed-override"
            else:
                subtopic_status = "review-candidate" if topic_score > 0 else "manual-review-required"

        record = {
            "id": qid,
            "track": "computer-science",
            "scopeReason": "Computer Science subject paper",
            "primaryUnit": unit,
            "secondaryUnits": override.get("secondaryUnits", []) if override else [],
            "unitTitle": UNIT_TITLES.get(unit),
            "unitStatus": unit_status,
            "unitCandidates": unit_candidates,
            "chapter": chapter,
            "chapterStatus": chapter_status,
            "chapterCandidates": chapter_ranked[:3],
            "subtopic": subtopic,
            "subtopicStatus": subtopic_status,
            "subtopicEvidenceScore": topic_score,
            "solutionStatus": "independent-complete" if solved else "pending-independent-solution",
            "sourceRisks": source_risks,
            "difficulty": None,
            "studyTier": None,
            "estimatedMinutes": None,
            "placementReason": override.get("reason") if override else None,
        }
        index.append(record)

        reasons = []
        if unit_status not in REVIEWED_PLACEMENT_STATUSES:
            reasons.append("unit-placement")
        if chapter_status not in {"review-candidate", "manual-reviewed-override"}:
            reasons.append("chapter-placement")
        if subtopic_status not in {"review-candidate", "manual-reviewed-override"}:
            reasons.append("subtopic-placement")
        reasons.extend(source_risks)
        if reasons:
            review.append({
                "id": qid,
                "reviewReasons": reasons,
                "primaryUnitCandidate": unit,
                "unitCandidates": unit_candidates,
                "chapterCandidate": chapter,
                "chapterCandidates": chapter_ranked[:3],
                "subtopicCandidate": subtopic,
                "sourcePage": question.get("sourcePage"),
                "sourceFile": question["sourceFile"],
            })

    tracks = Counter(record["track"] for record in index)
    subject = [record for record in index if record["track"] == "computer-science"]
    unit_counts = Counter(record["primaryUnit"] for record in subject)
    audit = {
        "totalQuestions": len(index),
        "subjectQuestions": tracks["computer-science"],
        "paper1Questions": tracks["paper-1"],
        "independentSolutions": sum(
            record["solutionStatus"] == "independent-complete" for record in index
        ),
        "pendingIndependentSolutions": sum(
            record["solutionStatus"] != "independent-complete" for record in index
        ),
        "subjectUnitCandidates": {
            str(unit): unit_counts[unit] for unit in range(1, 11)
        },
        "unresolvedUnitCandidates": unit_counts[None],
        "unitReviewRequired": sum(
            record["unitStatus"] not in REVIEWED_PLACEMENT_STATUSES for record in subject
        ),
        "manualPlacementOverrides": sum(
            record["unitStatus"] == "manual-reviewed-override" for record in subject
        ),
        "chapterOrTopicReviewRequired": sum(
            record["chapterStatus"] == "manual-review-required"
            or record["subtopicStatus"] == "manual-review-required"
            for record in subject
        ),
        "visualReviewQuestions": sum("visual-review" in record["sourceRisks"] for record in subject),
        "possibleOcrDamageQuestions": sum(
            "possible-ocr-damage" in record["sourceRisks"] for record in subject
        ),
        "descriptiveQuestions": sum(
            question.get("extractionStatus") == "complete-descriptive"
            and not is_paper_1(question)
            for question in corpus
        ),
        "multiUnitQuestions": sum(bool(record["secondaryUnits"]) for record in subject),
        "reviewQueueRecords": len(review),
    }

    if audit["totalQuestions"] != 2461:
        raise ValueError(f"Unexpected corpus size: {audit['totalQuestions']}")
    if audit["subjectQuestions"] != 2361 or audit["paper1Questions"] != 100:
        raise ValueError(
            f"Unexpected scope split: subject={audit['subjectQuestions']}, "
            f"paper1={audit['paper1Questions']}"
        )

    TAXONOMY.write_text(json.dumps(taxonomy, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    STUDY_INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    REVIEW_QUEUE.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    AUDIT_JSON.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    AUDIT_MD.write_text(markdown_audit(audit), encoding="utf-8")
    STUDY_HOME.parent.mkdir(parents=True, exist_ok=True)
    STUDY_HOME.write_text(markdown_study_home(audit), encoding="utf-8")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
