# Question 16

*UGC NET CS · 2012 Dec Paper 2 · Data Structures · AVL Balance*

In which tree, for every node, do the heights of its left and right subtrees differ by at most one?

- **1.** Binary search tree
- **2.** AVL tree
- **3.** Threaded binary tree
- **4.** Complete binary tree

> [!TIP]
> **Correct answer: 2. AVL tree**

## Solution

An AVL tree is a self-balancing binary search tree. For every node it maintains |height(left)-height(right)| <= 1. After insertion or deletion, rotations restore this condition, keeping the overall height logarithmic.

## Key Points

- AVL means a binary search tree with balance factor -1, 0 or +1 at every node.

## Why the other options are incorrect

A general binary search tree has no height-balance guarantee. Threading replaces null links with traversal links and does not impose this height condition. A complete binary tree has a level-filling shape property, which is different from the local AVL balance-factor rule.
