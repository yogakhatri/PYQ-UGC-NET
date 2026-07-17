# Question 49

*UGC NET CS · 2017 Jan Paper 3 · Memory Management · Paging Address-Bit Calculation*

A memory management system has 64 pages with 512 bytes page size. Physical memory consists of 32 page frames. Number of bits required in logical and physical address are respectively :

- **1.** 14 and 15
- **2.** 14 and 29
- **3.** 15 and 14
- **4.** 16 and 32

> [!TIP]
> **Correct answer: 3. 15 and 14**

## Solution

A 512-byte page needs log2(512)=9 offset bits. The logical space has 64=2^6 pages, so its page number needs 6 bits and a logical address needs 6+9=15 bits. Physical memory has 32=2^5 frames, so its frame number needs 5 bits and a physical address needs 5+9=14 bits. Thus the pair is 15 and 14, option 3.

## Key Points

- Paged address = page-or-frame number bits + offset bits; offset bits are log2(page size).

## Why the other options are incorrect

The offset is the same in logical and physical addresses because page and frame sizes are equal. Options 1, 2, and 4 use inconsistent page/frame counts or fail to add the 9-bit offset correctly.
