# Question 32

*UGC NET CS · 2015 June Paper 3 · Advanced Algorithms · Exact Exponential Algorithms for TSP*

The travelling salesman problem can be solved in :

- **1.** Polynomial time using dynamic programming algorithm
- **2.** Polynomial time using branch-and-bound algorithm
- **3.** Exponential time using dynamic programming algorithm or branch-and-bound algorithm
- **4.** Polynomial time using backtracking algorithm

> [!TIP]
> **Correct answer: 3. Exponential time using dynamic programming algorithm or branch-and-bound algorithm**

## Solution

Exact TSP is NP-hard. Held-Karp dynamic programming stores the best path for each subset and endpoint in `Θ(n^2 2^n)` time, which is exponential. Branch-and-bound may prune many tours on favorable inputs, but its worst case is also exponential because it can explore an exponential search tree. Thus option 3 correctly describes both exact approaches.

## Key Points

- Exact TSP remains exponential; dynamic programming improves over n!
- enumeration but does not make it polynomial.

## Why the other options are incorrect

No known general exact polynomial-time algorithm is supplied by dynamic programming, branch-and-bound, or backtracking. Options 1, 2, and 4 incorrectly label these exact methods polynomial.
