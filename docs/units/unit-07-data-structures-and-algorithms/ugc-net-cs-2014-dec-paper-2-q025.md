# Question 25

*UGC NET CS · 2014 Dec Paper 2 · Trees · Full Binary Tree Node Count*

A full binary tree with n leaves contains

- **A.** n nodes
- **B.** log 2 n nodes
- **C.** 2n –1 nodes
- **D.** 2 n nodes

> [!TIP]
> **Correct answer: C. 2n –1 nodes**

## Solution

In a full binary tree every internal node has exactly two children. If I is the number of internal nodes and L=n is the number of leaves, counting edges gives 2I=I+L−1, so I=L−1=n−1. Total nodes are I+L=(n−1)+n=2n−1.

## Key Points

- Full binary tree invariant: leaves = internal nodes + 1, hence total = 2·leaves−1.

## Why the other options are incorrect

n counts only the leaves. log₂n would relate to height only for special balanced trees, not total nodes. 2^n grows exponentially and is not the full-tree identity.
