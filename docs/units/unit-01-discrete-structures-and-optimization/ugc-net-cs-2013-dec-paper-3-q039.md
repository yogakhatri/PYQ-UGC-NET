# Question 39

*UGC NET CS · 2013 Dec Paper 3 · Graph Theory · Cliques and Vertex Covers*

A _________ complete subgraph and a _________ subset of vertices of a graph G = (V, E) ar e a clique and a vertex cover respectively.

- **A.** minimal, maximal
- **B.** minimal, minimal
- **C.** maximal, maximal
- **D.** maximal, minimal

> [!TIP]
> **Correct answer: D. maximal, minimal**

## Solution

In the terminology intended by this question, a clique is a maximal complete subgraph: it is complete and cannot be enlarged by adding another adjacent vertex. A minimal vertex cover covers every edge, but removing any one of its vertices would leave some edge uncovered. Hence the blanks are maximal and minimal.

## Key Points

- Maximal means cannot be enlarged; minimal means no element can be removed while preserving the property.

## Why the other options are incorrect

A and B incorrectly call the complete subgraph minimal. C incorrectly calls the vertex cover maximal; adding vertices preserves the cover property but does not express the economical irredundancy normally required here. Note that some modern texts call every complete vertex subset a clique and reserve 'maximal clique' for the inclusion-maximal case; the exam is using the stricter wording in its blank.
