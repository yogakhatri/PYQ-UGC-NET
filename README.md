# UGC NET Computer Science Previous-Year Question Guide

A free, community-maintained study guide for **UGC NET Computer Science and
Applications** previous-year questions.

Questions are arranged by syllabus unit and chapter. The aim is to explain the
basic idea behind each question, solve it step by step, and teach a method that
can also be used for similar questions.

This repository covers the **subject-specific Computer Science paper only**. It
does not cover Paper 1 (teaching and research aptitude), and it is not a
complete replacement for textbooks, current official notices or full mock
tests.

> [!IMPORTANT]
> **Unit 1 has project-reviewed solutions. Units 2–10 are working question
> inventories, not solved guides.** All 1,938 answers in Units 2–10 are still
> withheld. Some question placement, OCR text, formulas and missing figures
> also require manual correction. Do not use Units 2–10 as your only source for
> answer checking or final revision.

## Open a unit

| Unit | Topic and guide | Questions | Current status |
|---:|---|---:|---|
| 1 | [Discrete Structures and Optimization](docs/unit-1-discrete-structures-and-optimization.md) | 143 | Project-reviewed solutions |
| 2 | [Computer System Architecture](docs/unit-2-computer-system-architecture.md) | 394 | Question inventory; not solved |
| 3 | [Programming Languages and Computer Graphics](docs/unit-3-programming-languages-and-computer-graphics.md) | 176 | Question inventory; not solved |
| 4 | [Database Management Systems](docs/unit-4-database-management-systems.md) | 178 | Question inventory; not solved |
| 5 | [System Software and Operating System](docs/unit-5-system-software-and-operating-system.md) | 184 | Question inventory; not solved |
| 6 | [Software Engineering](docs/unit-6-software-engineering.md) | 178 | Question inventory; not solved |
| 7 | [Data Structures and Algorithms](docs/unit-7-data-structures-and-algorithms.md) | 250 | Question inventory; not solved |
| 8 | [Theory of Computation and Compilers](docs/unit-8-theory-of-computation-and-compilers.md) | 223 | Question inventory; not solved |
| 9 | [Data Communication and Computer Networks](docs/unit-9-data-communication-and-computer-networks.md) | 257 | Question inventory; not solved |
| 10 | [Artificial Intelligence](docs/unit-10-artificial-intelligence.md) | 98 | Question inventory; not solved |

There are **10 unit guides with 2,081 study records**. You can also use the
[one-page guide index](docs/README.md) or read the [official syllabus
transcription](docs/syllabus.md).

## What each guide contains

- chapters arranged according to the UGC NET syllabus;
- previous-year questions numbered continuously inside each unit;
- a short reference showing the examination and original question number;
- chapter-level foundations and exam methods;
- formulas, rules and exam shortcuts;
- question-specific, step-by-step reasoning in the reviewed Unit 1 guide;
- common mistakes and methods for solving similar questions;
- no guessed answer when reliable verification is not available.

## How to use the guide

1. Choose a unit from the table above.
2. Use the contents section inside the unit to open a chapter.
3. Try the question before reading the explanation.
4. Revise the basic concept and important formula.
5. Follow the solution steps.
6. Study the “How to solve similar questions” section.
7. Mark difficult questions and try them again during revision.

For Units 2–10, chapter notes are general revision notes rather than detailed
solutions to each question. Text saying that an answer is awaiting validation
means the final answer has not been verified.

## Current coverage

- **UGC NET Computer Science:** 33 local paper files covering examinations from
  2009 to 2026.
- **Corpus limitation:** this is not a complete collection of every session or
  every question. Several papers are missing, partial or damaged during
  extraction.
- **Questions in the broad extraction index:** 2,102 Computer Science question
  blocks after removing Paper 1 material and coaching/promotional content.
- **Questions in the readable unit guides:** 2,081.
- **Unit 1:** 143 reviewed questions with answers and explanations.
- **2021 and 2022:** all 100 Computer Science question positions were recovered
  from each paper.
- **Rajasthan SET Computer Science:** no verifiable paper is present in the
  available local collection, so Rajasthan SET coverage is not claimed.
- **Paper 1:** not covered; the repository focuses on Computer Science subject
  questions.

For detailed evidence, see the [coverage audit](data/all-units-coverage-audit.md),
[Unit 1 audit](data/unit-1-audit.md), [source inventory](data/source-files-report.md),
[classification review](data/classification-review.md), [extraction issues](data/extraction-errors.md)
and [disputed questions](data/disputed-questions.md).

## Project folders

| Folder | What it contains |
|---|---|
| [docs](docs/README.md) | The syllabus and all ten readable unit guides |
| [data](data/all-units-coverage-audit.md) | Structured questions, audits and review lists |
| [scripts](scripts/check_release.py) | Tools used to extract, build and check the guides |
| [sources](sources/README.md) | Instructions for local source papers; PDFs are not published |

Important structured files:

- [data/questions.json](data/questions.json) — reviewed Unit 1 records;
- [data/questions.csv](data/questions.csv) — Unit 1 data in spreadsheet form;
- [data/all-unit-question-index.json](data/all-unit-question-index.json) — the
  working question index for all units.

## Source papers

Source PDFs are kept locally for checking questions, but they are ignored by
Git and should not be uploaded to this repository. The local collection is
about 163 MB and may include material owned by examination bodies or other
publishers.

The public repository includes filenames, hashes and extraction notes in the
[source inventory](data/source-files-report.md), without redistributing the PDF
files. See [sources/README.md](sources/README.md) for the local setup.

## Help improve the guide

Contributions are welcome. Useful contributions include:

- checked solutions for Units 2–10;
- clearer beginner-friendly explanations;
- corrections to damaged OCR text, formulas, tables or code;
- verification using an official answer key;
- corrections to chapter placement;
- reports of duplicate or disputed questions.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request and
follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Do not submit guessed answers, copied coaching explanations, promotional text
or source PDFs.

## Rebuilding and checking

The project uses Python 3.10 or newer. Install the PDF dependency, then run the
build commands from the repository root:

    python3 -m pip install -r requirements.txt

    python3 scripts/build_unit1_outputs.py
    python3 scripts/build_remaining_unit_guides.py
    python3 scripts/build_source_report.py
    python3 scripts/check_release.py

The last command checks repository structure, numbering, references, links and
public files. It does **not** prove that answers, OCR text or classifications
are correct. Read the [readiness audit](data/all-units-coverage-audit.md) before
using or publishing the guides.

## License

- Project scripts are available under the [MIT License](LICENSE).
- Original notes, explanations and worked solutions are available under
  [Creative Commons Attribution 4.0](CONTENT_LICENSE.md).
- Examination questions, official answer keys, trademarks and third-party
  material are not relicensed by this project. Read [NOTICE.md](NOTICE.md).

## Disclaimer

This is an independent educational project. It is not affiliated with or
endorsed by UGC, NTA or any examination authority.
Always check the official syllabus, notification and final answer key for your
examination session.
