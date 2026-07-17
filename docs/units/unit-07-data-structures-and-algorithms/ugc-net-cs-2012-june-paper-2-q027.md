# Question 27

*UGC NET CS · 2012 June Paper 2 · Data Structures · Binary Search Tree Traversal*

The Inorder traversal of the tree will yield a sorted listing of elements of tree in

- **A.** Binary tree
- **B.** Binary search tree
- **C.** Heaps
- **D.** None of the above

> [!TIP]
> **Correct answer: B. Binary search tree**

## Solution

Inorder traversal visits left subtree, node, then right subtree. In a binary search tree every left key is smaller and every right key is larger according to the duplicate convention. Recursive inorder traversal therefore emits keys in nondecreasing sorted order.

## Key Points

- BST ordering plus left-root-right traversal yields sorted keys.

## Why the other options are incorrect

An arbitrary binary tree has no ordering invariant. A heap guarantees only parent-child priority, not a sorted inorder sequence. Therefore 'none' is false.
