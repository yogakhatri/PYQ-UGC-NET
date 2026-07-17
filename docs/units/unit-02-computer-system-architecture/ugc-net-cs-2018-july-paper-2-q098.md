# Question 98

*UGC NET CS · 2018 July Paper 2 · Memory Hierarchy · Cache Mapping Techniques*

Which of the following mapping is not used for mapping process in cache memory ?

- **1.** Associative mapping
- **2.** Direct mapping
- **3.** Set-Associative mapping
- **4.** Segmented - page mapping

> [!TIP]
> **Correct answer: 4. Segmented - page mapping**

## Solution

The three standard cache placement organizations are direct mapping, fully associative mapping, and set-associative mapping. Segmented-paged mapping instead combines segmentation and paging for virtual-memory address translation; it is not a cache mapping method. Therefore option 4 is correct.

## Key Points

- Cache: direct/associative/set-associative; virtual memory: paging/segmentation/segmented paging.

## Why the other options are incorrect

Options 1–3 are exactly the standard cache choices, differing in how many cache lines may hold a given memory block. Do not confuse cache placement with the operating system's logical-to-physical address translation schemes.
