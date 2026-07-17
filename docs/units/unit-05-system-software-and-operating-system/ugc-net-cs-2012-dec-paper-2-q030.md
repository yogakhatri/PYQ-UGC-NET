# Question 30

*UGC NET CS · 2012 Dec Paper 2 · Memory Management · Segmentation and External Fragmentation*

Which memory-allocation scheme suffers from external fragmentation?

- **1.** Segmentation
- **2.** Pure demand paging
- **3.** Swapping
- **4.** Paging

> [!TIP]
> **Correct answer: 1. Segmentation**

## Solution

Segmentation allocates variable-sized contiguous regions for logical segments such as code, stack and data. As segments are created and removed, free memory becomes separated into holes. The total free space may be sufficient while no single contiguous hole is large enough, which is external fragmentation.

## Key Points

- Variable-size contiguous allocation, including segmentation, causes external fragmentation; fixed-size paging avoids it.

## Why the other options are incorrect

Paging and pure demand paging use fixed-size pages and frames, so any free frame can hold any page and external fragmentation is avoided, though internal fragmentation can occur. Swapping is a movement policy rather than the listed variable-sized allocation scheme whose defining problem is being tested; its fragmentation behavior depends on the underlying allocator.
