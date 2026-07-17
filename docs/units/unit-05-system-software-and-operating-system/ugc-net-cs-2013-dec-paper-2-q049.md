# Question 49

*UGC NET CS · 2013 Dec Paper 2 · File Systems · Free-Space Bitmap Size*

How much space will be required to store the bit map of a 1.3 GB disk with 512 bytes block size ?

- **A.** 332.8 KB
- **B.** 83.6 KB
- **C.** 266.2 KB
- **D.** 256.6 KB

> [!TIP]
> **Correct answer: A. 332.8 KB**

## Solution

With binary storage units, the number of 512-byte blocks is (1.3×2^30)/2^9=1.3×2^21. A bitmap needs one bit per block, so its size is (1.3×2^21)/8=1.3×2^18 bytes. Dividing by 2^10 bytes per KB gives 1.3×2^8=332.8 KB.

## Key Points

- Bitmap size in bytes = disk size in bytes / block size in bytes / 8.

## Why the other options are incorrect

The other values result from losing a factor of 4, using the wrong block count, or mixing bits and bytes. The sequence must be disk bytes ÷ bytes per block ÷ 8 bits per bitmap byte.
