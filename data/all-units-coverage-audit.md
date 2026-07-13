# All-Units Coverage Audit

## Outcome

Exactly ten unit guide files are present. Unit 1 is the reviewed, solved standard. Units 2-10 are comprehensive working inventories for the recoverable local corpus, but are not yet fully solved or answer-validated.

| Unit | Guide records | Chapter classification | Correct option / worked solution |
|---|---:|---|---|
| 1 | 143 | Reviewed | Complete |
| 2 | 394 | 327 keyword-supported; 67 review | Pending validation |
| 3 | 176 | 157 keyword-supported; 19 review | Pending validation |
| 4 | 178 | 158 keyword-supported; 20 review | Pending validation |
| 5 | 184 | 176 keyword-supported; 8 review | Pending validation |
| 6 | 178 | 165 keyword-supported; 13 review | Pending validation |
| 7 | 250 | 200 keyword-supported; 50 review | Pending validation |
| 8 | 223 | 192 keyword-supported; 31 review | Pending validation |
| 9 | 257 | 188 keyword-supported; 69 review | Pending validation |
| 10 | 98 | 90 keyword-supported; 8 review | Pending validation |

The ten guides contain 2,081 records: 143 curated Unit 1 records plus 1,938 working records for Units 2-10.

## Broader extraction index

The broad all-unit extraction currently contains 2,102 question blocks from 33 UGC NET question-paper PDFs. It excludes 83 answer, explanation and promotional blocks found in a third-party 2023 compilation. The 2021 and 2022 answer-bearing papers were reparsed by internal question ID, recovering all 100 Computer Science question positions in each and removing mixed Paper 1 content. It assigns 164 blocks to Unit 1, while 143 survive the stricter Unit 1 curation and solution workflow. The remaining broad-pass Unit 1 candidates are not silently added to the completed guide because they include low-confidence routing, source defects, duplicates or blocks rejected by the focused audit.

The broad index is stored in data/all-unit-question-index.json. It is an extraction and routing artifact, not an answer key.

## What Units 2-10 currently provide

- official-syllabus chapter structure;
- exam-focused concept summaries, formulas, reusable methods and common traps;
- every recovered question block assigned to a chapter;
- source PDF and page links;
- visible classification confidence;
- explicit placeholders for unvalidated answers and worked derivations.

## What remains before calling all ten units complete

1. Manually inspect the 285 chapter placements with no direct chapter-keyword support.
2. Recheck diagrams, tables, code and mathematical notation against source scans.
3. Match answer-bearing papers and standalone keys by exam and question number.
4. Independently derive every answer, including legacy papers without reliable keys.
5. Add question-specific explanations and a method for solving variants.
6. Run duplicate, dispute, link and answer-consistency reviews.

## Source limitation

No verifiable Rajasthan SET Computer Science question paper is present in the supplied local corpus. Four descriptively named RPSC PDFs are recruitment papers and are excluded from NET/SET coverage rather than being mislabelled.
