# Question 68

*UGC NET CS · 2014 Dec Paper 3 · Optimization · Degeneracy in Transportation Problems*

What does degeneracy mean in a transportation problem?

- **A.** total supply equals total demand
- **B.** total supply does not equal total demand
- **C.** the solution so obtained is not feasible
- **D.** none of these

> [!TIP]
> **Correct answer: D. none of these**

## Solution

For an m×n transportation problem, a nondegenerate basic feasible solution has exactly m+n−1 occupied independent cells. Degeneracy occurs when the number of positive allocations is smaller than m+n−1, often handled by placing a tiny ε allocation in a suitable empty cell. None of A–C states this condition, so D is correct.

## Key Points

- Transportation degeneracy concerns too few basic occupied cells, not supply-demand balance or feasibility.

## Why the other options are incorrect

Equal total supply and demand merely defines a balanced transportation problem. Unequal totals define an unbalanced problem that can be balanced with a dummy row or column. A degenerate solution can still be feasible, so C is false.
