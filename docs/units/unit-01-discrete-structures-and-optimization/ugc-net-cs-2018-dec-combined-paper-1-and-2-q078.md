# Question 78

*UGC NET CS · 2018 Dec Paper 1 And 2 · Graph Theory · Bipartite Graphs and Odd Cycles*

A K-colouring of an undirected graph G=(V,E) is a function c:V→{0,1,…,K−1} such that c(u)≠c(v) for every edge (u,v)∈E. For the equivalent characterizations involving two colours, which statement is not correct?

- **1.** G is bipartite
- **2.** G is 2-colorable
- **3.** G has cycles of odd length
- **4.** G has no cycles of odd length

> [!TIP]
> **Correct answer: 3. G has cycles of odd length**

## Solution

For an undirected graph, the following are equivalent: G is bipartite; G is 2-colourable; and G contains no odd-length cycle. Therefore options 1, 2, and 4 are correct descriptions of the same property. ‘G has cycles of odd length’ contradicts them and is the statement that is not correct, option 3.

## Key Points

- Bipartite ⇔ 2-colourable ⇔ no odd cycle.

## Why the other options are incorrect

Options 1, 2, and 4 should not be selected because each is a standard characterization of bipartiteness. During a two-colouring, traversing an odd cycle forces its last vertex to need both colours, which proves why odd cycles are forbidden.
