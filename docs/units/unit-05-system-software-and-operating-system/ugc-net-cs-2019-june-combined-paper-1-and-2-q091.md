# Question 91

*UGC NET CS · 2019 June Paper 1 And 2 · Storage Management · SSTF disk scheduling*

Consider a disk system with 100 cylinders. Requests occur in the sequence 4, 34, 10, 7, 19, 73, 2, 15, 6, 20. Assuming the head is currently at cylinder 50, what is the time taken to satisfy all requests if it takes 1 ms to move to an adjacent cylinder and the shortest-seek-time-first policy is used?

- **1.** 357 ms
- **2.** 238 ms
- **3.** 276 ms
- **4.** 119 ms

> [!TIP]
> **Correct answer: 4. 119 ms**

## Solution

Under SSTF, always service the pending cylinder closest to the current head. Starting at 50, the order is 34, 20, 19, 15, 10, 7, 6, 4, 2, 73. The movements are 16+14+1+4+5+3+1+2+2+71=119 cylinders. At 1 ms per adjacent-cylinder movement, the total seek time is 119 ms.

## Key Points

- SSTF is greedy: after each request, recompute the nearest pending cylinder from the new head position.

## Why the other options are incorrect

The other totals arise from a different request order or from omitting the final long movement from cylinder 2 to cylinder 73.
