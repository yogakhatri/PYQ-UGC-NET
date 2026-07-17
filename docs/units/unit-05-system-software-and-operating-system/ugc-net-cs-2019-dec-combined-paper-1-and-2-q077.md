# Question 77

*UGC NET CS · 2019 Dec Paper 1 And 2 · Memory Management · TLB Effective Access Time*

Consider a paging system where translation look aside buffer (TLB) a special type of associative memory is used with hit ratio of 80%. Assume that memory reference takes 80 nanoseconds and reference time to TLB is 20 nanoseconds. What will be the effective memory access time given 80% hit ratio?

- **1.** 110 nanoseconds
- **2.** 116 nanoseconds
- **3.** 200 nanoseconds
- **4.** 100 nanoseconds

> [!TIP]
> **Correct answer: 2. 116 nanoseconds**

## Solution

On a TLB hit, translation lookup plus one memory access costs 20+80=100 ns. On a miss, the system spends 20 ns checking the TLB, 80 ns reading the page-table entry, and 80 ns accessing the desired word: 180 ns. The weighted average is 0.8×100+0.2×180=80+36=116 ns. Thus option 2.

## Key Points

- EAT = hit ratio × hit cost + miss ratio × miss cost, with a miss requiring both page-table and data memory accesses.

## Why the other options are incorrect

One hundred ns is only the hit time and ignores the 20% misses. Two hundred ns overcounts the miss path. One hundred ten ns does not follow from the stated 80/20 weighting. The miss probability must be included even with a high hit ratio.
