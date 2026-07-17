# Question 49

*UGC NET CS · 2015 Dec Paper 2 · File and Input/Output Systems · Inode Direct and Indirect Addressing*

A Unix file system has 1-KB blocks and 4-byte disk addresses. What is the maximum file size if each inode contains 10 direct entries and one single-, double-, and triple-indirect entry?

- **1.** 32 GB
- **2.** 64 GB
- **3.** 16 GB
- **4.** 1 GB

> [!TIP]
> **Correct answer: 3. 16 GB**

## Solution

An indirect block holds 1024/4=256 disk addresses. The inode can address 10 + 256 + 256² + 256³ data blocks. Multiplying by 1 KB gives 10 KB + 256 KB + 64 MB + 16 GB, approximately 16.063 GB (using binary units). The triple-indirect contribution dominates, so the closest listed maximum is 16 GB.

## Key Points

- Pointers per indirect block = block size/address size; sum direct, single, double, and triple capacities.

## Why the other options are incorrect

1 GB undercounts the triple-indirect level. 32 GB and 64 GB exceed what 256³ one-kilobyte data blocks can address. Each indirection level multiplies capacity by 256, not by the block size directly.
