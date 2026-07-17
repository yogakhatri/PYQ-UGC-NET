# Question 25

*UGC NET CS · 2010 June Paper 2 · Performance Analysis and Recurrences · Time and Space Complexity*

In a B tree of order 5, the following keys are inserted as follows : 7, 8, 1, 4, 13, 20, 2, 6 and 5 How many elements are present in the root of the tree ?

- **A.** 1
- **B.** 2
- **C.** 3
- **D.** 4

> [!TIP]
> **Correct answer: B. 2**

## Solution

For order 5, a node holds at most four keys. Insert 7,8,1,4; inserting 13 overflows [1,4,7,8,13], so promote 7, leaving [1,4] and [8,13]. Insert 20 on the right. Insert 2,6 on the left; inserting 5 overflows [1,2,4,5,6], so promote 4. The root becomes [4,7], containing two elements.

## Key Points

- An order-m B-tree has at most m children and m−1 keys per node; promote the median on overflow.

## Why the other options are incorrect

Counts 1,3,4 result from omitting the second split, promoting the wrong key, or confusing key count with child count.
