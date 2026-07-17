# Question 45

*UGC NET CS · 2014 Dec Paper 2 · Software Testing · Cyclomatic Complexity*

Which one of the following is used to compute cyclomatic complexity ?

- **A.** The number of regions – 1
- **B.** E – N + 1, where E is the number of flow graph edges and N is the number of flow graph nodes.
- **C.** P – 1, where P is the number of predicate nodes in the flow graph G.
- **D.** P + 1, where P is the number of predicate nodes in the flow graph G.

> [!TIP]
> **Correct answer: D. P + 1, where P is the number of predicate nodes in the flow graph G.**

## Solution

For a connected control-flow graph, cyclomatic complexity can be computed as V(G)=E−N+2, as the number of regions in a planar drawing, or as P+1 when every predicate node is binary. Among the offered formulas, only P+1 is correct.

## Key Points

- Equivalent connected-flow-graph formulas: V=E−N+2=regions=P+1.

## Why the other options are incorrect

A should be the number of regions, not regions−1. B is missing one from E−N+2. C should add one to the predicate count rather than subtract one.
