# Extraction Errors and Review Log

## File-open failures

None. All 36 retained UGC NET, answer-key and syllabus PDFs open successfully.

## OCR-required files

The following files have no usable native text layer and were processed with page-delimited OCR:

- `sources/ugc-net-cs-2012-dec-paper-2.pdf`
- `sources/ugc-net-cs-2018-dec-combined-paper-1-and-2.pdf`
- `sources/ugc-net-cs-2019-dec-combined-paper-1-and-2.pdf`
- `sources/ugc-net-cs-2019-june-combined-paper-1-and-2.pdf`
- `sources/ugc-net-cs-2020-nov-combined-with-answers.pdf`
- `sources/ugc-net-cs-2024-june-unofficial-question-paper.pdf`

The four 2015 UGC NET PDFs contain native text, but their embedded character maps frequently extract as `/G...` glyph codes. OCR copies were therefore generated for question recovery.

## Known extraction risks

- Mathematical symbols, matrices, diagrams and color-coded correct answers require visual page verification after OCR.
- Browser-exported NTA papers often store formulas or answer choices as images even when surrounding text extracts normally.
- `sources/ugc-net-cs-2024-june-unofficial-question-paper.pdf` is an unofficial copy; any printed answer marking is not an official answer.

Only curated Unit 1 text is promoted to `questions.json` after source-page checks. The working all-unit index and Units 2–10 may retain damaged text for review and must not be treated as verified transcriptions.
