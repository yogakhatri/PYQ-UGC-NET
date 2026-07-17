# Question 75

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Structures · Binary Search Tree Insertion*

A binary search tree is constructed by inserting, in order, 60, 25, 72, 15, 30, 68, 101, 13, 18, 47, 70, 34. How many nodes are in the left subtree of the root?

- **1.** 5
- **2.** 6
- **3.** 7
- **4.** 3

> [!TIP]
> **Correct answer: 3. 7**

## Solution

The first inserted key, 60, is the root. In a binary search tree, every later key smaller than 60 enters the root’s left subtree, regardless of its deeper parent. Those keys are 25,15,30,13,18,47,34—seven nodes. The keys 72,68,101,70 are on the right side. Hence option 3.

## Key Points

- For a BST with root r, every inserted key less than r belongs somewhere in the complete left subtree.

## Why the other options are incorrect

The other counts omit descendants below 25 or mistakenly count only immediate children/one level. The question asks for the entire left subtree, not merely the root’s left child or the children of node 25.
