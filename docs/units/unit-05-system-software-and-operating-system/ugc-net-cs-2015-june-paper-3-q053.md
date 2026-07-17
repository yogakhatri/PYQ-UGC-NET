# Question 53

*UGC NET CS · 2015 June Paper 3 · File and Input/Output Systems · Linked File Allocation*

In __________ allocation method for disk block allocation in a file system, insertion and deletion of blocks in a file is easy.

- **1.** Index
- **2.** Linked
- **3.** Contiguous
- **4.** Bit Map

> [!TIP]
> **Correct answer: 2. Linked**

## Solution

In linked allocation, every file block contains a pointer to the next block. Inserting a block requires changing nearby links, and deleting one requires bypassing its link; the remaining file need not be moved. Hence block insertion and deletion are easy.

## Key Points

- Linked allocation trades easy growth and edits for poor random access and pointer overhead.

## Why the other options are incorrect

Contiguous allocation may require moving or relocating a file when it grows. Indexed allocation supports direct access through an index, but insertion can require index updates or additional index capacity. A bitmap records free-space availability; it is not itself a per-file block-allocation method.
