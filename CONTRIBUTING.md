# Contributing

Thank you for helping make this guide accurate, understandable and useful for
exam preparation. Corrections and focused pull requests are welcome.

## Before contributing

1. Read the [project status](README.md#coverage) and the relevant unit guide.
2. Search existing issues and records to avoid duplicate work.
3. Use an official paper or answer key when available. If no reliable key is
   available, derive the answer independently and show enough reasoning to
   verify it.
4. Do not commit source PDFs, copied coaching explanations, promotional text
   or material you do not have permission to redistribute.

## A complete solved-question contribution

Each solution should include:

- the question and options, preserving mathematical notation;
- a short exam/session reference rather than a local file path;
- the correct option, with official-key or independent-verification status;
- a beginner-friendly explanation of the required concepts;
- step-by-step reasoning or calculation;
- a clear final conclusion;
- a reusable method for solving similar questions;
- common traps, shortcuts or boundary cases when relevant.

Never guess an answer to make a record look complete. Mark uncertainty clearly
and place disputes in [data/disputed-questions.md](data/disputed-questions.md).

## Markdown style

- Use descriptive headings and short paragraphs that render well on GitHub.
- Keep unit question numbers continuous; do not reuse the original paper number
  as the unit sequence number.
- Put the short source reference directly below the question.
- Use Markdown tables only when they improve comparison or calculation.
- Prefer mathematical notation that GitHub renders reliably.
- Do not add absolute paths, editor-specific links, internal IDs, promotional
  text or raw extraction metadata to the reading guides.

## Rebuilding generated files

Use Python 3.10 or newer. Run commands from the repository root:

    python3 -m pip install -r requirements.txt

    python3 scripts/build_unit1_outputs.py
    python3 scripts/build_remaining_unit_guides.py
    python3 scripts/build_source_report.py
    python3 scripts/check_release.py

The release checker validates structure and links only. It does not certify an
answer, OCR transcription or chapter classification.

The source report requires the local, ignored PDFs described in
[sources/README.md](sources/README.md). OCR extraction for image-only papers
uses the macOS Vision helper in scripts/ocr_pdf.swift.

## Checks before a pull request

- Confirm that exactly ten unit guides remain in docs.
- Confirm continuous question numbering in every changed guide.
- Test all new relative links.
- Search changed Markdown for local paths, editor URLs and private data.
- Compare OCR-sensitive formulas, code, diagrams and tables with the source.
- Explain the evidence for answer or classification changes in the pull
  request description.

By contributing, you agree that original software contributions are provided
under the MIT License and original educational-content contributions are
provided under CC BY 4.0. You must have the right to submit your contribution.
