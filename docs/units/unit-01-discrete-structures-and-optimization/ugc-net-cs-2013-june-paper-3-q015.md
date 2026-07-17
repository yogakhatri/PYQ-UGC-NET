# Question 15

*UGC NET CS · 2013 June Paper 3 · Graph Theory · Vertex Cover*

A vertex cover of an undirected graph G(V, E) is a subset V 1 ⊆ V vertices such that

- **A.** Each pair of vertices in V 1 is connected by an edge
- **B.** If (u, v) ∈ E then u ∈ V1 and v ∈ V1
- **C.** If (u, v) ∈ E then u ∈ V 1 or v ∈ V1
- **D.** All pairs of vertices in V 1 are not connected by an edge

> [!TIP]
> **Correct answer: C. If (u, v) ∈ E then u ∈ V 1 or v ∈ V1**

## Solution

A vertex cover V1 must touch every edge. Formally, for each edge (u,v) in E, at least one endpoint belongs to V1: u∈V1 or v∈V1. The inclusive 'or' allows both endpoints to be selected but requires at least one.

## Key Points

- Vertex cover: every edge has at least one selected endpoint; independent set is its complementary viewpoint.

## Why the other options are incorrect

A defines a clique-like property among selected vertices and says nothing about covering every graph edge. B unnecessarily requires both endpoints of every edge, which would usually force nearly all nonisolated vertices into the cover. D describes an independent-set-like condition, not edge coverage.
