# Question 62

*UGC NET CS · 2019 June Paper 1 And 2 · Memory Hierarchy · Associative Memory*

Suppose that the register A and the register K have the bit configuration. Only the three leftmost bits of A are compared with memory words because K has I's in these positions. Because of its organization, this type of memory is uniquely suited to parallel searches by data association. This type of memory is known as

- **1.** RAM
- **2.** ROM
- **3.** content addressable memory
- **4.** secondary memory

> [!TIP]
> **Correct answer: 3. content addressable memory**

## Solution

The mask register K selects which bit positions of register A participate in a comparison. All stored words can be compared with the selected bits of A simultaneously, so the memory is searched by content rather than by a numeric address. That is content-addressable memory, also called associative memory.

## Key Points

- Content-addressable memory returns matching words by comparing stored contents in parallel.

## Why the other options are incorrect

- **RAM:** describes read/write access by address, not parallel comparison by content.
- **ROM:** describes non-volatile fixed contents, not associative lookup.
- **Secondary memory:** refers to persistent storage such as disks and SSDs.

## Additional Information

A mask permits don't-care positions, so only selected bits need to match the search key.
