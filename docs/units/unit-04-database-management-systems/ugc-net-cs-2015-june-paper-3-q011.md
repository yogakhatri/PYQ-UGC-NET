# Question 11

*UGC NET CS · 2015 June Paper 3 · Relational Database Design · Binary Lossless-Join Decomposition Test*

The relation schemas R1 and R2 form a lossless-join decomposition of R if and only if which conditions hold? (a) (R1 ∩ R2) → (R1 − R2) (b) R1 → R2 (c) (R1 ∩ R2) → (R2 − R1) (d) R2 → (R1 ∩ R2). Codes:

- **1.** (a) and (b) happens
- **2.** (a) and (d) happens
- **3.** (a) and (c) happens
- **4.** (b) and (c) happens

> [!TIP]
> **Correct answer: 3. (a) and (c) happens**

## Solution

For a binary decomposition `R → R1, R2`, the join is lossless exactly when the common attributes functionally determine all attributes unique to at least one component: `(R1 ∩ R2) → (R1 − R2)` or `(R1 ∩ R2) → (R2 − R1)`. These are conditions (a) and (c), so option 3 is correct.

## Key Points

- A binary decomposition is lossless iff the shared attributes form a superkey for R1 or for R2.

## Why the other options are incorrect

Conditions (b) and (d) are not the standard binary lossless-join test. The determinant must be the intersection shared by both decomposed schemas; options 1, 2, and 4 include at least one irrelevant or incorrectly oriented dependency.
