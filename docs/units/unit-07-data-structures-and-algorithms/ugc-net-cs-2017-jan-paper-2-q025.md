# Question 25

*UGC NET CS · 2017 Jan Paper 2 · Graph and Tree Algorithms · Connected Components and Tree Reconstruction*

Which of the following statements is false ? (A) Optimal binary search tree construction can be performed efficiently using dynamic programming. (B) Breadth-first search cannot be used to find connected components of a graph. (C) Given the prefix and postfix walks of a binary tree, the tree cannot be re-constructed uniquely. (D) Depth-first-search can be used to find the connected components of a graph.

- **1.** A
- **2.** B
- **3.** C
- **4.** D

> [!TIP]
> **Correct answer: 2. B**

## Solution

Statement B is false. To find connected components, start BFS from any unvisited vertex, mark every reached vertex as one component, and repeat from another unvisited vertex until none remain. Thus BFS works perfectly well. A is true because optimal-BST construction has a standard dynamic-programming solution. C is true for a general binary tree because preorder plus postorder does not uniquely locate a single child as left or right. D is true because the same repeated-search method works with DFS.

## Key Points

- Both BFS and DFS can enumerate connected components; the traversal strategy changes the exploration order, not reachability.

## Why the other options are incorrect

A, C, and D are true statements, so selecting them would not answer 'which is false.' The qualification 'general binary tree' matters for C; additional restrictions such as every internal node having two children can restore uniqueness.
