# Question 4

*UGC NET CS · 2013 Dec Paper 3 · Software Testing · Flow-Graph Cyclomatic Complexity*

Given a flow graph with 10 nodes, 13 edges and one connected component, what are the number of regions and predicate (decision) nodes?

- **A.** 4, 5
- **B.** 5, 4
- **C.** 3, 1
- **D.** 13, 8

> [!TIP]
> **Correct answer: B. 5, 4**

## Solution

For a connected flow graph, cyclomatic complexity is V=E-N+2=13-10+2=5. This equals the number of regions, including the outside region. For a connected structured flow graph V=P+1, where P is the number of predicate nodes, so P=4. The pair is 5 regions and 4 predicates.

## Key Points

- Connected flow graph: V=E-N+2=regions=predicate nodes+1.

## Why the other options are incorrect

The other pairs fail either the edge-node formula or V=P+1. A reverses the correct quantities; C and D do not match the graph's cyclomatic complexity.
