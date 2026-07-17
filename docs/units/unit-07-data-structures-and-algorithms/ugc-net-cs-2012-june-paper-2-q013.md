# Question 13

*UGC NET CS · 2012 June Paper 2 · Data Structures · B-Tree Balance*

Leaves of which of the following trees are at the same level ?

- **A.** Binary tree
- **B.** B-tree
- **C.** AVL-tree
- **D.** Expression tree

> [!TIP]
> **Correct answer: B. B-tree**

## Solution

A B-tree is height-balanced by definition: every leaf occurs at the same depth. Insertions split full nodes and can grow a new root; deletions borrow or merge nodes and can shrink the root, always preserving equal leaf depth.

## Key Points

- All root-to-leaf paths in a B-tree have the same length.

## Why the other options are incorrect

An arbitrary binary tree can have leaves at many depths. AVL trees bound the height difference of subtrees but do not require all leaves at exactly one level. An expression tree mirrors expression structure and may also be unbalanced.
