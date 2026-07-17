# Question 24

*UGC NET CS · 2013 June Paper 3 · Optimization · Degeneracy in Transportation Problems*

A basic feasible solution to a m-origin, n-destination transportation problem is said to be _________ if the number of positive allocations are less than m + n – 1.

- **A.** degenerate
- **B.** non-degenerate
- **C.** unbounded
- **D.** unbalanced

> [!TIP]
> **Correct answer: A. degenerate**

## Solution

A nondegenerate basic feasible solution of an m-by-n transportation problem has exactly m+n-1 occupied independent cells. If fewer than m+n-1 allocations are positive, one or more basic variables have value zero; the solution is called degenerate.

## Key Points

- Transportation degeneracy test: positive allocations < m+n-1.

## Why the other options are incorrect

Nondegenerate requires the full m+n-1 positive basic allocations. Unbounded describes an objective that can improve without limit. Unbalanced means total supply differs from total demand and is fixed by a dummy row/column; it is unrelated to the number of positive allocations.
