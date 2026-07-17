# Question 39

*UGC NET CS · 2013 Dec Paper 2 · Graph Theory · Kuratowski's Planarity Theorem*

A graph is non-planar if and only if it contains a subgraph homomorphic to

- **A.** K 3, 2 or K5
- **B.** K 3, 3 and K6
- **C.** K 3, 3 or K5
- **D.** K 2, 3 and K5

> [!TIP]
> **Correct answer: C. K 3, 3 or K5**

## Solution

Kuratowski's theorem states that a finite graph is non-planar exactly when it contains a subdivision, or a subgraph homeomorphic to, K5 or K3,3. Subdividing edges adds degree-2 vertices without changing the underlying obstruction to planarity.

## Key Points

- The two Kuratowski obstructions are K5 and K3,3.

## Why the other options are incorrect

K3,2 and K2,3 are planar complete bipartite graphs. K6 is non-planar but is not one of the two minimal homeomorphic obstructions named by the theorem. The condition uses 'or', because either obstruction suffices.
