# Question 91

*UGC NET CS · 2019 Dec Paper 1 And 2 · Graph Algorithms · Shortest Paths*

When using Dijkstra's algorithm to find shortest path in a graph, which of the following statement is not true?

- **1.** It can find shortest path within the same graph data structure
- **2.** Every time a new node is visited. we choose the node with smallest known distance/ cost (weight) to visit first
- **3.** Shortest path always passes through least number of vertices
- **4.** The graph needs to have a non-negative weight on every edge

> [!TIP]
> **Correct answer: 3. Shortest path always passes through least number of vertices**

## Solution

A weighted shortest path minimizes total edge weight, not the number of vertices or edges. A path with several light edges can cost less than a path with one heavy edge, so statement 3 is not true. Dijkstra does select the unsettled vertex with the smallest tentative distance and requires nonnegative edge weights for its greedy finalization argument.

## Key Points

- Dijkstra minimizes weight sum; BFS on an unweighted graph minimizes edge count.

## Why the other options are incorrect

Statement 2 describes Dijkstra's central greedy choice, and statement 4 states its standard weight restriction. Statement 1 is awkwardly worded but simply says the algorithm operates on the given graph representation. Only statement 3 confuses weighted shortest path with unweighted minimum-hop path.
