# Question 36

*UGC NET CS · 2013 Dec Paper 2 · Graph Theory · Edges in a Forest*

How many edges are there in a forest of t-trees containing a total of n vertices ?

- **A.** n + t
- **B.** n – t
- **C.** n ∗ t
- **D.** n t

> [!TIP]
> **Correct answer: B. n – t**

## Solution

Each tree with n_i vertices has n_i-1 edges. A forest of t disjoint trees with total vertices n has Σ(n_i-1)=Σn_i-t=n-t edges.

## Key Points

- A forest with n vertices and t connected components has exactly n-t edges.

## Why the other options are incorrect

Adding t has the wrong sign, multiplying n and t ignores tree structure, and n^t has no connection to edge counting. Each connected tree component contributes exactly one fewer edge than vertices.
