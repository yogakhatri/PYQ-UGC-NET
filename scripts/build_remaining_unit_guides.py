#!/usr/bin/env python3
"""Build chapter-wise working guides for Units 2-10 from the audited question index.

This script deliberately does not guess answer keys.  It creates a complete
source-linked inventory, syllabus-aligned teaching notes, and an exam method
for every recovered question.  Question-specific answers remain visibly
flagged until independently solved or matched to a reliable key.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"

UNITS = {
    2: ("Computer System Architecture", "unit-2-computer-system-architecture.md"),
    3: ("Programming Languages and Computer Graphics", "unit-3-programming-languages-and-computer-graphics.md"),
    4: ("Database Management Systems", "unit-4-database-management-systems.md"),
    5: ("System Software and Operating System", "unit-5-system-software-and-operating-system.md"),
    6: ("Software Engineering", "unit-6-software-engineering.md"),
    7: ("Data Structures and Algorithms", "unit-7-data-structures-and-algorithms.md"),
    8: ("Theory of Computation and Compilers", "unit-8-theory-of-computation-and-compilers.md"),
    9: ("Data Communication and Computer Networks", "unit-9-data-communication-and-computer-networks.md"),
    10: ("Artificial Intelligence", "unit-10-artificial-intelligence.md"),
}

PLAYBOOK = {
    2: {
        "core": "Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.",
        "method": "Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.",
        "rules": "Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.",
        "traps": "Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.",
    },
    3: {
        "core": "Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.",
        "method": "For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.",
        "rules": "Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.",
        "traps": "Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.",
    },
    4: {
        "core": "Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.",
        "method": "For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.",
        "rules": "2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.",
        "traps": "Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.",
    },
    5: {
        "core": "Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.",
        "method": "Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.",
        "rules": "Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.",
        "traps": "Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.",
    },
    6: {
        "core": "Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.",
        "method": "Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.",
        "rules": "Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.",
        "traps": "Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.",
    },
    7: {
        "core": "Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.",
        "method": "Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.",
        "rules": "Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.",
        "traps": "Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.",
    },
    8: {
        "core": "Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.",
        "method": "For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.",
        "rules": "Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.",
        "traps": "The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.",
    },
    9: {
        "core": "Locate the question at the correct layer, draw the frame/packet path, and label addresses, headers, windows, or signal parameters.",
        "method": "Normalize bit/byte and second units. For subnetting split prefix and host bits; for error control perform modulo-2 arithmetic; for sliding windows trace sequence numbers.",
        "rules": "Transmission delay = length/rate; propagation delay = distance/speed. Hosts per IPv4 subnet are normally 2^h-2. Nyquist and Shannon answer different channel assumptions.",
        "traps": "Do not mix MAC, IP and port addresses; bandwidth with throughput; forwarding with routing; CRC polynomial division with ordinary subtraction.",
    },
    10: {
        "core": "Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.",
        "method": "For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.",
        "rules": "A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.",
        "traps": "Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.",
    },
}

STOP = {
    "and", "the", "for", "with", "from", "into", "their", "that", "this",
    "are", "of", "to", "in", "a", "an", "or", "on", "by", "as", "is",
    "its", "types", "models", "systems", "computer", "programming",
}


def words(text: str) -> set[str]:
    return {
        w for w in re.findall(r"[a-z0-9+*]+", text.lower())
        if len(w) > 2 and w not in STOP
    }


def syllabus_units() -> dict[int, list[dict[str, str]]]:
    text = (DOCS / "syllabus.md").read_text()
    result: dict[int, list[dict[str, str]]] = {}
    matches = list(re.finditer(r"^## Unit (\d+): .+$", text, re.M))
    for i, match in enumerate(matches):
        unit = int(match.group(1))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end():end]
        chapters = []
        for title, scope in re.findall(r"^- \*\*(.+?):\*\* (.+)$", body, re.M):
            chapters.append({"title": title.strip(), "scope": scope.strip()})
        result[unit] = chapters
    return result


def choose_chapter(question: str, chapters: list[dict[str, str]]) -> tuple[int, int]:
    # A few syllabus terms are much more specific than generic distractor words.
    # Route these before bag-of-words scoring so, for example, an XML option
    # containing the word "language" cannot outrank the Web Programming chapter.
    if re.search(r"\b(?:XML|HTML|DHTML|servlets?|applets?|javascript)\b", question, re.I):
        for index, chapter in enumerate(chapters):
            if chapter["title"] == "Web Programming":
                return index, 100
    qwords = words(question)
    scored = []
    for index, chapter in enumerate(chapters):
        title_words = words(chapter["title"])
        scope_words = words(chapter["scope"])
        score = 4 * len(qwords & title_words) + len(qwords & scope_words)
        scored.append((score, index))
    score, index = max(scored)
    return index, score


def display_question(text: str) -> str:
    text = re.sub(
        r"^\s*Question Number\s*:\s*\d+.*?Wrong Marks\s*:\s*-?[\d.]+",
        " ",
        text,
        flags=re.I,
    )
    # Newer NTA exports flatten the entire metadata header onto the same line as
    # the question.  Remove each field and its short value separately; consuming
    # to end-of-line here would also consume the stem and all four choices.
    text = re.sub(r"\bQuestion Number\s*:\s*\d+", " ", text, flags=re.I)
    text = re.sub(r"\bQuestion Id\s*:\s*\d+", " ", text, flags=re.I)
    text = re.sub(r"\bQuestion Type\s*:\s*[A-Za-z]+", " ", text, flags=re.I)
    text = re.sub(
        r"\b(?:Option Shuffling|Display Question Number|Is Question Mandatory|"
        r"Single Line Question Option)\s*:\s*(?:Yes|No)",
        " ",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\bOption Orientation\s*:\s*(?:Vertical|Horizontal)",
        " ",
        text,
        flags=re.I,
    )
    text = re.sub(r"\[?Question ID\s*[=:-]+\s*\d+[^\]\n)]*[\])]*", " ", text, flags=re.I)
    text = re.sub(r"\[?Question Description\s*[=:-]+[^\]\n)]*[\])]*", " ", text, flags=re.I)
    # Option-ID mappings are export metadata, not answer information or choices.
    text = re.sub(r"\b\d{9,}\s*\.\s*[1-4]\b", " ", text)
    text = re.sub(r"\b(?:Personal Exam Guide|al Exams Guide)\b", " ", text, flags=re.I)
    text = re.sub(r"^\s*\d{1,3}[.)]\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


OPTION_SCHEMES = (
    (("A", "B", "C", "D"), re.compile(r"(?<!\w)\(\s*([A-D])\s*\)\s*", re.I)),
    (("1", "2", "3", "4"), re.compile(r"(?<!\w)\(\s*([1-4])\s*\)\s*")),
    (("A", "B", "C", "D"), re.compile(r"(?<![\w.])([A-D])\.\s+", re.I)),
    (("1", "2", "3", "4"), re.compile(r"(?<![\w.])([1-4])\.\s+")),
    # OCR frequently removes the space between a numeric label and its value
    # (for example ``2.13``).  Requiring a full 1-2-3-4 sequence keeps this
    # compact fallback from treating an isolated decimal as a choice marker.
    (("1", "2", "3", "4"), re.compile(r"(?<![\w.])([1-4])\.\s*")),
)
LOOSE_OPTION_SCHEMES = (
    (
        ("A", "B", "C", "D"),
        re.compile(
            r"(?<!\w)\(\s*A\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*B\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*C\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*D\s*\)\s*(.*)$",
            re.I,
        ),
    ),
    (
        ("1", "2", "3", "4"),
        re.compile(
            r"(?<!\w)\(\s*1\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*2\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*3\s*\)\s*(.*?)"
            r"(?<!\w)\(\s*4\s*\)\s*(.*)$",
        ),
    ),
)


def split_options(text: str) -> tuple[str, tuple[str, ...], list[str]] | None:
    """Return the last complete four-option sequence found in extracted text."""
    candidates: list[tuple[int, str, tuple[str, ...], list[str]]] = []
    for labels, pattern in OPTION_SCHEMES:
        matches = list(pattern.finditer(text))
        for index in range(len(matches) - 3):
            sequence = matches[index:index + 4]
            found_labels = tuple(match.group(1).upper() for match in sequence)
            if found_labels != labels:
                continue
            start = sequence[0].start()
            if start < 5:
                continue
            values = []
            for option_index, match in enumerate(sequence):
                end = sequence[option_index + 1].start() if option_index < 3 else len(text)
                value = text[match.end():end].strip(" \t;|")
                values.append(value)
            if all(values):
                # Prefer the final complete sequence. This correctly chooses
                # numbered answer choices after an earlier A-D statement list.
                candidates.append((start, labels[0], labels, values))
    if not candidates:
        return None
    start, _, labels, values = max(candidates, key=lambda candidate: candidate[0])
    stem = text[:start].strip()
    stem = re.sub(r"\b(?:Options?|Code)\s*:\s*$", "", stem, flags=re.I).strip()
    return stem, labels, values


def split_damaged_options(text: str) -> tuple[str, tuple[str, ...], list[str]] | None:
    """Recover visibly flattened choices even when OCR left an option empty."""
    candidates = []
    for labels, pattern in LOOSE_OPTION_SCHEMES:
        match = pattern.search(text)
        if match:
            values = [value.strip(" \t;|") for value in match.groups()]
            candidates.append((match.start(), text[:match.start()].strip(), labels, values))
    if not candidates:
        return None
    _, stem, labels, values = max(candidates, key=lambda candidate: candidate[0])
    return stem, labels, values


def truncate_merged_next_question(text: str, question_number: int | str) -> str:
    """Stop a recovered block when the next numbered question was merged into it."""
    try:
        next_number = int(question_number) + 1
    except (TypeError, ValueError):
        return text
    pattern = re.compile(
        rf"\s+Question\s+(?:Number|No\.?)[\s:=-]*{next_number}\b",
        re.IGNORECASE,
    )
    match = pattern.search(text)
    return text[:match.start()] if match else text


def quoted_stem(stem: str) -> list[str]:
    """Render a stem and expose any additional embedded choice set for review."""
    embedded: list[tuple[tuple[str, ...], list[str]]] = []
    remaining = stem
    while True:
        parsed = split_options(remaining)
        if parsed is None:
            break
        remaining, labels, values = parsed
        embedded.append((labels, values))

    damaged = split_damaged_options(remaining)
    if damaged is not None:
        remaining, labels, values = damaged
        embedded.append((labels, values))

    lines = [f"> {remaining}"] if remaining else []
    for labels, values in reversed(embedded):
        lines.extend([
            ">",
            "> **Additional extracted choices — check the source page:**",
            ">",
        ])
        if labels == ("1", "2", "3", "4"):
            lines.extend(
                f"> {label}. {value or '_Missing in extracted text_'}"
                for label, value in zip(labels, values)
            )
        else:
            lines.extend(
                f"> - **{label}.** {value or '_Missing in extracted text_'}"
                for label, value in zip(labels, values)
            )
    return lines


def question_markdown(text: str, question_number: int | str) -> list[str]:
    """Format a recovered question and its choices for direct GitHub reading."""
    cleaned = display_question(truncate_merged_next_question(text, question_number))
    parsed = split_options(cleaned)
    if parsed is None:
        return quoted_stem(cleaned)

    stem, labels, options = parsed
    lines = quoted_stem(stem)
    lines.extend(["", "**Options**", ""])
    if labels == ("1", "2", "3", "4"):
        lines.extend(f"{label}. {option}" for label, option in zip(labels, options))
    else:
        lines.extend(f"- **{label}.** {option}" for label, option in zip(labels, options))
    return lines


def short_reference(item: dict) -> str:
    """Return a compact human reference without exposing paths or internal IDs."""
    name = Path(item["sourceFile"]).stem
    qnum = item["questionNumber"]
    if "2026-jan-dec-2025-session" in name:
        return f"UGC NET Dec 2025 session (Jan 2026), original Q{qnum}"
    if "2023-mar-11-shift-2-dec-2022-session" in name:
        return f"UGC NET Dec 2022 session, 11 Mar 2023 Shift 2, original Q{qnum}"
    if "2023-mar-15-shift-1-dec-2022-session" in name:
        return f"UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q{qnum}"
    match = re.search(r"ugc-net-cs-(\d{4})-(jan|june|july|aug|oct|nov|dec)", name)
    if not match:
        return f"UGC NET, original Q{qnum}"
    year, month = match.groups()
    month_name = {
        "jan": "Jan", "june": "June", "july": "July", "aug": "Aug",
        "oct": "Oct", "nov": "Nov", "dec": "Dec",
    }[month]
    paper = ""
    if "-paper-2" in name:
        paper = ", Paper II"
    elif "-paper-3" in name:
        paper = ", Paper III"
    return f"UGC NET {month_name} {year}{paper}, original Q{qnum}"


def solution_route(unit: int, chapter: dict[str, str]) -> str:
    p = PLAYBOOK[unit]
    return (
        f"For {chapter['title']} questions: {p['method']} "
        f"Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases."
    )


def solution_key(item: dict) -> str:
    return f"{item['sourceFile']}#{item['questionNumber']}"


def solution_markdown(solution: dict) -> list[str]:
    lines = [
        "**Correct answer**",
        "",
        f"**Option {solution['correctOption']}: {solution['correctText']}**",
        "",
        f"*Verification: {solution['answerStatus']}.*",
        "",
        "**Step-by-step solution**",
        "",
    ]
    lines.extend(f"{index}. {step}" for index, step in enumerate(solution["steps"], 1))
    lines.extend(["", "**Why each option is right or wrong**", ""])
    lines.extend(f"- {analysis}" for analysis in solution["optionAnalysis"])
    lines.extend(["", "**Conceptual lesson**", ""])
    for index, paragraph in enumerate(solution["conceptualLesson"]):
        if index:
            lines.append("")
        lines.append(paragraph)
    lines.extend([
        "",
        "**How to solve similar questions**",
        "",
        solution["similarQuestionMethod"],
        "",
        "**Verification references**",
        "",
    ])
    labels = ("Final-answer-key archive", "Independent concept reference")
    lines.extend(
        f"- [{labels[index] if index < len(labels) else 'Additional verification source'}]({source})"
        for index, source in enumerate(solution["verificationSources"])
    )
    return lines


def chapter_note(unit: int, chapter: dict[str, str]) -> list[str]:
    p = PLAYBOOK[unit]
    return [
        f"**What to master:** {chapter['scope']}",
        "",
        f"**Exam lens:** {p['core']}",
        "",
        f"**Reusable method:** {p['method']}",
        "",
        f"**High-yield rules:** {p['rules']}",
        "",
        f"**Common traps:** {p['traps']}",
    ]


def build() -> None:
    questions = json.loads((DATA / "all-unit-question-index.json").read_text())
    solutions = json.loads((DATA / "verified-solutions.json").read_text())
    chapters_by_unit = syllabus_units()
    coverage = {}

    for unit, (title, filename) in UNITS.items():
        items = [q for q in questions if q["suggestedUnit"] == unit]
        validated_count = sum(solution_key(item) in solutions for item in items)
        pending_count = len(items) - validated_count
        chapters = chapters_by_unit[unit]
        grouped: dict[int, list[tuple[dict, int]]] = defaultdict(list)
        chapter_scores = Counter()
        for item in items:
            solution = solutions.get(solution_key(item))
            chapter_title = solution.get("chapterTitle") if solution else None
            if chapter_title:
                chapter_index = next(
                    index for index, chapter in enumerate(chapters)
                    if chapter["title"] == chapter_title
                )
                score = 100
            else:
                chapter_index, score = choose_chapter(item["rawText"], chapters)
            grouped[chapter_index].append((item, score))
            chapter_scores["keyword-supported" if score else "fallback"] += 1

        lines = [
            f"# Unit {unit}: {title}",
            "",
            "[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)",
            "",
            "## Contents",
            "",
            "- [How to use this guide](#status-and-use)",
            "- [Unit-wide exam playbook](#unit-wide-exam-playbook)",
        ]
        lines.extend(
            f"- [{chapter_index + 1}. {chapter['title']}](#chapter-{chapter_index + 1})"
            for chapter_index, chapter in enumerate(chapters)
        )
        lines += [
            "- [Coverage and quality notes](#coverage-and-quality-notes)",
            "",
            "## Status and use",
            "",
            f"This guide contains all **{len(items)} question blocks currently recoverable and assigned to Unit {unit}** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.",
            "",
            "> [!WARNING]",
            f"> This is a working extraction inventory, not a complete solved guide. **{validated_count} answers are validated and {pending_count} remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.",
            "",
            "Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.",
            "",
            "## Unit-wide exam playbook",
            "",
            f"- **Core idea:** {PLAYBOOK[unit]['core']}",
            f"- **Method:** {PLAYBOOK[unit]['method']}",
            f"- **Rules/formulas:** {PLAYBOOK[unit]['rules']}",
            f"- **Frequent traps:** {PLAYBOOK[unit]['traps']}",
            "",
            "## Chapter-wise concepts and PYQs",
            "",
        ]

        unit_question_number = 0
        for chapter_index, chapter in enumerate(chapters):
            entries = grouped.get(chapter_index, [])
            lines.extend([
                f'<a id="chapter-{chapter_index + 1}"></a>',
                "",
                f"### {chapter_index + 1}. {chapter['title']} ({len(entries)} questions)",
                "",
                *chapter_note(unit, chapter),
                "",
            ])
            if not entries:
                lines.extend([
                    "_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._",
                    "",
                ])
                continue
            entries.sort(key=lambda pair: (pair[0]["sourceFile"], pair[0]["questionNumber"], pair[0]["sourcePage"]))
            for item, chapter_score in entries:
                unit_question_number += 1
                verified_solution = solutions.get(solution_key(item))
                lines.extend([
                    "---",
                    "",
                    f"#### Question {unit_question_number}",
                    "",
                    f"*{short_reference(item)}*",
                    "",
                    *question_markdown(item["rawText"], item["questionNumber"]),
                    "",
                ])
                if verified_solution:
                    lines.extend([*solution_markdown(verified_solution), ""])
                else:
                    lines.extend([
                        "**Chapter foundations**",
                        "",
                        f"This question belongs to the ideas covered by **{chapter['title']}**. Revise these foundations: {chapter['scope']}",
                        "",
                        "**Exam method**",
                        "",
                        "1. Identify the exact definition, formula, algorithm or system property being tested.",
                        f"2. {solution_route(unit, chapter)}",
                        "3. Check units, boundary cases and every statement before selecting an option.",
                        "",
                        "**Answer status**",
                        "",
                        "This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.",
                        "",
                    ])

        lines.extend([
            "## Coverage and quality notes",
            "",
            f"- Recovered question blocks in this unit: **{len(items)}**",
            f"- Chapter placements with direct keyword support: **{chapter_scores['keyword-supported']}**",
            f"- Chapter placements needing manual review: **{chapter_scores['fallback']}**",
            f"- Questions with validated answers in this guide: **{validated_count}**",
            "- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.",
            "- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.",
            "",
            "---",
            "",
            "[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)",
            "",
        ])
        (DOCS / filename).write_text("\n".join(lines) + "\n")
        coverage[str(unit)] = {
            "title": title,
            "file": f"docs/{filename}",
            "questions": len(items),
            "chapterKeywordSupported": chapter_scores["keyword-supported"],
            "chapterManualReview": chapter_scores["fallback"],
            "validatedAnswers": validated_count,
            "solutionStatus": "working inventory; validated answers are rendered where available",
        }

    (DATA / "units-2-10-working-coverage.json").write_text(
        json.dumps(coverage, indent=2) + "\n"
    )
    print(json.dumps(coverage, indent=2))


if __name__ == "__main__":
    build()
