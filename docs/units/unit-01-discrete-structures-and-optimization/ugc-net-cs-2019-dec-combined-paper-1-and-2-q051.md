# Question 51

*UGC NET CS · 2019 Dec Paper 1 And 2 · Optimization · Degeneracy in Transportation Problems*

A basic feasible solution of an m x n transportation problem is non-degenerate if it contains exactly how many individual allocations, and in what kind of positions?

- **1.** m+n+1, independent
- **2.** m+n-1, independent
- **3.** m+n-1, appropriate
- **4.** m-n+1, independent

> [!TIP]
> **Correct answer: 2. m+n-1, independent**

## Solution

A balanced m×n transportation model has m row equations and n column equations, but one equation is redundant because total supply equals total demand. The constraint rank is therefore m+n−1, so a basic feasible solution can have at most m+n−1 basic allocations. It is non-degenerate when all m+n−1 of those allocations are positive and occupy independent positions—that is, their cells do not form a closed allocation loop. Hence option 2.

## Key Points

- Non-degenerate transportation BFS = exactly m+n−1 positive allocations in independent cells.

## Why the other options are incorrect

m+n+1 and m−n+1 are not the rank of the transportation constraints. Option 3 gives the right count but replaces the essential mathematical condition ‘independent’ with the vague word ‘appropriate.’ Fewer than m+n−1 positive basic allocations would be a degenerate solution.
