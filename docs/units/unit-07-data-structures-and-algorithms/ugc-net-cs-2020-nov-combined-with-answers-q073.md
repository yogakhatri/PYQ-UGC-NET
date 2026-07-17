# Question 73

*UGC NET CS · 2020 Nov With Answers · Trees · Full n-ary Tree Node Counts*

In a full n-ary tree, every node has either n children or none. If the tree has I=10 internal nodes and L=41 leaves, what is n?

- **1.** 3
- **2.** 4
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 3. 5**

## Solution

A full n-ary tree with I internal nodes has nI edges because every internal node contributes n child edges. It has I+L total vertices, and every tree has one fewer edge than vertices: nI=I+L−1. Rearranging gives L=(n−1)I+1. Substitute L=41 and I=10: 41=10(n−1)+1, so 40=10(n−1), n−1=4, and n=5. Hence option 3.

## Key Points

- Full n-ary tree identity: L=(n−1)I+1, derived by equating nI edges with I+L−1.

## Why the other options are incorrect

Substituting n=3,4,6 would produce 21,31,51 leaves, respectively. The relation is not L=nI because one incoming edge links each nonroot vertex.
