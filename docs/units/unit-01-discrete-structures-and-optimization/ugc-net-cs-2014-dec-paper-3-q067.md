# Question 67

*UGC NET CS · 2014 Dec Paper 3 · Optimization · Artificial Variables and Infeasibility*

If an artificial variable remains in the basic-variable column of an optimal simplex tableau, the solution is:

- **A.** Optimum
- **B.** Infeasible
- **C.** Unbounded
- **D.** Degenerate

> [!TIP]
> **Correct answer: Intended answer: B, infeasible—provided the remaining artificial basic variable has a positive value. Presence alone is insufficient if its value is zero.**

## Solution

Artificial variables are introduced only to obtain an initial basis; the original model requires all of them to be zero. If an optimal Phase-I/Big-M tableau still has an artificial basic variable with positive right-hand-side value, the original constraints cannot be satisfied, so the problem is infeasible. However, an artificial variable may remain basic at value zero because of degeneracy or a redundant constraint without making the model infeasible.

## Key Points

- At the end, inspect the value—not just the name—of an artificial basic variable: positive means infeasible; zero may be a degenerate feasible basis.

## Why the other options are incorrect

Optimum and unbounded do not describe the implication of a positive artificial value. Degenerate may describe the zero-valued-basic exception, not the usual positive case. Since the printed question omits the artificial variable's value, B is the conventional intended choice but the condition is technically incomplete.
