#!/usr/bin/env python3
"""Generate page-delimited OCR caches for PDFs without usable native text."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
TEXT = ROOT / "tmp" / "pdfs" / "text"
OCR = ROOT / "scripts" / "ocr_pdf.swift"


def cache_path(pdf: Path) -> Path:
    relative = pdf.relative_to(ROOT).as_posix()
    return TEXT / f"ocr__{relative.replace('/', '__')}.txt"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdfs", nargs="*", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    pdfs = args.pdfs or sorted(SOURCES.glob("*.pdf"))
    TEXT.mkdir(parents=True, exist_ok=True)
    for supplied in pdfs:
        pdf = supplied if supplied.is_absolute() else ROOT / supplied
        output = cache_path(pdf)
        if output.exists() and not args.force:
            print(f"Keeping existing {output.relative_to(ROOT)}")
            continue
        print(f"OCR {pdf.relative_to(ROOT)}")
        result = subprocess.run(
            ["swift", str(OCR), str(pdf)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output.write_text(result.stdout, encoding="utf-8")
        print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
