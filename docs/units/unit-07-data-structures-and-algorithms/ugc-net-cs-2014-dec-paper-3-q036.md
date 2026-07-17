# Question 36

*UGC NET CS · 2014 Dec Paper 3 · Data Structures · Binary-Search-Tree Search-Path Constraints*

Suppose that we have numbers between 1 and 1000 in a binary search tree and we want to search for the number 365. Which of the following sequences could not be the sequence of nodes examined ?

- **A.** 4, 254, 403, 400, 332, 346, 399, 365
- **B.** 926, 222, 913, 246, 900, 260, 364, 365
- **C.** 927, 204,913, 242, 914, 247, 365
- **D.** 4, 401, 389, 221, 268, 384, 383, 280, 365

> [!TIP]
> **Correct answer: C. 927, 204,913, 242, 914, 247, 365**

## Solution

During a BST search for 365, every comparison narrows an allowable interval. In C, after 927 the key must be below 927; after 204 it must be above 204; after visiting 913 (>365), every later node on the path must lie below 913. The next values 242 and then 914 are impossible because 914 is outside the current interval (242,913). Hence C cannot be a search path.

## Key Points

- Validate a BST search path by maintaining one interval, not merely by comparing each adjacent pair.

## Why the other options are incorrect

A, B, and D always keep the next node inside the current lower and upper bounds: a node below 365 raises the lower bound, while a node above 365 lowers the upper bound. Their irregular-looking rises and falls are still compatible with different left/right subtrees. Only C violates an inherited ancestor bound.
