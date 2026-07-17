# Question 70

*UGC NET CS · 2013 Dec Paper 3 · Memory Hierarchy · TLB Associative Lookup*

Translation Look-aside Buffer (TLB) is

- **A.** a cache-memory in which item to be searched is compared one-by-one with the keys.
- **B.** a cache-memory in which item to be searched is compared with all the keys simultaneously.
- **C.** an associative memory in which item to be searched is compared one-by-one with the keys.
- **D.** an associative memory in which item to be searched is compared with all the keys simultaneously.

> [!TIP]
> **Correct answer: D. an associative memory in which item to be searched is compared with all the keys simultaneously.**

## Solution

A TLB stores recently used virtual-page to physical-frame translations. It is implemented as associative, or content-addressable, memory: the incoming virtual page number is presented to all stored tags, and comparison hardware checks the tags in parallel. A match can therefore return the frame number without a sequential one-by-one search.

## Key Points

- A TLB is a small associative translation cache whose tags are searched in parallel.

## Why the other options are incorrect

A and C describe sequential comparison, which would defeat the TLB's speed. B recognizes parallel comparison but calls the organization only cache memory; D gives the precise associative-memory mechanism and the simultaneous tag comparison requested by the definitions.
