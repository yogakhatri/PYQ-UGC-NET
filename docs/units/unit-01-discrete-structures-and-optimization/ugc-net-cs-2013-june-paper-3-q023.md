# Question 23

*UGC NET CS · 2013 June Paper 3 · Optimization · Alternate Optimum in the Simplex Method*

At any iteration of simplex method, if Δj (Zj – Cj) corresponding to any non-basic variable Xj is obtained as zero, the solution under the test is

- **A.** Degenerate solution
- **B.** Unbounded solution
- **C.** Alternative solution
- **D.** Optimal solution

> [!TIP]
> **Correct answer: C. Alternative solution**

## Solution

In an optimal simplex tableau, a nonbasic variable normally has a strictly non-improving reduced cost. If its reduced cost Zj-Cj is exactly zero, that variable can enter the basis without changing the objective value. A pivot may therefore produce a different basic feasible solution with the same optimum-an alternative optimal solution.

## Key Points

- At optimum, zero reduced cost for a nonbasic variable means another basis can achieve the same objective value.

## Why the other options are incorrect

Degeneracy concerns a basic variable equal to zero, not a zero reduced cost for a nonbasic variable. Unboundedness requires an improving entering column with no valid leaving row. Optimality of the current solution is established by the sign condition on all reduced costs; the extra zero specifically signals an alternative optimum.
