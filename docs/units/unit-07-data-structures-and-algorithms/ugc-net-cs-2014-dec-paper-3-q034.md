# Question 34

*UGC NET CS · 2014 Dec Paper 3 · Graph Algorithms · Greedy and Dynamic-Programming Shortest Paths*

Dijkstra's algorithm, which solves the single-source shortest-path problem for nonnegative edge weights, is a ______, and the Floyd–Warshall algorithm, which finds shortest paths between all pairs of vertices, is a ______.

- **A.** Greedy algorithm, Divide-conquer algorithm
- **B.** Divide-conquer algorithm, Greedy algorithm
- **C.** Greedy algorithm, Dynamic programming algorithm
- **D.** Dynamic programming algorithm, Greedy algorithm

> [!TIP]
> **Correct answer: C. Greedy algorithm, Dynamic programming algorithm**

## Solution

Dijkstra's algorithm repeatedly commits the unvisited vertex with minimum tentative distance. With nonnegative edge weights, that locally best choice is safe, so the algorithm is greedy. Floyd–Warshall builds solutions by allowing intermediate vertices from an expanding set: Dᵏ[i,j]=min(Dᵏ⁻¹[i,j], Dᵏ⁻¹[i,k]+Dᵏ⁻¹[k,j]). Reusing these overlapping subproblem results is dynamic programming. The pair is therefore greedy, dynamic programming.

## Key Points

- Dijkstra commits a safe local minimum; Floyd–Warshall evaluates a recurrence over progressively allowed intermediate vertices.

## Why the other options are incorrect

A incorrectly calls Floyd–Warshall divide-and-conquer. B reverses both classifications. D reverses them as well. Dijkstra's extract-min choice and Floyd–Warshall's staged recurrence uniquely identify option C.
