# Question 58

*UGC NET CS · 2018 July Paper 2 · Memory Management · LRU Page Replacement*

Consider a virtual page reference string 1, 2, 3, 2, 4, 2, 5, 2, 3, 4. Suppose LRU page replacement algorithm is implemented with 3 page frames in main memory. Then the num ber of page faults are_________.

- **1.** 5
- **2.** 7
- **3.** 9
- **4.** 10

> [!TIP]
> **Correct answer: 2. 7**

## Solution

With three empty frames, references 1, 2, and 3 cause the first three faults; the next 2 is a hit. Reference 4 faults and evicts least-recently-used page 1. Reference 2 is a hit. Reference 5 faults and evicts page 3. Reference 2 is a hit. Reference 3 faults and evicts page 4; finally 4 faults and evicts page 5. The fault sequence is 1,2,3,4,5,3,4: seven faults, option 2.

## Key Points

- LRU evicts the resident page whose most recent reference is farthest in the past.

## Why the other options are incorrect

Five counts only the distinct page numbers and ignores reloads of 3 and 4. Nine or ten incorrectly count one or more hits on page 2 as faults. Under LRU, update recency on every reference, including hits.
