# Question 37

*UGC NET CS · 2014 Dec Paper 2 · Memory Management · Shared Text and Per-Process Memory*

An editor has 200 K of program text, 15 K of initial stack, 50 K of initialized data and 70 K of bootstrap code. If five editors start simultaneously, how much physical memory is needed when shared text is used?

- **A.** 1135 K
- **B.** 335 K
- **C.** 1065 K
- **D.** 320 K

> [!TIP]
> **Correct answer: No listed option follows from correct memory sharing. If both read-only code sections are shared, the total is 595 K; if only the 200 K program-text segment is shared, it is 875 K.**

## Solution

Each editor must have its own writable stack (15 K) and initialized-data instance (50 K), so five processes require 5×65=325 K of private memory. Program text is read-only and can be shared once. Bootstrap code is also code and, if shareable, contributes one 70 K copy: 200+70+325=595 K. If 'shared text' narrowly names only the 200 K segment and bootstrap code is private, the total is 200+5×(15+50+70)=875 K. Neither interpretation produces an offered value.

## Key Points

- Processes may share read-only code, but each needs private stack and writable data; count shared segments once and private segments per process.

## Why the other options are incorrect

335 K is merely one editor's total and incorrectly shares writable stacks/data among five processes. 320 K even omits the stack. 1065 K and 1135 K arise from inconsistent mixtures of duplicated text and shared private state. A valid answer requires the question to clarify which code sections are shareable and to list 595 K or 875 K.
