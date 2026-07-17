# Question 26

*UGC NET CS · 2018 July Paper 2 · Trees and Binary Trees · Full Binary Tree Node Identity*

A binary search tree in which every non-leaf node has non-empty left and r ight subtrees is called a strictly binary tree. Such a tree with 19 leaves :

- **1.** cannot have more than 37 nodes
- **2.** has exactly 37 nodes
- **3.** has exactly 35 nodes
- **4.** cannot have more than 35 nodes

> [!TIP]
> **Correct answer: No unique answer: a strict binary tree with 19 leaves has exactly 37 nodes, so both options 1 and 2 are true.**

## Solution

In a strict/full binary tree, every internal node has two children. If I is the number of internal nodes and L the number of leaves, counting edges gives 2I=I+L−1, hence L=I+1. With L=19, I=18 and total nodes I+L=37. Therefore option 2 is the exact result—but option 1 ('cannot have more than 37') is also logically true.

## Key Points

- For every nonempty full binary tree: leaves = internal nodes + 1, and total nodes = 2×leaves−1.

## Why the other options are incorrect

Options 3 and 4 use 35, which violates the full-binary-tree identity. An intended single-answer key will choose option 2 because it is the strongest statement, but the presence of the weaker true option 1 makes the MCQ defective.
