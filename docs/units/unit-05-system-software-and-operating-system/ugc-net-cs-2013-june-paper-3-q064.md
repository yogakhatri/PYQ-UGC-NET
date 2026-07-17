# Question 64

*UGC NET CS · 2013 June Paper 3 · File Systems · Inode Direct and Indirect Addressing*

A UNIX file system has a 1 KB block size and 4-byte disk addresses. What is the maximum file size if the inode contains ten direct block entries, one single-indirect entry, one double-indirect entry and one triple-indirect entry?

- **A.** 30 GB
- **B.** 64 GB
- **C.** 16 GB
- **D.** 1 GB

> [!TIP]
> **Correct answer: C, approximately 16 GB (the exact binary capacity from all listed pointers is about 16.063 GiB).**

## Solution

A 1 KB indirect block holds 1024/4=256 disk addresses. The inode can therefore address 10 direct blocks, 256 through the single-indirect entry, 256² through the double-indirect entry and 256³ through the triple-indirect entry. Total size is (10+256+256²+256³)×1 KB = 16,843,018 KB, about 16.063 GiB. The dominant triple-indirect term is exactly 16 GiB, so the offered rounded answer is 16 GB.

## Key Points

- Indirect capacity grows by pointer fan-out: B/addr pointers per level, giving n, n² and n³ data blocks.

## Why the other options are incorrect

1 GB is far too small because triple indirection alone reaches 256³ blocks. 30 GB and 64 GB overstate the pointer fan-out; a 1 KB block with 4-byte addresses has 256, not 512 or 1024, pointers.
