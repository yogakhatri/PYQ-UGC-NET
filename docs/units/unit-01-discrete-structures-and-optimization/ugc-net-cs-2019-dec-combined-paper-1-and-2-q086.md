# Question 86

*UGC NET CS · 2019 Dec Paper 1 And 2 · Graph Theory · Cliques and Complete Subgraphs*

A clique in an undirected graph G=(V,E) is a subset V'⊆V of vertices such that:

- **1.** If (u,v)∈E, then u∈V' and v∈V'
- **2.** If (u,v)∈E, then u∈V' or v∈V'
- **3.** Each pair of vertices in V' is connected by an edge
- **4.** All pairs of vertices in V' are not connected by an edge

> [!TIP]
> **Correct answer: 3. Each pair of vertices in V' is connected by an edge**

## Solution

A clique is a vertex subset V' whose induced subgraph is complete: for every two distinct vertices u,v in V', the edge (u,v) belongs to E. In plain words, every pair of vertices in V' is connected by an edge. That is option 3.

## Key Points

- Clique means pairwise adjacent; independent set means pairwise nonadjacent.

## Why the other options are incorrect

Options 1 and 2 try to infer membership in V' from arbitrary edges of the whole graph, which is not how a subset is defined. Option 4 describes the opposite extreme—an independent set, in which no two selected vertices are adjacent.
