#!/usr/bin/env python3
"""Extract page-delimited text from PDFs without silently dropping page errors."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--first-page", type=int, default=1)
    parser.add_argument("--last-page", type=int)
    args = parser.parse_args()

    try:
        reader = PdfReader(args.pdf)
    except Exception as exc:
        print(f"ERROR: could not open {args.pdf}: {exc}", file=sys.stderr)
        return 2

    first = max(1, args.first_page)
    last = min(len(reader.pages), args.last_page or len(reader.pages))
    if first > last:
        print(f"ERROR: invalid page range {first}-{last}", file=sys.stderr)
        return 2

    had_error = False
    for page_number in range(first, last + 1):
        print(f"\n===== PAGE {page_number} =====\n")
        try:
            print(reader.pages[page_number - 1].extract_text() or "")
        except Exception as exc:
            had_error = True
            print(f"[EXTRACTION ERROR: {type(exc).__name__}: {exc}]")

    return 1 if had_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
