# Question 24

*UGC NET CS · 2009 Dec Paper 2 · Data Structures · Binary Search*

With regard to linked list, which of the following stateme nt is false ?

- **A.** An algorithm to search for an element in a singly linked li st requires 0(n) operations in the worst case.
- **B.** An algorithm for deleting the first element in a singly linked list requires 0(n) operations in the worst case.
- **C.** An algorithm for finding the maximum value in a circular li nked list requires 0(n) operations.
- **D.** An algorithm for deleting the middle node of a circular li nked list requires 0(n) operations.

> [!TIP]
> **Correct answer: B. An algorithm for deleting the first element in a singly linked list requires 0(n) operations in the worst case.**

## Solution

Deleting the first node of a singly linked list requires only changing the head pointer (and freeing the old node), so it is Θ(1), not Θ(n). Therefore statement B is false.

## Key Points

- Head insertion/deletion is constant time; position/value discovery generally requires traversal.

## Why the other options are incorrect

Searching an unsorted list and finding a maximum require a full Θ(n) traversal. Finding/deleting an unspecified middle node also requires Θ(n) traversal unless a direct pointer is supplied.
