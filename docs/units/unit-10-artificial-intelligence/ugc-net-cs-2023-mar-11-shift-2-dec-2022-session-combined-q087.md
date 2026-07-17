# Question 87

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Approaches to AI · Heuristic Search*

The A* algorithm is optimal when.

- **1.** It always finds the solution with the lowest total cost if the heuristic 'h' is admissible.
- **2.** Always finds the solution with the highest total cost if the heuristic "h' is admissible.
- **3.** Finds the solution with the lowest total cost if the heuristic h' is not admissible.
- **4.** It always finds the solution with the highest total cost if the heuristic 'h' is not admissible.

> [!TIP]
> **Correct answer: 1. It always finds the solution with the lowest total cost if the heuristic 'h' is admissible.**

## Solution

A* orders nodes by f(n)=g(n)+h(n). If h is admissible, it never overestimates the remaining optimal cost; with the usual graph-search consistency/reopening conditions, A* returns a solution of minimum total path cost.

## Key Points

- Admissible h(n)≤h*(n) is the central optimality condition for A*.

## Why the other options are incorrect

A* is a minimization algorithm, so the highest-cost alternatives are reversed. A non-admissible heuristic can overestimate and cause an optimal path to be skipped.
