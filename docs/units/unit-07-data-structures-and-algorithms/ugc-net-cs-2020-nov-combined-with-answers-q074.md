# Question 74

*UGC NET CS · 2020 Nov With Answers · Heaps · Minimum Search in a Max-Heap*

In a binary max-heap containing n numbers, the smallest element can be found in what asymptotic time?

- **1.** O(n)
- **2.** O(log₂ n)
- **3.** O(1)
- **4.** O(log₂ log₂ n)

> [!TIP]
> **Correct answer: 1. O(n)**

## Solution

A max-heap guarantees only that each parent is at least as large as its children. Therefore the minimum cannot be an internal node with children; it must be among the leaves. A binary heap has about n/2 leaves, and their internal order is unconstrained, so finding the smallest requires scanning all of them in the worst case. This takes Θ(n), represented by O(n) in option 1.

## Key Points

- In a max-heap, maximum is at the root; minimum may be any leaf, so scan Θ(n) leaf candidates.

## Why the other options are incorrect

O(1) applies to finding the maximum at the root, not the minimum. Heap height O(log n) helps restore heap order along one path, but does not identify which of Θ(n) leaves is smallest. The double-log bound has no supporting property.
