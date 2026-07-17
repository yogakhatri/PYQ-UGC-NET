# Question 145

*UGC NET CS · 2019 Dec Paper 1 And 2 · Software Testing · Flow Graphs and Basis-Path Testing*

How many predicate nodes are there and what are their names?

- **1.** Three: 1, (2,3), 6
- **2.** Three: 1, 4, 6
- **3.** Four: (2,3), 6, 10, 11
- **4.** Four: (2,3), 6, 9, 10

> [!TIP]
> **Correct answer: 1. Three: 1, (2,3), 6**

## Solution

A predicate node is a decision point with more than one outgoing edge. Node 1 branches either to the body node (2,3) or to exit 11. Node (2,3) branches to node 6 or node (4,5). Node 6 branches to node 7 or node 8. Every other node has exactly one outgoing edge, even if it has multiple incoming edges. Therefore the three predicate nodes are 1, (2,3), and 6, giving option 1.

## Key Points

- Predicate node = outdegree greater than one, not indegree greater than one.

## Why the other options are incorrect

Option 2 names 4, which is only a statement label within node (4,5), not a branching node. Options 3 and 4 treat merge or exit nodes such as 9, 10, or 11 as predicates; multiple incoming edges do not make a decision node.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2019-dec-flowgraph-q141-q145.png)
