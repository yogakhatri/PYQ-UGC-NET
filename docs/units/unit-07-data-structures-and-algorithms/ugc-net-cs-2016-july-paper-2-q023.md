# Question 23

*UGC NET CS · 2016 July Paper 2 · Trees and Binary Trees · Maximum Height of a Full Binary Tree*

A full binary tree has n nodes, and every node has either zero or two children. If height is counted in edges, what is its maximum possible height?

- **1.** n/2 − 1
- **2.** n/2 + 1
- **3.** (n – 1)/2
- **4.** (n + 1)/2

> [!TIP]
> **Correct answer: 3. (n – 1)/2**

## Solution

Let I be the number of internal nodes in a full binary tree. Every internal node has two children, so the number of leaves is I+1 and n=I+(I+1)=2I+1; hence I=(n−1)/2. To maximize height, arrange the internal nodes along one root-to-leaf spine, giving one edge of height per internal node. Maximum height is therefore (n−1)/2 edges.

## Key Points

- Full binary tree: leaves=internal+1 and total nodes=2·internal+1.

## Why the other options are incorrect

The alternatives do not match the full-tree node identity n=2I+1. If height were counted as the number of vertices on the longest path rather than edges, it would be (n+1)/2; the source and standard data-structure convention here count edges, making option 3 correct.
