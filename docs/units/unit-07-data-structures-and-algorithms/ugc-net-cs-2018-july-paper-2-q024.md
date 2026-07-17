# Question 24

*UGC NET CS · 2018 July Paper 2 · Graph Algorithms · Dijkstra Single-Source Shortest Paths*

Which algorithm solves the single-source shortest-path problem?

- **1.** Prim’s algorithm
- **2.** Floyd - Warshall algorithm
- **3.** Johnson’s algorithm
- **4.** Dijkstra’s algorithm

> [!TIP]
> **Correct answer: 4. Dijkstra’s algorithm**

## Solution

Dijkstra's algorithm computes shortest-path distances from one selected source to all reachable vertices when edge weights are nonnegative. It repeatedly finalizes the unsettled vertex with minimum tentative distance and relaxes outgoing edges. Therefore option 4 is correct.

## Key Points

- Dijkstra = single source with nonnegative weights; Bellman–Ford handles negative edges; Floyd–Warshall/Johnson = all pairs.

## Why the other options are incorrect

Prim builds a minimum spanning tree, not source-rooted shortest paths. Floyd–Warshall and Johnson are all-pairs shortest-path algorithms. Dijkstra is the only listed algorithm whose standard problem statement is single-source shortest paths.
