# Question 38

*UGC NET CS · 2018 July Paper 2 · Context-Sensitive Languages · The Language 0ⁿ1ⁿ2ⁿ*

The language A={0ⁿ1ⁿ2ⁿ | n=1,2,3,…} is:

- **1.** Context sensitive
- **2.** Context free
- **3.** Regular
- **4.** None of the above

> [!TIP]
> **Correct answer: 1. Context sensitive**

## Solution

The language {0ⁿ1ⁿ2ⁿ | n≥1} requires three separated blocks to have exactly the same count. It is a standard context-sensitive language: an LBA can mark one 0, one 1, and one 2 repeatedly while staying within the input tape. It is not context-free, as can be shown by the CFL pumping lemma or closure arguments. Therefore option 1 is correct.

## Key Points

- {aⁿbⁿ} is context-free, but adding a third equal-count block {aⁿbⁿcⁿ} moves beyond CFLs into context-sensitive languages.

## Why the other options are incorrect

Regular and context-free machines cannot enforce equality of all three unbounded counts in this ordered form. Since the language is context-sensitive, `None of the above` is also false.
