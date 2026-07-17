# Question 88

*UGC NET CS · 2019 Dec Paper 1 And 2 · Data Structures · B-Tree Node Storage*

In a B-Tree. each node represents a disk block. Suppose one block holds 8192 bytes. Each key uses 32 bytes. In a B-tree of order M there are M - 1 keys. Since each branch is on another disk block, we assume a branch is of 4 bytes. The total memory requirement for a non leaf node is

- **1.** 32 M - 32
- **2.** 36 M - 32
- **3.** 36 M - 36
- **4.** 32 M - 36

> [!TIP]
> **Correct answer: 2. 36 M - 32**

## Solution

A non-leaf B-tree node of order M has M child branches and M−1 keys. Key storage is 32(M−1)=32M−32 bytes. Branch-pointer storage is 4M bytes. Their sum is 32M−32+4M=36M−32 bytes, which is option 2.

## Key Points

- An internal order-M B-tree node interleaves M pointers with M−1 keys.

## Why the other options are incorrect

Option 1 counts keys but omits all branch pointers. Option 3 incorrectly uses only M−1 pointers, subtracting 36 rather than 32. Option 4 has neither the correct 36M coefficient nor the correct constant term.
