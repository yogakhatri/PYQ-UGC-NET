# Question 33

*UGC NET CS · 2017 Jan Paper 3 · Data Structures · Red-Black Tree Worst-Case Operations*

Red-black trees are one of many search tree schemes that are “balanced” in order to guarantee that basic dynamic-set operations take ________ time in the worst case.

- **1.** O(1)
- **2.** O(lg n)
- **3.** O(n)
- **4.** O(n lg n)

> [!TIP]
> **Correct answer: 2. O(lg n)**

## Solution

Red-black invariants keep the longest root-to-leaf path at most twice the shortest, which bounds the height of an n-node tree by O(lg n). Search follows one root-to-leaf path, while insertion and deletion use a path plus only constant work per visited level for recoloring and rotations. Therefore the basic dynamic-set operations take O(lg n) worst-case time, option 2.

## Key Points

- Balanced height O(lg n) makes search, insertion, and deletion O(lg n) per operation.

## Why the other options are incorrect

O(1) is impossible for arbitrary key search in an ordered comparison tree. O(n) is the possible height of an unbalanced BST, which red-black balancing prevents. O(n lg n) describes larger batch costs, not one operation.
