# Question 36

*UGC NET CS · 2016 July Paper 2 · Virtual Memory · FIFO Page Replacement and Belady's Anomaly*

Consider the reference string 0 1 2 3 0 1 4 0 1 2 3 4 If FIFO page replacement algorithm is used, then the number of page faults with three page frames and four page frames are _______ and ______ respectively.

- **1.** 10, 9
- **2.** 9, 9
- **3.** 10, 10
- **4.** 9, 10

> [!TIP]
> **Correct answer: 4. 9, 10**

## Solution

Apply FIFO to 0,1,2,3,0,1,4,0,1,2,3,4. With three frames, the first seven references fault; 0 and 1 then hit; 2 and 3 fault; and the final 4 hits, for 9 faults. With four frames, 0,1,2,3 cause four faults; 0 and 1 hit; then 4,0,1,2,3,4 each replaces the oldest page and faults, for 10 faults. The answer is therefore (9,10), option 4.

## Key Points

- FIFO evicts the page loaded earliest and does not refresh a page's age on a hit.

## Why the other options are incorrect

The alternatives arise from treating FIFO as LRU or updating FIFO order on a hit. A hit does not move a page in the FIFO queue. This trace is also a classic Belady anomaly: increasing frames from 3 to 4 increases faults from 9 to 10.
