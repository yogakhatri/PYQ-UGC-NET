# Question 25

*UGC NET CS · 2013 Dec Paper 3 · Heuristic Search · A-Star Admissible Heuristics*

If h * represents an estimate of the cost of getting from the current node N to the goal node and h represents actual cost of getting from the current node to the goal node, then A * algorithm gives an optimal solution if

- **A.** h * is equal to h
- **B.** h * overestimates h
- **C.** h * underestimates h
- **D.** none of these

> [!TIP]
> **Correct answer: C. h * underestimates h**

## Solution

A* is optimal when its heuristic is admissible: h*(N)≤h(N) for every node, so it never overestimates the true remaining cost. The intended option is that the estimate underestimates the actual cost; equality is also allowed as the limiting perfect-heuristic case.

## Key Points

- A* tree-search optimality uses an admissible heuristic: 0≤h*≤true remaining cost; consistency is the stronger graph-search condition.

## Why the other options are incorrect

Overestimation can cause A* to ignore the optimal path. A states only exact equality, which is sufficient but unnecessarily stronger than the general admissibility condition. The complete rule is non-overestimation.
