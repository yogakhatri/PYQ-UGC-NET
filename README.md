# UGC NET Computer Science PYQ Study Guide

An exam-focused, community-maintained study guide for UGC NET Computer Science and Applications previous-year questions.

> [!IMPORTANT]
> **Unit 1 is reviewed and solved. Units 2-10 are public working guides:** their recovered questions, chapter placement, foundational notes and exam methods are available, but unverified answers are intentionally withheld. Please do not treat a question marked as awaiting validation as a solved record.

## Start studying

| Unit | Guide | Questions | Status |
|---:|---|---:|---|
| 1 | [Discrete Structures and Optimization](docs/unit-1-discrete-structures-and-optimization.md) | 143 | Reviewed, solved and explained |
| 2 | [Computer System Architecture](docs/unit-2-computer-system-architecture.md) | 394 | Indexed; answers under validation |
| 3 | [Programming Languages and Computer Graphics](docs/unit-3-programming-languages-and-computer-graphics.md) | 176 | Indexed; answers under validation |
| 4 | [Database Management Systems](docs/unit-4-database-management-systems.md) | 178 | Indexed; answers under validation |
| 5 | [System Software and Operating System](docs/unit-5-system-software-and-operating-system.md) | 184 | Indexed; answers under validation |
| 6 | [Software Engineering](docs/unit-6-software-engineering.md) | 178 | Indexed; answers under validation |
| 7 | [Data Structures and Algorithms](docs/unit-7-data-structures-and-algorithms.md) | 250 | Indexed; answers under validation |
| 8 | [Theory of Computation and Compilers](docs/unit-8-theory-of-computation-and-compilers.md) | 223 | Indexed; answers under validation |
| 9 | [Data Communication and Computer Networks](docs/unit-9-data-communication-and-computer-networks.md) | 257 | Indexed; answers under validation |
| 10 | [Artificial Intelligence](docs/unit-10-artificial-intelligence.md) | 98 | Indexed; answers under validation |

The ten guides currently contain **2,081 study records**. Use the [guide index](docs/README.md) for a compact reading page or the [official syllabus transcription](docs/syllabus.md) to plan revision.

## How the guides are designed

Each unit is written for direct reading on GitHub:

- syllabus-aligned chapters and stable contents links;
- continuous question numbering within each unit;
- short references such as “UGC NET June 2023, original Q19”;
- foundational concepts before the solution method;
- exam-focused rules, shortcuts and common traps;
- source paths and internal IDs kept out of the reading flow;
- no guessed answer where an official key or independent derivation is unavailable.

For solved Unit 1 questions, use this sequence:

1. Attempt the question without looking at the answer.
2. Read **Build the basics**.
3. Follow the **Step-by-step reasoning**.
4. Reuse the rule under **How to solve similar questions**.

## Coverage

- **UGC NET Computer Science:** 33 locally inventoried paper files covering the 2009-2026 date range.
- **Master extraction index:** 2,102 retained Computer Science blocks after removing Paper 1 and third-party coaching/promotional content.
- **2021 and 2022 papers:** all 100 Computer Science question positions recovered from each.
- **Rajasthan SET Computer Science:** no verifiable paper is present in the supplied corpus.
- **RPSC supplemental papers:** four recruitment papers are inventoried but excluded from NET/SET question counts.

See the [coverage audit](data/all-units-coverage-audit.md), [source inventory](data/source-files-report.md), [classification review](data/classification-review.md) and [disputed questions](data/disputed-questions.md).

## Source PDFs

Source PDFs are **not intended to be committed to the public repository**. They are ignored by Git because they total approximately 163 MB and may contain material owned by examination bodies or third-party publishers.

The public repository retains:

- descriptive filenames and hashes in the [source inventory](data/source-files-report.md);
- source/page references in structured audit data;
- reproduction instructions in [sources/README.md](sources/README.md).

This keeps the repository lightweight and avoids implying that the project can relicense third-party papers.

## Data and reproducibility

| Path | Purpose |
|---|---|
| [data/questions.json](data/questions.json) | Reviewed Unit 1 records and solutions |
| [data/questions.csv](data/questions.csv) | Spreadsheet-friendly Unit 1 data |
| [data/all-unit-question-index.json](data/all-unit-question-index.json) | Working extraction index across all units |
| [data/unit-1-audit.md](data/unit-1-audit.md) | Unit 1 extraction and validation evidence |
| [scripts/build_unit1_outputs.py](scripts/build_unit1_outputs.py) | Rebuilds Unit 1 Markdown and structured data |
| [scripts/build_remaining_unit_guides.py](scripts/build_remaining_unit_guides.py) | Rebuilds Units 2-10 |
| [scripts/build_source_report.py](scripts/build_source_report.py) | Rebuilds the local PDF inventory |
| [scripts/check_release.py](scripts/check_release.py) | Checks guide counts, numbering, references, links and public files |

The extraction scripts use Python and, for image-only PDFs on macOS, Vision OCR through [scripts/ocr_pdf.swift](scripts/ocr_pdf.swift).

Before publishing a change, run:

    python3 scripts/check_release.py

## Repository layout

    .
    ├── README.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── CONTENT_LICENSE.md
    ├── NOTICE.md
    ├── docs/       # Syllabus and ten readable unit guides
    ├── data/       # Structured records, audits and review queues
    ├── scripts/    # Reproducible extraction and generation tools
    └── sources/    # Local-only PDFs plus public setup instructions

## Contributing

Corrections and new worked solutions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

High-value contributions include:

- independently derived solutions for Units 2-10;
- corrections to OCR-damaged notation;
- better chapter placement with a short justification;
- validation against an official answer key;
- clearer explanations that teach the underlying method.

Do not submit copied coaching-book explanations, promotional text, guessed answers or source PDFs.

## Licensing and third-party material

- Scripts are licensed under the [MIT License](LICENSE).
- Original educational notes and explanations are licensed under [CC BY 4.0](CONTENT_LICENSE.md).
- Examination questions, official keys, trademarks and third-party source material are **not** relicensed by this project. See [NOTICE.md](NOTICE.md).

## Disclaimer

This is an independent educational project. It is not affiliated with or endorsed by UGC, NTA, RPSC or any examination authority. Always consult the official notification, syllabus and answer key for the examination session you are preparing for.
