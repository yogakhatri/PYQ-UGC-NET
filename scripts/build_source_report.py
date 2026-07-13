#!/usr/bin/env python3
"""Build the reproducible source-PDF inventory report."""

from __future__ import annotations

import hashlib
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
OUTPUT = ROOT / "data" / "source-files-report.md"

RPSC_FILES = {
    "rpsc-computer-science-2012-paper-3.pdf": "RPSC Assistant Professor/Librarian/PTI 2012, Computer Science Application Paper III (supplemental; not SET)",
    "rpsc-computer-science-2012-paper-2.pdf": "RPSC Assistant Professor/Librarian/PTI 2012, Computer Science Application Paper II (supplemental; not SET)",
    "rpsc-computer-science-2013-paper-2.pdf": "RPSC Assistant Professor/Librarian/PTI 2013, Computer Science Application Paper II (supplemental; not SET)",
    "rpsc-computer-science-2013-paper-3.pdf": "RPSC Assistant Professor/Librarian/PTI 2013, Computer Science Application Paper III (supplemental; not SET)",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def ocr_exists(path: Path) -> bool:
    key = rel(path).replace("/", "__")
    return (ROOT / "tmp" / "pdfs" / "text" / f"ocr__{key}.txt").exists()


def main() -> None:
    pdfs = sorted(SOURCES.glob("*.pdf"))
    rows = []
    hash_groups: dict[str, list[str]] = defaultdict(list)
    total_pages = 0
    failures = []

    for path in pdfs:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hash_groups[digest].append(rel(path))
        try:
            reader = PdfReader(path)
            pages = len(reader.pages)
            text_chars = sum(len(page.extract_text() or "") for page in reader.pages)
            parse = "Openable"
        except Exception as exc:  # pragma: no cover - records damaged inputs
            pages = 0
            text_chars = 0
            parse = f"Failed: {type(exc).__name__}"
            failures.append((rel(path), str(exc)))

        total_pages += pages
        if path.name == "ugc-net-computer-science-official-syllabus.pdf":
            kind = "Official syllabus"
        elif "final-answer-key" in path.name:
            kind = "Official answer key"
        elif path.name in RPSC_FILES:
            kind = "RPSC supplemental paper"
        else:
            kind = "UGC NET question paper"

        if ocr_exists(path):
            extraction = "Native text + OCR"
        elif "-2015-" in path.name:
            extraction = "OCR required (embedded character-map issue)"
        elif text_chars >= max(1000, pages * 100):
            extraction = "Native text"
        else:
            extraction = "OCR required"

        note = RPSC_FILES.get(path.name, "")
        if "unofficial" in path.name:
            note = "Unofficial question-paper copy; answers must not be treated as official."
        if path.name == "ugc-net-cs-2023-june-paper-2.pdf":
            note = "Third-party question/answer copy; coaching explanations and promotional blocks are excluded from the public index."
        rows.append((rel(path), kind, pages, text_chars, extraction, parse, note, digest[:12]))

    duplicates = [files for files in hash_groups.values() if len(files) > 1]
    ugc_papers = [r for r in rows if r[1] == "UGC NET question paper"]
    rpsc_papers = [r for r in rows if r[1] == "RPSC supplemental paper"]
    answer_keys = [r for r in rows if r[1] == "Official answer key"]

    lines = [
        "# Source Files Report",
        "",
        "Generated from the current workspace. SHA-256 prefixes are included for traceability; duplicate detection uses the complete hash.",
        "",
        "## Summary",
        "",
        f"- PDF files: **{len(rows)}**",
        f"- Total PDF pages: **{total_pages}**",
        f"- UGC NET question-paper files: **{len(ugc_papers)}**",
        f"- Rajasthan SET question-paper files: **0 verifiable files**",
        f"- RPSC Assistant Professor/Librarian/PTI supplemental papers: **{len(rpsc_papers)}**",
        f"- Standalone official answer-key files: **{len(answer_keys)}**",
        f"- Exact duplicate groups: **{len(duplicates)}**",
        f"- Files that failed to open: **{len(failures)}**",
        "",
        "## Scope Finding",
        "",
        (f"{len(rpsc_papers)} RPSC recruitment scans are retained only as excluded supplemental inputs; they are not UGC NET or Rajasthan SET papers." if rpsc_papers else "No RPSC recruitment scans are retained in the current UGC NET source collection."),
        "",
        "No locally available PDF can presently be verified as a Rajasthan SET Computer Science paper. This is a source gap, not an extraction failure.",
        "",
        "## Inventory",
        "",
        "| Source file | Type | Pages | Native text chars | Extraction | Parse | SHA-256 prefix | Notes |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for filename, kind, pages, chars, extraction, parse, note, digest in rows:
        lines.append(
            f"| `{filename}` | {kind} | {pages} | {chars} | {extraction} | {parse} | `{digest}` | {note} |"
        )

    lines.extend(["", "## Exact Duplicates", ""])
    if duplicates:
        for group_number, files in enumerate(duplicates, 1):
            lines.append(f"- Group {group_number}: " + ", ".join(f"`{f}`" for f in files))
    else:
        lines.append("No byte-identical PDFs were found.")

    lines.extend(["", "## Parse and Extraction Issues", ""])
    if failures:
        for filename, error in failures:
            lines.append(f"- `{filename}`: {error}")
    else:
        ocr_only = sum(row[4] == "OCR required" for row in rows)
        lines.append(f"All PDFs can be opened. {ocr_only} files have no usable native text layer and require OCR; the 2015 papers also require OCR because their embedded character maps extract as glyph codes.")

    lines.extend(
        [
            "",
            "## Answer-Key Coverage",
            "",
            "Standalone official keys are locally available only for June 2024 and the December 2024 session held in January 2025. Some other question-paper PDFs include answers inline; those are validated question by question. Missing keys are recorded as `officialAnswer: null` rather than inferred.",
            "",
            "## Reproduction",
            "",
            "- Native extraction: `scripts/extract_pdf_text.py`",
            "- Image-only extraction: `scripts/ocr_pdf.swift` (macOS Vision)",
            "- Inventory generation: `scripts/build_source_report.py`",
            "",
        ]
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
