# Question 22

*UGC NET CS · 2013 Dec Paper 2 · Data Structures · Linked-Queue Enqueue Pointers*

If a queue is implemented with a linked list using front and rear pointers, which pointer changes during insertion into a non-empty queue?

- **A.** Neither pointer changes
- **B.** Only the front pointer changes
- **C.** Only the rear pointer changes
- **D.** Both pointers change

> [!TIP]
> **Correct answer: C. Only the rear pointer changes**

## Solution

In a non-empty linked queue, front already points to the oldest node and remains unchanged during enqueue. The new node is linked after the current rear, and rear is updated to point to that new last node. Therefore only the rear pointer changes.

## Key Points

- Enqueue into non-empty linked queue updates rear; enqueue into empty queue initializes both front and rear.

## Why the other options are incorrect

Neither pointer changing would make the new last node inaccessible through rear. Changing only front would incorrectly alter the deletion end. Both pointers change only when inserting into an empty queue, where the first node is simultaneously front and rear.
