# Question 59

*UGC NET CS · 2013 June Paper 3 · Memory Management · FIFO and LRU Page Replacement*

A job has four pages A, B, C, D and the main memory has two page frames only. The job needs to process its pages in following order : ABACABDBACD Assuming that a page interrupt occurs when a new page is brought in the main memory, irrespective of whether the page is swapped out or not. The number of page interrupts in FIFO and LRU page replacement algorithms are

- **A.** 9 and 7
- **B.** 7 and 6
- **C.** 9 and 8
- **D.** 8 and 6

> [!TIP]
> **Correct answer: C. 9 and 8**

## Solution

Trace ABACABDBACD with two empty frames. FIFO faults on A,B,C,A,B,D,A,C,D: 9 interrupts; hits occur only on the third A and the second B. LRU retains the most recently used page and faults on A,B,C,B,D,A,C,D: 8 interrupts; it also hits on the fifth A. Hence the FIFO/LRU pair is 9 and 8.

## Key Points

- FIFO evicts the oldest loaded page; LRU evicts the page whose most recent reference is oldest—trace them separately.

## Why the other options are incorrect

A undercounts LRU by one, B undercounts both algorithms, and D undercounts FIFO and LRU. Initial loads count as page interrupts because each brings a new page into memory, exactly as the question states.
