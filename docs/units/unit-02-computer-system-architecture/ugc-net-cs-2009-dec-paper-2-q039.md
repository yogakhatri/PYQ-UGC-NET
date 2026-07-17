# Question 39

*UGC NET CS · 2009 Dec Paper 2 · Memory Hierarchy · Associative Memory*

A program is located in the smallest available hole in t he memory is _________

- **A.** best – fit
- **B.** first – bit
- **C.** worst – fit
- **D.** buddy

> [!TIP]
> **Correct answer: A. best – fit**

## Solution

Best-fit allocation searches the free holes and chooses the smallest hole large enough for the request. This leaves the least immediate unused remainder in the selected hole.

## Key Points

- Best fit means the smallest adequate free block.

## Why the other options are incorrect

First-fit uses the first sufficient hole; worst-fit uses the largest; buddy allocation chooses power-of-two blocks through splitting/coalescing.
