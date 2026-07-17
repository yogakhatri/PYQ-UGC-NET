# Question 75

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Performance Analysis and Recurrences · Time and Space Complexity*

SI. : 87025 In a the left and right subtrees for any given node, differ in height by more than one.

- **1.** Balanced Binary Tree
- **2.** Weight balanced binary tree
- **3.** Height balanced tree
- **4.** Binary Search Tree

> [!TIP]
> **Correct answer: 3. Height balanced tree**

## Solution

The intended sentence is that left and right subtree heights do not differ by more than one. That is the defining balance condition of a height-balanced (AVL-style) tree.

## Key Points

- Height balance requires |height(left)−height(right)|≤1 at every node.

## Why the other options are incorrect

A generic BST need not be balanced; ‘balanced binary tree’ is less precise, and weight balance compares subtree sizes/weights rather than heights.
