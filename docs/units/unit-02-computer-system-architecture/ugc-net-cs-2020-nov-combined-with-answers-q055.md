# Question 55

*UGC NET CS · 2020 Nov With Answers · Memory Hierarchy · Direct-Mapped Cache Address Fields*

A machine has a byte-addressable main memory of 2^16 bytes, a block size of 8 bytes, and a direct-mapped cache with 32 lines. How many bits are in the tag, line, and word/byte-offset fields of a main-memory address, respectively?

- **1.** 8, 5, 3
- **2.** 8, 6, 2
- **3.** 7, 5, 4
- **4.** 7, 6, 3

> [!TIP]
> **Correct answer: 1. 8, 5, 3**

## Solution

Byte-addressable memory of 2^16 bytes needs a 16-bit address. Each cache block holds 8=2^3 bytes, so the lowest 3 bits select a byte within the block. A direct-mapped cache with 32=2^5 lines needs 5 index bits. The remaining high bits form the tag: 16−3−5=8. Thus tag, line, and offset widths are 8,5,3, which is option 1.

## Key Points

- Address = tag | line index | block offset; widths come from log2(lines) and log2(bytes per block).

## Why the other options are incorrect

Every other option either allocates the wrong number of index/offset bits or fails to total 16 correctly. Six line bits would imply 64 cache lines, and a two- or four-bit offset would imply 4- or 16-byte blocks.
