# Question 67

*UGC NET CS · 2020 Nov With Answers · File and Input/Output Systems · Inode Addressing and Maximum File Size*

A Linux-style file system has 2 KiB blocks and 32-bit disk addresses. An inode contains 12 direct block addresses, one single-indirect address, and one double-indirect address. Approximately what is the largest representable file?

- **1.** 513 Kbytes
- **2.** 513 MBytes
- **3.** 537 Mbytes
- **4.** 537 KBytes

> [!TIP]
> **Correct answer: 2. 513 MBytes**

## Solution

A 32-bit address occupies 4 bytes, so one 2 KiB indirect block holds 2048/4=512 addresses. The inode reaches 12 direct data blocks, 512 blocks through the single-indirect pointer, and 512² blocks through the double-indirect pointer. Total data capacity is (12+512+262,144)×2048 bytes = 525,336 KiB, approximately 513 MiB. Thus option 2.

## Key Points

- Pointers per indirect block = block size/address size; double indirection contributes that number squared.

## Why the other options are incorrect

The kilobyte answers ignore the double-indirect level. About 537 MB results from decimal/binary unit confusion or an incorrect pointer count. Metadata blocks store addresses and are not themselves counted as file-data capacity.
