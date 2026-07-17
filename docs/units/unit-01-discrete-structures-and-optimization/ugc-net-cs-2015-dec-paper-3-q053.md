# Question 53

*UGC NET CS · 2015 Dec Paper 3 · Optimization · Non-Degenerate Transportation Solutions*

Consider these conditions for an initial transportation solution: (a) it is feasible and satisfies every supply and demand constraint; (b) it has exactly m+n−1 positive allocations for m rows and n columns; and (c) all positive allocations occupy independent positions. Which conditions characterize a non-degenerate basic feasible solution?

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (b) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

A transportation basic feasible solution must first be feasible, satisfying every supply and demand equation. For an m×n transportation table, a non-degenerate basis contains exactly m+n−1 positive allocations, and those occupied cells must be independent—meaning they do not form a closed allocation loop. Therefore all three conditions are required.

## Key Points

- Non-degenerate transportation BFS = feasible + exactly m+n−1 positive independent allocations.

## Why the other options are incorrect

Each of options 1–3 omits one necessary condition. Feasibility alone is insufficient, the count m+n−1 alone is insufficient, and occupied cells forming a loop are linearly dependent and cannot constitute a valid transportation basis.
