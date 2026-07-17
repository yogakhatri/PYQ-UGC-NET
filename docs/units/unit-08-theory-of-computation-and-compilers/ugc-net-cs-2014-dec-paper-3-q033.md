# Question 33

*UGC NET CS · 2014 Dec Paper 3 · Unsolvable Problems and Computational Complexity · Reduction Direction for NP-Hardness*

We can show that the clique problem is NP-hard by proving that

- **A.** CLIQUE ≤ₚ 3-CNF-SAT
- **B.** CLIQUE ≤ₚ VERTEX-COVER
- **C.** CLIQUE ≤ₚ SUBSET-SUM
- **D.** None of the above

> [!TIP]
> **Correct answer: D. None of the above**

## Solution

To prove that CLIQUE is NP-hard, a problem already known to be NP-hard must reduce to CLIQUE. The standard proof constructs a graph from a 3-CNF formula and establishes 3-CNF-SAT ≤ₚ CLIQUE. Then a polynomial-time algorithm for CLIQUE would solve 3-CNF-SAT. Every displayed reduction instead starts from CLIQUE and goes to another problem, so none proves CLIQUE hard.

## Key Points

- To prove target T is NP-hard, reduce a known NP-hard source H to it: H ≤ₚ T.

## Why the other options are incorrect

A–C all use the direction CLIQUE ≤ₚ X. Such a reduction can help show X is at least as hard as CLIQUE; it does not transfer the known hardness of X backward to CLIQUE. The direction of a reduction is the central test, making D correct.
