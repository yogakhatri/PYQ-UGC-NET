#!/usr/bin/env python3
"""Build a broad page-level candidate set for Unit 1 manual curation."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
TEXT = ROOT / "tmp" / "pdfs" / "text"
OUTPUT = ROOT / "tmp" / "pdfs" / "unit1_candidates.json"

RPSC_SUPPLEMENTS = {
    "rpsc-computer-science-2012-paper-3.pdf",
    "rpsc-computer-science-2013-paper-2.pdf",
    "rpsc-computer-science-2012-paper-2.pdf",
    "rpsc-computer-science-2013-paper-3.pdf",
}

PATTERNS = {
    "Mathematical Logic": re.compile(
        r"\b(propositional|predicate logic|logical(?:ly)? equivalent|tautolog|contradiction|"
        r"quantifier|rules? of inference|normal form|conjunctive normal|disjunctive normal|"
        r"truth table|modus ponens|modus tollens)\b",
        re.I,
    ),
    "Sets and Relations": re.compile(
        r"\b(power set|cartesian product|binary relation|relation R|reflexive|irreflexive|"
        r"symmetric relation|antisymmetric|transitive relation|equivalence relation|"
        r"partial(?:ly)? order|poset|hasse diagram|lattice|upper bound|lower bound)\b",
        re.I,
    ),
    "Counting, Induction and Probability": re.compile(
        r"\b(pigeonhole|permutation|combination|inclusion.?exclusion|mathematical induction|"
        r"probability|bayes|randomly|at random|sample space|independent events?|conditional probability|"
        r"expected (?:number|value))\b",
        re.I,
    ),
    "Group Theory": re.compile(
        r"\b(subgroup|semigroup|semi-group|monoid|group theory|cyclic group|abelian group|"
        r"isomorph|homomorph|automorph|quotient group|normal subgroup|integral domain|"
        r"commutative ring|field with|finite field)\b",
        re.I,
    ),
    "Graph Theory": re.compile(
        r"\b(simple graph|multigraph|weighted graph|graph G|vertices|vertex|degree sequence|"
        r"euler(?:ian)?|hamilton(?:ian)?|planar graph|non-planar|chromatic|graph colou?r|"
        r"bipartite|rooted tree|prefix code|tree traversal|spanning tree|cut.?set|clique|"
        r"complete graph|connected graph|adjacency matrix|incidence matrix)\b",
        re.I,
    ),
    "Boolean Algebra": re.compile(
        r"\b(boolean (?:algebra|function|expression)|karnaugh|k.?map|minterm|maxterm|"
        r"sum of products|product of sums|de morgan)\b",
        re.I,
    ),
    "Optimization": re.compile(
        r"\b(linear programm?(?:ing)?|simplex method|revised simplex|dual simplex|integer program|transportation (?:model|problem)|"
        r"assignment (?:model|problem)|vogel|pert|cpm|critical path|resource levelling|"
        r"project scheduling|basic feasible solution|artificial variable)\b",
        re.I,
    ),
}


def source_text(pdf: Path) -> Path | None:
    rel = pdf.relative_to(ROOT).as_posix()
    ocr = TEXT / f"ocr__{rel.replace('/', '__')}.txt"
    if ocr.exists():
        return ocr
    native = TEXT / f".__{rel.replace('/', '__')}.txt"
    return native if native.exists() else None


def main() -> None:
    records = []
    for pdf in sorted(SOURCES.glob("*.pdf")):
        if pdf.name in RPSC_SUPPLEMENTS:
            continue
        if pdf.name == "ugc-net-computer-science-official-syllabus.pdf" or "final-answer-key" in pdf.name:
            continue
        text_path = source_text(pdf)
        if not text_path:
            continue
        content = text_path.read_text(encoding="utf-8", errors="replace")
        parts = re.split(r"\n===== PAGE (\d+) =====\n", content)
        for index in range(1, len(parts), 2):
            page = int(parts[index])
            body = parts[index + 1].strip()
            topics = [name for name, pattern in PATTERNS.items() if pattern.search(body)]
            if topics:
                records.append(
                    {
                        "sourceFile": pdf.relative_to(ROOT).as_posix(),
                        "page": page,
                        "candidateTopics": topics,
                        "text": body,
                    }
                )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} candidate pages from {len({r['sourceFile'] for r in records})} papers to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
