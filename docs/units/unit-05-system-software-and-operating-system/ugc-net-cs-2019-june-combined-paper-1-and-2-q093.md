# Question 93

*UGC NET CS · 2019 June Paper 1 And 2 · Memory Management · LRU and optimal page replacement*

A process has been allocated 3 frames and has the page-reference sequence 1, 2, 1, 3, 7, 4, 5, 6, 3, 1. What is the difference in the number of page faults using LRU and optimal page replacement?

- **1.** 2
- **2.** 0
- **3.** 1
- **4.** 3

> [!TIP]
> **Correct answer: 1. 2**

## Solution

With three frames, LRU faults on 1,2,3,7,4,5,6,3,1; only the second reference to 1 is a hit, so LRU has 9 faults. Optimal replacement faults on 1,2,3,7,4,5,6 and then keeps 3 and 1 for their future references, giving 7 faults. The difference is 9-7=2.

## Key Points

- Simulate each policy independently; optimal evicts the page whose next use is farthest in the future or never occurs.

## Why the other options are incorrect

Options 2–4 do not match the two complete simulations. Optimal can use future knowledge and therefore saves two faults relative to LRU here.
