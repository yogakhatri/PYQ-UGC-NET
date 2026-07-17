# Question 3

*UGC NET CS · 2013 Dec Paper 3 · Optimization · Linear-Programming Feasibility*

The following Linear Programming problem has : Max Z = x1 + x2 Subject to x1 – x2 ≥ 0 3 x1 – x2 ≤ –3 and x1, x2 ≥ 0

- **A.** Feasible solution
- **B.** No feasible solution
- **C.** Unbounded solution
- **D.** Single point as solution

> [!TIP]
> **Correct answer: B. No feasible solution**

## Solution

From x1-x2≥0 and x1,x2≥0, we have x2≤x1. Therefore 3x1-x2≥3x1-x1=2x1≥0. The second constraint demands the same expression be at most -3, which is impossible. The feasible region is empty.

## Key Points

- Test LP feasibility before optimizing; combine inequalities to expose contradictions.

## Why the other options are incorrect

With no point satisfying both constraints, the program cannot have a feasible, unbounded or single-point solution. Objective maximization is irrelevant once constraint feasibility fails.
