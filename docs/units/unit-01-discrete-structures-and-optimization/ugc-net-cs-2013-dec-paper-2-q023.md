# Question 23

*UGC NET CS · 2013 Dec Paper 2 · Counting, Mathematical Induction and Discrete Probability · Mathematical Induction*

_____ is often used to prove the correctness of a recursive function.

- **A.** Diagonalization
- **B.** Commutativity
- **C.** Mathematical induction
- **D.** Matrix multiplication

> [!TIP]
> **Correct answer: C. Mathematical induction**

## Solution

A recursive function reduces a problem to smaller instances of the same form. Mathematical induction mirrors this structure: prove the base case, assume correctness for smaller input, and use that assumption to prove the next case. This makes induction the standard proof method for recursive algorithms.

## Key Points

- Recursion and induction are structural partners: base case corresponds to the induction base, and the recursive step corresponds to the inductive step.

## Why the other options are incorrect

Diagonalization proves certain existence or non-computability results, commutativity is an algebraic property, and matrix multiplication is an operation. None supplies the base-case and inductive-step structure needed here.
