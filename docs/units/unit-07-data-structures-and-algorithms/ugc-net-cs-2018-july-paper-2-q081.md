# Question 81

*UGC NET CS · 2018 July Paper 2 · Graph Algorithms · Ford-Fulkerson Runtime with Integer Capacities*

Let E be the number of graph edges and f the value of a maximum flow. With integer capacities, the runtime of the Ford-Fulkerson algorithm is bounded by:

- **1.** O (E ∗ f)
- **2.** O (E 2∗ f)
- **3.** O (E ∗ f2)
- **4.** O (E 2∗ f2)

> [!TIP]
> **Correct answer: 1. O (E ∗ f)**

## Solution

With integer capacities, every augmenting path increases the flow value by at least 1. If the final maximum-flow value is f, Ford-Fulkerson therefore performs at most f augmentations. Finding and updating one augmenting path by graph traversal takes O(E), so the total bound is O(Ef), option 1.

## Key Points

- Integer capacities give ≤f augmentations, each costing O(E), hence O(Ef).

## Why the other options are incorrect

The squared bounds add unnecessary factors. This is the value-dependent Ford-Fulkerson bound; it is pseudo-polynomial because f may be large relative to the number of bits used to encode capacities. Edmonds-Karp instead gives O(VE²).
