# Local Source Papers

[Project home](../README.md) · [Source inventory](../data/source-files-report.md) · [Coverage audit](../data/all-units-coverage-audit.md)

This directory is the local input area for question-paper extraction and
verification. PDF files here are intentionally ignored by Git and must not be
included in the public repository.

## Reproducing the local setup

1. Obtain examination papers and answer keys from official or otherwise lawful
   sources.
2. Confirm that you are permitted to download and use each file.
3. Save the files locally in this directory using the descriptive filenames in
   the [source inventory](../data/source-files-report.md).
4. Run the extraction or report scripts from the repository root.

The public inventory records filenames, hashes and extraction notes so that
contributors can identify matching inputs without redistributing them.

## Important limits

- Do not add PDFs to Git, Git LFS, release assets or pull requests merely
  because they are available elsewhere online.
- Do not submit coaching compilations, answer guides or promotional documents.
- Prefer official papers and official answer keys.
- Treat OCR output as untrusted until formulas, code, diagrams and tables have
  been compared with the source page.

The scripts expect local files, but the readable Markdown guides do not require
the PDFs and can be used directly on GitHub.
