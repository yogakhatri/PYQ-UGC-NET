# Question 8

*UGC NET CS · 2012 June Paper 2 · Data Structures · Binary Search Tree Properties*

A binary search tree is a binary tree :

- **A.** All items in the left subtree are less than root
- **B.** All items in the right subtree are greater than or equal to the root
- **C.** Each subtree is itself a binary search tree
- **D.** All of the above COMPUTER SCIENCE AND APPLICATIONS Paper – II Note : This paper contains fifty (50) objective type questions, each question carrying two (2) marks. Attempt all the questions. www.solutionsadda.in

> [!TIP]
> **Correct answer: D. All of the above COMPUTER SCIENCE AND APPLICATIONS Paper – II Note : This paper contains fifty (50) objective type questions, each question carrying two (2) marks. Attempt all the questions. www.solutionsadda.in**

## Solution

A binary search tree satisfies an ordering invariant at every node: keys in the left subtree are less than the node key, keys in the right subtree are greater (or greater than/equal under the duplicate convention stated), and each subtree recursively satisfies the same rule. Thus statements A, B and C jointly define the BST used by the question.

## Key Points

- BST ordering is recursive: left keys smaller, right keys larger according to the duplicate policy, and both subtrees are BSTs.

## Why the other options are incorrect

Each of A-C states only part of the recursive invariant. Selecting one alone would allow a tree that violates another required side or whose descendants are not themselves correctly ordered.
