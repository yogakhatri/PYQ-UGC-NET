# Question 87

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Approaches to AI · Turing Test and Rational Agents*

Which search technique is complete and optimal, when h(n) is consistent?

- **1.** Best First Search
- **2.** Depth First Search
- **3.** A* Search
- **4.** Breadth First Search

> [!TIP]
> **Correct answer: 3. A* Search**

## Solution

With a consistent heuristic, A* graph search is complete (under standard positive-cost/finite-branching conditions) and optimal. Consistency ensures f-values do not decrease along paths and closed nodes need not be reopened.

## Key Points

- Consistent h implies admissibility and monotone A* f-values.

## Why the other options are incorrect

Greedy best-first and DFS are not generally optimal; BFS is optimal only for equal step costs and does not use h.
