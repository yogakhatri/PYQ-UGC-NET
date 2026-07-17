# Question 23

*UGC NET CS · 2015 June Paper 2 · Trees · Level-Order Traversal*

Level order Traversal of a rooted Tree can be done by starting from root and performing :

- **1.** Breadth First Search
- **2.** Depth First Search
- **3.** Root Search
- **4.** Deep Search

> [!TIP]
> **Correct answer: 1. Breadth First Search**

## Solution

Level-order traversal visits all vertices at depth 0, then depth 1, then depth 2, and so on. Breadth-first search produces exactly this order by placing the root in a queue, removing one vertex at a time, and enqueuing its children. Therefore level order is breadth-first search.

## Key Points

- Level order is BFS on a rooted tree and is implemented with a queue.

## Why the other options are incorrect

Depth-first search follows one branch before returning, so it does not generally preserve level order. `Root search` and `deep search` are not standard traversal algorithms with the required queue-based behavior.
