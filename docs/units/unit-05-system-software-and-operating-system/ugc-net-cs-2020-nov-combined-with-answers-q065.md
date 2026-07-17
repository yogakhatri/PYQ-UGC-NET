# Question 65

*UGC NET CS · 2020 Nov With Answers · Memory Management · FIFO and LRU Page Replacement*

A machine has three page frames and reference string ⟨A,B,C,D,A,B,E,A,B,C,D,E,B,A,B⟩. If P and Q are the page-fault counts under FIFO and LRU, respectively, what is (P,Q)?

- **1.** (11, 10)
- **2.** (12, 11)
- **3.** (10, 11)
- **4.** (11, 12)

> [!TIP]
> **Correct answer: 4. (11, 12)**

## Solution

Trace three frames through A,B,C,D,A,B,E,A,B,C,D,E,B,A,B. FIFO faults on A,B,C,D,A,B,E,C,D,B,A and hits the other four references, giving P=11. LRU faults on A,B,C,D,A,B,E,C,D,E,B,A; only the second A, second B, and final B are hits, giving Q=12. Therefore (P,Q)=(11,12), option 4.

## Key Points

- Maintain separate state rules: FIFO evicts earliest loaded, whereas LRU evicts least recently referenced.

## Why the other options are incorrect

The alternatives mis-handle hits when updating recency or incorrectly move a FIFO page to the back on a hit. FIFO replacement order changes only on a fault/insertion; LRU order changes on every reference.
