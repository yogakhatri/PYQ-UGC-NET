# Question 16

*UGC NET CS · 2021 Nov With Answers · Software Configuration Management · Repository Contents and Generated Artifacts*

In the context of Software Configuration Management (SCM), what kind of files should be committed to your source control repository? A. Code files B. Documentation files C. Output files D. Automatically generated files that are required for your system to be used Choose the correct answer from the options given below:

- **1.** A and B only
- **2.** B and C only
- **3.** C and D only
- **4.** D and A only

> [!TIP]
> **Correct answer: 1. A and B only**

## Solution

Source control should preserve the authoritative material needed to understand, change, and rebuild the system. That includes code files (A) and documentation files (B). Ordinary output files are results of running the program, and automatically generated files should normally be recreated by a documented, reproducible build rather than stored as independent sources. Thus A and B only, option 1.

## Key Points

- Version the sources of truth; regenerate derived outputs.

## Why the other options are incorrect

Options 2–4 include outputs or generated artifacts while omitting code or documentation. Generated files may be committed only in exceptional deployment workflows; the SCM rule tested here is to version inputs and reproducible build instructions, not derived products.
