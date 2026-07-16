# Unit 1 Extraction and Validation Audit

## Outcome

- **Guide:** `docs/unit-1-discrete-structures-and-optimization.md`
- **Solved records:** 151
- **Years represented:** every year present in the verified UGC corpus from 2009 through 2026
- **Source PDFs represented:** 31
- **Question IDs:** 151 unique
- **Topics:** all seven official Unit 1 topic groups represented
- **Question duplicate groups:** 6 conservative exact/conceptual groups
- **Rajasthan SET:** 0 questions because no verifiable SET paper/key is present

## Workflow

1. The exact Unit 1 taxonomy was transcribed from `sources/ugc-net-computer-science-official-syllabus.pdf`.
2. All 36 retained UGC NET, answer-key and syllabus PDFs were opened, page-counted and SHA-256 compared.
3. Native extraction was used where reliable; OCR was generated for scanned or broken-font papers.
4. A broad topic filter produced 235 candidate pages from all 33 UGC question-paper PDFs.
5. Candidate pages were manually classified against the official syllabus; cross-unit lookalikes were either retained with a secondary classification or excluded by the published boundary rules.
6. Mathematical notation at risk from OCR was checked against rendered source pages.
7. Answers were derived independently. Official/supplied answer evidence is recorded only when available; two genuine conflicts are documented.
8. The build validates unique IDs, source-file existence, nonempty solutions and valid option indexes. A second validation checked every recorded page against its PDF page count.

## Data contract

Each row in `questions.json` contains exam/session metadata, question number/ID, source filename and page, official unit/topic/subtopic, complete normalized question and any source options, answer status, correct answer, solution steps, concept/rule, shortcut, trap, option analysis, duplicate canonical ID and source anchor.

The CSV is a lossless tabular projection of the same 151 records; nested options and solution steps are JSON-encoded inside their CSV cells.

## Scope and exceptions

Completeness is measured against the supplied, verifiable UGC NET PDFs, not against every examination session ever published. Questions whose scans irretrievably lose operands, overbars or diagram cells are listed in `classification-review.md`; they are not silently guessed or counted as solved.

## Rebuild

```bash
python3 scripts/build_unit1_candidates.py
python3 scripts/build_unit1_outputs.py
```
