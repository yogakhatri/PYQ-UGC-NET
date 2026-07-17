# Question 6

*UGC NET CS · 2016 July Paper 3 · Memory Hierarchy · Cache Memory*

In _____ method, the word is written to the block in both the cache and main memory, in parallel.

- **1.** Write through
- **2.** Write back
- **3.** Write protected
- **4.** Direct mapping

> [!TIP]
> **Correct answer: 1. Write through**

## Solution

With a write-through cache, every processor write updates the cache line and main memory immediately (often using a write buffer). Thus the two copies remain consistent after each completed write, matching option 1.

## Key Points

- Write-through updates cache and memory on each write; write-back postpones memory update until eviction.

## Why the other options are incorrect

Write-back changes only the cache initially and writes the block to memory when it is evicted. Write protection prevents or restricts writing. Direct mapping determines where a memory block may be placed in the cache; it is not a write policy.
