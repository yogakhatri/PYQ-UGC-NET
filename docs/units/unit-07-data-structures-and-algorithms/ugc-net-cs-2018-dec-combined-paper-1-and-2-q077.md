# Question 77

*UGC NET CS · 2018 Dec Paper 1 And 2 · Graph Algorithms · Standard Graph-Algorithm Complexities*

Match each graph algorithm with the listed time complexity: (a) Dijkstra’s algorithm; (b) Kruskal’s algorithm; (c) Floyd–Warshall algorithm; (d) topological sorting. Complexities: (i) O(E lg E); (ii) Θ(V³); (iii) O(V²); (iv) Θ(V+E).

- **1.** (a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)
- **2.** (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)
- **3.** (a)-(i), (b)-(iii), (c)-(iv), (d)-(ii)
- **4.** (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)

> [!TIP]
> **Correct answer: 2. (a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)**

## Solution

With the implementations implied by the list: Dijkstra using an adjacency matrix/simple array selection is O(V²), so (a)→(iii). Kruskal sorts edges, giving O(E lg E), so (b)→(i). Floyd–Warshall has three nested vertex loops, Θ(V³), so (c)→(ii). Topological sorting by DFS or Kahn’s algorithm visits each vertex and edge once, Θ(V+E), so (d)→(iv). The matching is option 2.

## Key Points

- Associate the dominant operation: Kruskal sorts edges, Floyd–Warshall scans all vertex triples, and topological sorting performs one graph traversal.

## Why the other options are incorrect

The other matchings assign a complexity to the wrong algorithm. Dijkstra can have other bounds with different data structures, but O(V²) is the listed standard bound and is the only consistent match here.
