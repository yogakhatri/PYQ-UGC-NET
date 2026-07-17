# Question 1

*UGC NET CS · 2014 Dec Paper 3 · Memory Hierarchy · Average Access Time with Write-Through*

A hierarchical memory system that uses cache memory has ca che access time of 50 nano seconds, main memory access time of 300 nano seconds, 75% of memory reques ts are for read, hit ratio of 0.8 for read access and the write-through scheme is used. What will be the average access time of the system both for read and write requests ?

- **A.** 157.5 n.sec.
- **B.** 110 n.sec.
- **C.** 75 n.sec.
- **D.** 82.5 n.sec.

> [!TIP]
> **Correct answer: A. 157.5 n.sec.**

## Solution

Reads are 75% of requests. A read hit costs 50 ns; a read miss first checks the cache and then accesses memory, costing 50+300=350 ns. Average read time is 0.8×50+0.2×350=110 ns. The remaining 25% are writes; with write-through the main-memory write determines a 300 ns request time. Overall average is 0.75×110+0.25×300=82.5+75=157.5 ns.

## Key Points

- First average hit/miss time within reads, then weight read and write averages by their request frequencies.

## Why the other options are incorrect

110 ns is only the read-request average. 75 and 82.5 omit major miss/write contributions. The calculation must weight read and write paths by both the hit ratio and request mix.
