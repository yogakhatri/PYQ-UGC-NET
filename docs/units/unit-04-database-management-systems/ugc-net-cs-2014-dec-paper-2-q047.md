# Question 47

*UGC NET CS · 2014 Dec Paper 2 · Data Warehousing and Data Mining · Factless Fact Tables*

Fact-less fact table in a data warehouse contains

- **A.** only measures
- **B.** only dimensions
- **C.** keys and measures
- **D.** only surrogate keys

> [!TIP]
> **Correct answer: B. only dimensions**

## Solution

A factless fact table records that an event occurred or that a condition/coverage relationship exists without storing a numeric measure. Its rows consist chiefly of foreign keys to dimension tables, possibly with degenerate keys. Thus 'only dimensions' is the intended description: dimension keys are present, measures are absent.

## Key Points

- Factless fact table = dimension-key combinations whose row existence is the fact.

## Why the other options are incorrect

A is the opposite of factless. C describes an ordinary fact table containing both keys and measures. D is too narrow: the table contains keys referencing several dimensions, not only surrogate keys as an isolated category.
