# Question 122

*UGC NET CS · 2018 Dec Paper 1 And 2 · Memory Management · FIFO Page Replacement*

For process P, the page-reference sequence is 1, 2, 4, 5, 2, 1, 2, 4. Main memory accommodates three pages and initially contains pages 1 and 2, in that FIFO order: 1 first, then 2. Using FIFO page replacement, how many page faults occur while completing the sequence?

- **1.** 4
- **2.** 3
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 3. 5**

## Solution

Initially the FIFO queue is [1,2] with one free frame. References 1 and 2 hit. Reference 4 faults and fills the free frame: [1,2,4] (fault 1). Reference 5 faults and evicts 1: [2,4,5] (fault 2). Reference 2 hits. Reference 1 faults and evicts 2: [4,5,1] (fault 3). Reference 2 faults and evicts 4: [5,1,2] (fault 4). Finally 4 faults and evicts 5: [1,2,4] (fault 5). There are five page faults, option 3.

## Key Points

- Under FIFO, hits do not change arrival order; replace only the page that has been resident longest.

## Why the other options are incorrect

Counts 3 or 4 usually result from incorrectly refreshing a page's FIFO age on a hit; FIFO does not do that. Six incorrectly counts an initial resident-page reference or another hit as a fault. Only absent-page references 4, 5, 1, 2, and 4 fault.
