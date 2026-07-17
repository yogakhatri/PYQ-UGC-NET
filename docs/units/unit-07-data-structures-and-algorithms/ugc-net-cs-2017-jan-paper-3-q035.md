# Question 35

*UGC NET CS · 2017 Jan Paper 3 · Greedy Algorithms · Dijkstra's Shortest-Path Algorithm*

Dijkstra’s algorithm is based on

- **1.** Divide and conquer paradigm
- **2.** Dynamic programming
- **3.** Greedy Approach
- **4.** Backtracking paradigm

> [!TIP]
> **Correct answer: 3. Greedy Approach**

## Solution

Dijkstra's algorithm repeatedly chooses the unsettled vertex with the smallest tentative distance and permanently settles it. With nonnegative edge weights, no later route through a farther unsettled vertex can improve that distance. This locally best safe choice is the greedy-choice principle, so option 3 is correct.

## Key Points

- Dijkstra is greedy: repeatedly finalize the smallest tentative distance; negative edges invalidate the safety argument.

## Why the other options are incorrect

The algorithm does not recursively divide the graph, fill a dynamic-programming table, or explore and undo choices as backtracking does. Its correctness specifically relies on greedy selection and nonnegative weights.
