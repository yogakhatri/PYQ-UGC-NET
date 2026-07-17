# Question 31

*UGC NET CS · 2015 June Paper 3 · Graph Algorithms · Floyd-Warshall All-Pairs Shortest Paths*

An all-pairs shortest-paths problem is efficiently solved using :

- **1.** Dijkstra's algorithm
- **2.** Bellman-Ford algorithm
- **3.** Kruskal algorithm
- **4.** Floyd-Warshall algorithm

> [!TIP]
> **Correct answer: 4. Floyd-Warshall algorithm**

## Solution

Floyd-Warshall is designed for all-pairs shortest paths. It uses dynamic programming: after considering vertices 1 through k as possible intermediates, it updates `d[i][j] = min(d[i][j], d[i][k] + d[k][j])`. Three nested vertex loops give `Θ(V^3)` time and a complete distance matrix.

## Key Points

- Floyd-Warshall solves all-pairs shortest paths by allowing intermediate vertices one by one.

## Why the other options are incorrect

Dijkstra and Bellman-Ford are single-source algorithms; they can be repeated for every source but are not the direct all-pairs method intended. Kruskal constructs a minimum spanning tree, which minimizes total tree weight and does not preserve every pair's shortest path.
