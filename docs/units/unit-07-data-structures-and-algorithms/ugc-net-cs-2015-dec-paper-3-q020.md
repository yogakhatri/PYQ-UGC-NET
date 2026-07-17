# Question 20

*UGC NET CS · 2015 Dec Paper 3 · Graph Algorithms · Shortest Paths*

Floyd-Warshall algorithm utilizes __________ to solve the all-pairs shortest paths problem on a directed graph in __________ time.

- **1.** Greedy algorithm, Θ(V^3)
- **2.** Greedy algorithm, Θ(V² log n)
- **3.** Dynamic programming, Θ(V^3)
- **4.** Dynamic programming, Θ(V² log n)

> [!TIP]
> **Correct answer: 3. Dynamic programming, Θ(V^3)**

## Solution

Floyd–Warshall uses dynamic programming. After iteration k, D_k[i,j] is the shortest i-to-j path whose allowed intermediate vertices are drawn from {1,…,k}. The update is D_k[i,j]=min(D_(k−1)[i,j], D_(k−1)[i,k]+D_(k−1)[k,j]). Three nested loops over k,i,j give Θ(V³) time.

## Key Points

- Floyd–Warshall: dynamic programming over allowed intermediate vertices, Θ(V³).

## Why the other options are incorrect

The method is not greedy, eliminating options 1 and 2. Its dense all-pairs recurrence evaluates V³ combinations rather than Θ(V² log n), eliminating option 4.
