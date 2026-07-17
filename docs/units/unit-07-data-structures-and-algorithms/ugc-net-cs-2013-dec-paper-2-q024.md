# Question 24

*UGC NET CS · 2013 Dec Paper 2 · Data Structures · B-Tree Minimum-Degree Bounds*

For any B-tree of minimum degree t ≥ 2, every node other than the root must have atleast ________ keys and every node can have at most ________ keys.

- **A.** t – 1, 2t + 1
- **B.** t + 1, 2t + 1
- **C.** t – 1, 2t – 1
- **D.** t + 1, 2t – 1

> [!TIP]
> **Correct answer: C. t – 1, 2t – 1**

## Solution

For a B-tree of minimum degree t, every non-root node contains at least t-1 keys. A node can contain at most 2t-1 keys; if another key must be inserted, the full node is split. Correspondingly, an internal node has between t and 2t children, except for the root's special lower bound.

## Key Points

- Minimum-degree-t B-tree bounds: non-root keys t-1 through 2t-1; children t through 2t.

## Why the other options are incorrect

The maximum 2t+1 is too high, and t+1 is not the minimum key count. The defining occupancy interval for non-root nodes is [t-1, 2t-1].
