# Question 49

*UGC NET CS · 2013 June Paper 3 · Data Structures · Doubly Linked Lists and Deletion*

Suppose you want to delete the name that occurs before “Vivek” in an alphabetical listing. Which of the following data structures shall be most efficient for this operation ?

- **A.** Circular linked list
- **B.** Doubly linked list
- **C.** Linked list
- **D.** Dequeue

> [!TIP]
> **Correct answer: B. Doubly linked list**

## Solution

Once the node containing 'Vivek' is located, a doubly linked list gives direct access to its predecessor through the prev link. The node before Vivek can then be unlinked in constant time by updating the surrounding next and prev links. This makes predecessor deletion natural and efficient.

## Key Points

- Doubly linked lists support direct predecessor access and O(1) deletion once the target position is known.

## Why the other options are incorrect

A circular link only connects the end back to the beginning; it does not by itself give a backward link. A singly linked list cannot move directly from Vivek to its predecessor unless that predecessor was separately retained during traversal. A deque gives efficient deletion only at its two ends, not immediately before an arbitrary interior name.
