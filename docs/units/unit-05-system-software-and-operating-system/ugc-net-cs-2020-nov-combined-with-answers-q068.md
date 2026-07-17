# Question 68

*UGC NET CS · 2020 Nov With Answers · Memory Management · TLB Effective Access Time*

In a single-level paging system, the page table is in main memory. The TLB hit rate is 80%, a TLB lookup takes 15 ns, and one main-memory access takes 150 ns. What is the effective memory-access time?

- **1.** 185
- **2.** 195
- **3.** 205
- **4.** 175

> [!TIP]
> **Correct answer: 2. 195**

## Solution

A TLB hit costs one TLB lookup plus one memory access: 15+150=165 ns. A miss costs the lookup, one access to read the page-table entry, and one access to the desired word: 15+150+150=315 ns. Weight these by the 0.8 hit and 0.2 miss probabilities: EAT=0.8×165+0.2×315=132+63=195 ns. Therefore option 2.

## Key Points

- EAT = hit ratio×(TLB+memory) + miss ratio×(TLB+page-table memory+data memory).

## Why the other options are incorrect

Values 175 and 185 undercount the miss penalty. Two hundred five does not match the stated probabilities. Because the page table is in memory, every TLB miss needs two main-memory accesses, not one.
