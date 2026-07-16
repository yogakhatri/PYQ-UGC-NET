#!/usr/bin/env python3
"""Build a broad, traceable all-unit question index from page-delimited text.

This is an inventory/classification aid, not an answer generator.  It deliberately
keeps confidence and review state visible so later solution work never fabricates a
question, option, or key.
"""

from __future__ import annotations

import json
import math
import re
import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
TEXT = ROOT / "tmp" / "pdfs" / "text"
OUT = ROOT / "data" / "all-unit-question-index.json"
OVERRIDES = ROOT / "data" / "manual-classification-overrides.json"

EXCLUDE = {
    "rpsc-computer-science-2012-paper-3.pdf",
    "rpsc-computer-science-2013-paper-2.pdf",
    "rpsc-computer-science-2012-paper-2.pdf",
    "rpsc-computer-science-2013-paper-3.pdf",
}

# High-signal terms.  Ambiguous shared words are intentionally avoided.
UNIT_PATTERNS = {
    1: r"propositional|predicate logic|tautolog|quantifier|reflexive|antisymmetric|equivalence relation|partial order|friend relation|power set|set of all|pigeonhole|bayes|probability|permutation|combination|semigroup|monoid|group G|automorph|integral domain|hamilton|euler|planar graph|bipartite|chromatic|boolean (?:algebra|expression|function)|karnaugh|simplex|linear programming|transportation problem|PERT|critical path",
    2: r"logic gate|logic circuit|flip.flop|multiplexer|decoder|encoder|register transfer|microoperation|addressing mode|instruction cycle|control unit|cache|main memory|memory address|pipeline|DMA|interrupt|floating.point|binary representation|hexadecimal|2.s complement|hamming code|associative memory|RISC|CISC|microprogram|bus organization|ALU",
    3: r"\bC\+\+|\bC program|#include|printf|scanf|pointer|array in C|constructor|destructor|inheritance|polymorphism|encapsulation|class specified|abstract data type|exception handling|HTML|XML|servlet|applet|javascript|bezier|b.spline|clipping|scan.line|transformation matrix|computer graphics|raster|viewport|projection",
    4: r"database|relational algebra|functional dependenc|normal form|normalization|SQL|transaction|serializ|two.phase locking|deadlock schedule|ER model|E.R model|entity type|schema|DML|data definition|candidate key|primary key|data warehouse|data mining|OLAP|NoSQL|Hadoop|MapReduce|HDFS|query processing|join operation",
    5: r"operating system|process schedul|round.robin|CPU schedul|semaphore|critical section|page fault|page replacement|paging|segmentation|memory allocation|best.fit|thrashing|deadlock|file system|disk schedul|RAID|loader|linker|assembler|macro processor|Unix command|Linux|Windows scheduling|virtual machine|starvation",
    6: r"software engineering|software process|waterfall|spiral model|agile|scrum|requirement|SRS|cohesion|coupling|function point|COCOMO|software testing|white.box|black.box|cyclomatic|reliability|software quality|configuration management|version control|maintenance|design phase|top.down design|software error",
    7: r"data structure|stack operation|push\(|pop\(|queue|linked list|binary tree|binary search tree|AVL|B.tree|B\+ tree|heap|hash|sorting|searching|recursive function|recurrence|asymptotic|dynamic programming|greedy|backtracking|branch and bound|BFS|DFS|Dijkstra|Kruskal|Prim|Bellman|Floyd|maximum flow|NP.complete|time complexity|string matching|KMP|radix sort",
    8: r"finite autom|regular language|regular expression|context.free|pushdown|Turing machine|pumping lemma|Chomsky|grammar|parse tree|parser|LL\(|LR\(|LALR|syntax directed|attribute grammar|compiler|lexical|code generation|code optimization|intermediate code|symbol table|undecidable|halting problem|production rule|language is",
    9: r"computer network|data communication|OSI|TCP|UDP|IP datagram|IPv4|IPv6|subnet|routing|SNMP|Ethernet|CSMA|ALOHA|HDLC|frame relay|sliding window|data link|transport layer|network layer|gateway|topology|error detection|CRC|bandwidth|throughput|modulation|multiplexing|DNS|SMTP|FTP|wireless|GSM|mobile IP|cloud computing|IoT|firewall|cryptograph|digital signature|GHz|Mbps",
    10: r"artificial intelligence|heuristic search|A\*|minimax|alpha.beta|knowledge representation|expert system|forward chaining|backward chaining|fuzzy|genetic algorithm|neural network|perceptron|machine learning|natural language|planning|semantic network|ontology|reinforcement learning|support vector|Bayesian network|agent",
}
COMPILED = {k: re.compile(v, re.I) for k, v in UNIT_PATTERNS.items()}
STOP = {"the", "and", "for", "with", "which", "following", "given", "from", "that", "this", "are", "then", "what", "will", "option", "options", "question", "number", "correct", "answer", "choose", "below", "list", "statement", "statements", "consider"}

# Visually confirmed corrections for source defects that OCR cannot infer.
# Keep these narrow, source-addressed and traceable to the printed PDF page.
KNOWN_SOURCE_CORRECTIONS = {
    "sources/ugc-net-cs-2015-june-paper-3.pdf": {
        41: [
            {
                "questionNumber": 41,
                "sourcePage": 8,
                "rawText": "41. In XML, DOCTYPE declaration specifies to include a reference to ______ file. (1) Document Type Definition (2) Document type declaration (3) Document transfer definition (4) Document type language",
            },
            {
                "questionNumber": 42,
                "sourcePage": 8,
                "rawText": "42. Module design is used to maximize cohesion and minimize coupling. Which of the following is the key to implement this rule? (1) Inheritance (2) Polymorphism (3) Encapsulation (4) Abstraction",
            },
        ]
    },
    "sources/ugc-net-cs-2021-nov-with-answers.pdf": {
        8: [
            {
                "questionNumber": 8,
                "sourcePage": 1,
                "questionId": 2338,
                "rawText": "8. What is the transformation matrix M that transforms the square in the xy-plane defined by (1,1)^T, (-1,1)^T, (-1,-1)^T and (1,-1)^T to a parallelogram whose corresponding vertices are (2,1)^T, (0,1)^T, (-2,-1)^T and (0,-1)^T? 1. M = [[1,1,0],[0,1,0],[0,0,1]] 2. M = [[1,0,0],[1,1,0],[0,0,1]] 3. M = [[1,1,1],[0,1,0],[0,0,1]] 4. M = [[1,1,0],[1,1,0],[0,0,1]]",
            }
        ],
        9: [
            {
                "questionNumber": 9,
                "sourcePage": 1,
                "questionId": 2339,
                "rawText": "9. Suppose a Bezier curve P(t) is defined by the four control points P0=(-2,0), P1=(-2,4), P2=(2,4), and P3=(2,0). Which statements are correct? A. Bezier curve P(t) has degree 3. B. P(1/2)=(0,3). C. Bezier curve P(t) may extend outside the convex hull of its control points. 1. A and B only 2. A and C only 3. B and C only 4. A, B, and C",
            }
        ],
    },
}


@dataclass
class Page:
    number: int
    text: str


def source_text(pdf: Path) -> Path | None:
    rel = pdf.relative_to(ROOT).as_posix()
    ocr = TEXT / f"ocr__{rel.replace('/', '__')}.txt"
    native = TEXT / f".__{rel.replace('/', '__')}.txt"
    if ocr.exists():
        return ocr
    return native if native.exists() else None


def pages(path: Path) -> list[Page]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    parts = re.split(r"\n===== PAGE (\d+) =====\n", raw)
    return [Page(int(parts[i]), parts[i + 1]) for i in range(1, len(parts), 2)]


def pages_from_pdf(path: Path) -> list[Page]:
    """Read native PDF text when the optional extraction cache is absent."""
    # Keep PDF support optional for callers that only import the shared
    # classification rules.  A cached-text index build does not need pypdf.
    from pypdf import PdfReader

    reader = PdfReader(path)
    return [
        Page(number, page.extract_text() or "")
        for number, page in enumerate(reader.pages, 1)
    ]


def subject_page_allowed(source: str, page: int, qno: int) -> bool:
    if "2023-mar-15-shift-1-dec-2022-session" in source:
        return page >= 40
    if "2023-mar-11-shift-2-dec-2022-session" in source:
        return page >= 32
    if "2022-oct-with-answers" in source:
        return page <= 39
    if any(token in source for token in [
        "2018-dec-combined", "2019-dec-combined", "2019-june-combined",
        "2020-nov-combined", "2024-aug-combined", "2025-june-combined",
        "2026-jan-dec-2025-session-combined",
    ]):
        return qno >= 51
    return True


def clean(block: str) -> str:
    block = re.sub(r"https?://\S+", "", block)
    block = re.sub(r"\[Option ID[^\]]*\]|Options\s*:\s*\d+(?:\.\s*\d+)?", "", block, flags=re.I)
    block = re.sub(r"(?:\b\d{1,3}\)\s*){3,}", " ", block)
    block = re.sub(r"\s+", " ", block).strip()
    return block


def is_boilerplate(block: str) -> bool:
    low = block.lower()
    phrases = [
        "signature",
        "instructions for the candidates",
        "commencement of examination",
        "return the test question booklet",
        "rough work is to be done",
        "negative marks for incorrect answers",
        "responses to the items",
        "this paper consists of",
        "if you write your name",
        "if you write your name or put any mark",
        "name, roll number, phone number or put any mark",
        "test booklet, except for the space allotted",
    ]
    return any(p in low for p in phrases)


def is_third_party_explanation(block: str) -> bool:
    """Exclude coaching explanations/promotional pages that are not questions."""
    return bool(
        re.match(r"^\s*\d+[.)]?\s*Answer\s*:", block, re.I)
        or re.search(r"\b(?:Prepp|Collegedunia|Download\s+Prepp\s+APP)\b", block, re.I)
    )


def extract_from_page(source: str, page: Page) -> list[dict]:
    text = page.text
    nta = list(re.finditer(r"(?im)^\s*Question Number\s*:\s*(\d{1,3})\b", text))
    matches = nta or list(re.finditer(r"(?m)^\s*(\d{1,3})[.)]\s+(?=[A-Z\"'“(])", text))
    out = []
    for i, match in enumerate(matches):
        qno = int(match.group(1))
        if not subject_page_allowed(source, page.number, qno):
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = clean(text[match.start():end])
        if len(block) < 40 or is_boilerplate(block):
            continue
        out.append({"questionNumber": qno, "sourcePage": page.number, "rawText": block})
    return out


def apply_known_source_corrections(source: str, records: list[dict]) -> list[dict]:
    corrections = KNOWN_SOURCE_CORRECTIONS.get(source, {})
    if not corrections:
        return records
    corrected = []
    for record in records:
        replacements = corrections.get(record["questionNumber"])
        corrected.extend(replacements if replacements else [record])
    return corrected


def extract_id_delimited(path: Path, first_id: int, last_id: int) -> list[dict]:
    """Recover exported answer-bearing papers whose question text precedes its ID.

    These PDFs contain four option-ID markers after each question marker.  The
    next question begins after the fourth option marker, so this parser avoids
    confusing repeated Paper 1 and subject question numbers.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")
    page_marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"===== PAGE (\d+) =====", raw)]
    page_positions = [position for position, _ in page_marks]
    matches = [
        m for m in re.finditer(r"\[?Question ID\s*[=:-]+\s*(\d+)", raw, re.I)
        if first_id <= int(m.group(1)) <= last_id
    ]
    if len({int(m.group(1)) for m in matches}) != last_id - first_id + 1:
        return []

    records = []
    previous = None
    for index, marker in enumerate(matches):
        question_id = int(marker.group(1))
        qno = question_id - first_id + 1
        before_start = previous.end() if previous else 0
        before = raw[before_start:marker.start()]
        previous_options = list(re.finditer(r"\[Option ID[^\]]*\]", before, re.I))
        if previous_options:
            question_text = before[previous_options[min(3, len(previous_options) - 1)].end():]
        else:
            question_text = before
        # Remove the previous record's answer overlay.  Anchor the label so a
        # question instruction such as "Choose the correct answer" is never
        # mistaken for the answer-key boundary, and consume the answer line.
        question_text = re.sub(
            r"(?ims)^.*?^\s*Correct Answer\s*[:：][^\n]*(?:\n[^\n]*)?(?:\n|$)",
            "",
            question_text,
            count=1,
        )

        after_end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        after = raw[marker.end():after_end]
        current_options = list(re.finditer(r"\[Option ID[^\]]*\]", after, re.I))
        option_end = current_options[min(3, len(current_options) - 1)].end() if current_options else 0
        block = question_text + " " + after[:option_end]
        block = re.sub(r"===== PAGE \d+ =====|Topic\s*:[^\n]*", " ", block, flags=re.I)
        block = re.sub(r"\]?\[Question Description[^\]]*\]", " ", block, flags=re.I)
        block = re.sub(r"UGC NET 20\d{2} COMPUTER SCIENCE (?:N|AND) APPLICATIONS", " ", block, flags=re.I)
        block = re.sub(r"^(?:\s*\d+\)\s*){2,}", "", block)
        block = clean(block)
        page_index = bisect_right(page_positions, marker.start()) - 1
        page_number = page_marks[max(page_index, 0)][1]
        records.append({
            "questionNumber": qno,
            "sourcePage": page_number,
            "rawText": block,
            "questionId": question_id,
        })
        previous = marker
    return records


def extract_id_delimited_pdf(path: Path, first_id: int, last_id: int) -> list[dict]:
    """Extract an ID-delimited paper directly when cached text has bad ordering."""
    reader = PdfReader(path)
    raw = "".join(
        f"\n===== PAGE {page_number} =====\n{page.extract_text() or ''}"
        for page_number, page in enumerate(reader.pages, 1)
    )
    temporary = ROOT / "tmp" / "pdfs" / "text" / ".direct-id-extraction.txt"
    # Reuse the audited delimiter parser without leaving another public artifact.
    temporary.parent.mkdir(parents=True, exist_ok=True)
    temporary.write_text(raw, encoding="utf-8")
    try:
        return extract_id_delimited(temporary, first_id, last_id)
    finally:
        temporary.unlink(missing_ok=True)


def score(text: str) -> tuple[int | None, dict[int, int]]:
    scores = {unit: len(pattern.findall(text)) for unit, pattern in COMPILED.items()}
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return None, scores
    ordered = sorted(scores.values(), reverse=True)
    if len(ordered) > 1 and ordered[0] == ordered[1]:
        return None, scores
    return best, scores


def manual_unit(source: str, question_number: int) -> int | None:
    if not OVERRIDES.exists():
        return None
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    entry = overrides.get(f"{source}#{question_number}")
    return int(entry["unit"]) if entry else None


def tokens(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z][a-z0-9+.-]{2,}", text.lower()) if w not in STOP]


def statistical_fallback(records: list[dict]) -> None:
    """Classify keyword-missed blocks using a small transparent multinomial model."""
    unit_counts: dict[int, Counter] = defaultdict(Counter)
    totals = Counter()
    documents = Counter()
    vocab = set()
    for record in records:
        unit = record["suggestedUnit"]
        if unit is None:
            continue
        words = tokens(record["rawText"])
        unit_counts[unit].update(words)
        totals[unit] += len(words)
        documents[unit] += 1
        vocab.update(words)
    size = max(len(vocab), 1)
    total_docs = sum(documents.values())
    for record in records:
        if record["suggestedUnit"] is not None:
            continue
        words = tokens(record["rawText"])
        log_scores = {}
        for unit in range(1, 11):
            value = math.log((documents[unit] + 1) / (total_docs + 10))
            denom = totals[unit] + size
            for word in words:
                value += math.log((unit_counts[unit][word] + 1) / denom)
            log_scores[unit] = value
        ranked = sorted(log_scores, key=log_scores.get, reverse=True)
        record["suggestedUnit"] = ranked[0]
        record["classificationStatus"] = "statistical-fallback" if log_scores[ranked[0]] - log_scores[ranked[1]] >= 2 else "manual-review-fallback"
        record["statisticalMargin"] = round(log_scores[ranked[0]] - log_scores[ranked[1]], 3)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=OUT,
        help="Candidate index path; defaults to the canonical index",
    )
    args = parser.parse_args()
    all_records = []
    source_papers = {
        pdf.relative_to(ROOT).as_posix()
        for pdf in SOURCES.glob("*.pdf")
        if pdf.name not in EXCLUDE
        and pdf.name != "ugc-net-computer-science-official-syllabus.pdf"
        and "final-answer-key" not in pdf.name
    }
    for pdf in sorted(SOURCES.glob("*.pdf")):
        if pdf.name in EXCLUDE or pdf.name == "ugc-net-computer-science-official-syllabus.pdf" or "final-answer-key" in pdf.name:
            continue
        source = pdf.relative_to(ROOT).as_posix()
        if "2021-nov-with-answers" in source:
            candidates = extract_id_delimited_pdf(pdf, 2331, 2430)
        elif "2022-oct-with-answers" in source:
            text_path = source_text(pdf)
            candidates = (
                extract_id_delimited(text_path, 316, 415)
                if text_path
                else extract_id_delimited_pdf(pdf, 316, 415)
            )
        else:
            text_path = source_text(pdf)
            candidates = []
            source_pages = pages(text_path) if text_path else pages_from_pdf(pdf)
            for page in source_pages:
                candidates.extend(extract_from_page(source, page))
        if "2023-june-paper-2" in source:
            candidates = [item for item in candidates if not is_third_party_explanation(item["rawText"])]
        candidates = apply_known_source_corrections(source, candidates)

        # Repeated browser headers and page breaks can duplicate a question. Keep the
        # longest recovered version for a given displayed number and page neighbourhood.
        best: dict[int, dict] = {}
        for item in candidates:
            key = item["questionNumber"]
            if key not in best or len(item["rawText"]) > len(best[key]["rawText"]):
                best[key] = item
        for item in best.values():
            unit, scores = score(item["rawText"])
            reviewed_unit = manual_unit(source, item["questionNumber"])
            if reviewed_unit is not None:
                unit = reviewed_unit
            all_records.append(
                {
                    "exam": "UGC NET Computer Science and Applications",
                    "sourceFile": source,
                    **item,
                    "suggestedUnit": unit,
                    "classificationScores": scores,
                    "classificationStatus": (
                        "manual-reviewed-override" if reviewed_unit is not None
                        else "high-confidence-keyword" if unit else "manual-review"
                    ),
                }
            )

    statistical_fallback(all_records)
    recovered_sources = {record["sourceFile"] for record in all_records}
    # A missing text-extraction cache previously allowed this command to replace
    # the 2,103-record index with the 100 records read directly from one PDF.
    # Refuse a partial rebuild instead of silently destroying the canonical data.
    missing_sources = sorted(source_papers - recovered_sources)
    if missing_sources:
        preview = ", ".join(missing_sources[:3])
        remainder = len(missing_sources) - min(len(missing_sources), 3)
        suffix = f" (and {remainder} more)" if remainder else ""
        raise RuntimeError(
            "Refusing to overwrite the question index because extracted text is "
            f"missing for {len(missing_sources)} source papers: {preview}{suffix}. "
            "Recreate tmp/pdfs/text first."
        )
    if len(all_records) < 2000:
        raise RuntimeError(
            f"Refusing to overwrite the question index with only {len(all_records)} records."
        )
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(all_records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = Counter(r["suggestedUnit"] for r in all_records)
    print(f"Wrote {len(all_records)} recovered question blocks from {len(set(r['sourceFile'] for r in all_records))} papers")
    print("Unit counts:", dict(sorted(counts.items(), key=lambda x: (x[0] is None, x[0] or 0))))


if __name__ == "__main__":
    main()
