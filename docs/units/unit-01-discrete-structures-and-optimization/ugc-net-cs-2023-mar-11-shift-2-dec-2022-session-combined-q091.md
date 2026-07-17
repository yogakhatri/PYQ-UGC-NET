# Question 91

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Graph Theory · Simple Graph*

Consider the following statements: P: There exists no simple, undirected and connected graph with 80 vertices and 77 edges. Q: All vertices of Euler graph are of even degree. R: Every simple, undirected, connected and acyclic graph with 50 vertices has at least two vertices of degree one. S: There exits a bipartite graph with more than ten vertices which is 2-colorable. What is the number of correct statements among the above statements.

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: 4. 4**

## Solution

P is true because a connected graph on 80 vertices needs at least 79 edges. Q is the Euler-circuit degree criterion. R is the standard theorem that every nontrivial tree has at least two leaves. S is true because bipartite graphs of arbitrarily many vertices exist and are 2-colorable. Therefore all four statements are correct.

## Key Points

- Use the minimum-edge bound n−1 for connected graphs and the leaf theorem for trees.

## Why the other options are incorrect

Options 1–3 undercount the true statements; none of P, Q, R, or S is false under the standard definitions.
