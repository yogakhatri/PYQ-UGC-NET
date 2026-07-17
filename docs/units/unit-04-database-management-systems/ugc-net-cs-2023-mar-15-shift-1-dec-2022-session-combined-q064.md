# Question 64

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Centralized and Client/Server DBMS Architectures*

S1. 10-87014 Consider the relation R(P, Q, R, S, T, U, V, W, X, Y) and FDs: {P, Q. S) → T R → Y (P, Q) - V (R. X) - X Q → U V -(W, X} Which of the following is a candidate key?

- **1.** {P, Q, R, S)
- **2.** (R, Q, X}
- **3.** (V, X}
- **4.** None of the above

> [!TIP]
> **Correct answer: 1. {P, Q, R, S)**

## Solution

P,Q,R,S never occur on any FD right side, so every key must contain them. Their closure derives T from PQS, V from PQ, W and X from V, Y from R, and U from Q—every attribute. Removing any of P,Q,R,S loses that attribute, so {P,Q,R,S} is a candidate key.

## Key Points

- Attributes absent from all FD right sides must appear in every candidate key.

## Why the other options are incorrect

The other sets omit P or S, which cannot be derived; hence their closures are incomplete.
