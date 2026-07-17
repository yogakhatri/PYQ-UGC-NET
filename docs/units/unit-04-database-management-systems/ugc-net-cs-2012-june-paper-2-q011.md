# Question 11

*UGC NET CS · 2012 June Paper 2 · Database Indexing · B+ Tree Disk Access*

B+ tree are preferred to binary tree in Database because

- **A.** Disk capacity are greater than memory capacities
- **B.** Disk access is much slower than memory access
- **C.** Disk data transfer rates are much less than memory data transfer rate
- **D.** Disks are more reliable than memory

> [!TIP]
> **Correct answer: B. Disk access is much slower than memory access**

## Solution

Database indexes are typically much larger than RAM and reside on block storage. A B+ tree has high fan-out because one disk page holds many separator keys and child pointers, so its height is small and a lookup needs only a few page accesses. This matters chiefly because a random disk access has far greater latency than a main-memory access.

## Key Points

- B+ trees trade a high branching factor for very few slow disk-page accesses.

## Why the other options are incorrect

Large disk capacity explains why data is stored there but not why B+ trees outperform binary trees. Lower transfer rate is less central than per-access latency and the number of I/Os. Disk reliability is not the reason and is not generally greater than volatile memory reliability.
