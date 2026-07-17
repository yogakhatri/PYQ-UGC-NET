# Question 79

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Structures · Deletion from a Singly Linked List*

In a singly linked list, what is the worst-case time complexity of the best-known algorithm to delete node a when a pointer q to that node is given?

- **1.** O(n log n)
- **2.** O(n)
- **3.** O(log n)
- **4.** O(1)

> [!TIP]
> **Correct answer: 2. O(n)**

## Solution

If q points to a non-tail node, one can copy the successor’s data into q and bypass the successor in O(1). But worst-case analysis must include q pointing to the final node. A singly linked node has no pointer to its predecessor, so deleting the tail requires traversing from the head to find the preceding node, which takes Θ(n). Therefore the best algorithm’s worst-case time is O(n), option 2.

## Key Points

- A pointer to a singly linked node does not reveal its predecessor; the tail case determines the worst-case deletion cost.

## Why the other options are incorrect

O(1) is valid only under the extra promise that q is not the tail (or that a predecessor pointer is supplied). O(log n) and O(n log n) do not match sequential traversal in a singly linked list.
