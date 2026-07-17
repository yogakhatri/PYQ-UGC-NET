# Question 111

*UGC NET CS · 2019 June Paper 1 And 2 · Graph Algorithms · Algorithm Running Times*

Match each algorithm with its running time. List I: (a) Prim's algorithm; (b) Dijkstra's algorithm; (c) Faster all-pairs shortest path; (d) Edmonds-Karp algorithm. List II: (i) O(V^3 log V); (ii) O(V E^2); (iii) O(E log V); (iv) O(V^2).

- **1.** a-ii, b-iv, c-i, d-iii
- **2.** a-iii, b-iv, c-i, d-ii
- **3.** a-ii, b-i, c-iv, d-iii
- **4.** a-iii, b-i, c-iv, d-ii

> [!TIP]
> **Correct answer: 2. a-iii, b-iv, c-i, d-ii**

## Solution

Match each algorithm with the standard implementation bound named in List II. Prim's algorithm with a binary heap takes O(E log V), so (a)-(iii). The array-based version of Dijkstra's algorithm takes O(V^2), so (b)-(iv). The faster all-pairs shortest-path method listed here takes O(V^3 log V), so (c)-(i). Edmonds-Karp performs O(VE) augmentations, each found by an O(E) breadth-first search, giving O(VE^2), so (d)-(ii). The matching is therefore a-iii, b-iv, c-i, d-ii.

## Key Points

- Memorize bounds together with their implementation assumptions: heap-based Prim O(E log V), array Dijkstra O(V^2), and Edmonds-Karp O(VE^2).

## Why the other options are incorrect

Every other option assigns at least one graph algorithm an incompatible bound. In particular, O(VE^2) identifies Edmonds-Karp, while O(E log V) identifies heap-based Prim; fixing those two already rules out options 1, 3 and 4.
