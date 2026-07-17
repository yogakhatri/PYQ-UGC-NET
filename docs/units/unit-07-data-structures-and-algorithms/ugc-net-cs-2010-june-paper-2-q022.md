# Question 22

*UGC NET CS · 2010 June Paper 2 · Data Structures · Priority Queues*

What is the most appropriate data structure to implement a priority queue ?

- **A.** Heap
- **B.** Circular array
- **C.** Linked list
- **D.** Binary tree

> [!TIP]
> **Correct answer: A. Heap**

## Solution

A binary heap supports insertion and removal of the highest/lowest-priority element in O(log n), while inspecting that element is O(1). It is compact and is the standard efficient priority-queue implementation.

## Key Points

- Heap order keeps the extreme-priority item at the root while preserving logarithmic updates.

## Why the other options are incorrect

An unsorted array/list makes deletion of the best element linear; a sorted list makes insertion linear. An arbitrary binary tree gives no priority guarantee, whereas a heap is the specifically constrained tree needed.
