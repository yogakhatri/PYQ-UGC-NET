# Question 32

*UGC NET CS · 2009 Dec Paper 2 · Unsolvable Problems and Computational Complexity · Complexity Measurement and Classification*

Which of the following grammar is LR (1) ?

- **A.** A → a A b, A → b A b, A → a , A → b
- **B.** A → a A a, A → a A b, A → c
- **C.** A → A + A, A → a
- **D.** Both (A) and (B)

> [!TIP]
> **Correct answer: D. Both (A) and (B)**

## Solution

Grammar A describes nested strings whose leading production choice is recoverable from the eventual handle/lookahead, and grammar B describes a^n c followed by n symbols from {a,b}; both have deterministic rightmost reductions with one-symbol lookahead and are LR(1). Grammar C, A→A+A|a, is ambiguous because a+a+a has two parse trees. Hence both A and B, but not C.

## Key Points

- LR grammars must be unambiguous; canonical LR(1) lookahead can resolve deterministic nested handles.

## Why the other options are incorrect

Options A and B omit the other LR(1) grammar. Option C selects an ambiguous grammar, and an ambiguous grammar cannot be LR(k).
