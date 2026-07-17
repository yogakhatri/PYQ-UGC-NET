# Question 20

*UGC NET CS · 2014 Dec Paper 2 · Functional Dependencies · Candidate Key by Attribute Closure*

Identify the minimal key for relational scheme R(A, B, C, D, E ) with functional dependencies F = {A → B, B → C, AC → D}

- **A.** A
- **B.** AE
- **C.** BE
- **D.** CE

> [!TIP]
> **Correct answer: B. AE**

## Solution

Attribute E never appears on the right side of any dependency, so every key must include E. Starting with A, use A→B, then B→C, and with A and C use AC→D; thus A⁺={A,B,C,D}. Adding E gives (AE)⁺={A,B,C,D,E}. Neither A nor E alone is a superkey, so AE is minimal.

## Key Points

- Attributes absent from all FD right sides must appear in every candidate key; then compute closures.

## Why the other options are incorrect

A determines A–D but cannot determine E. BE gives B,C,E but cannot recover A or D. CE cannot derive A, B or D. Only AE closes to the entire relation.
