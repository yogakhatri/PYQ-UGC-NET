# Question 91

*UGC NET CS · 2018 Dec Paper 1 And 2 · Computer Graphics · Indexed Colour and Lookup Tables*

If the frame buffer has 10-bits per pixel and 8-bits are allocated for each of the R, G, and B components, then what would be the size of the color lookup table (LUT)?

- **1.** (2^8 + 2^9) bytes
- **2.** (2^10 + 2^8) bytes
- **3.** (2^10 + 2^24) bytes
- **4.** (2^10 + 2^11) bytes

> [!TIP]
> **Correct answer: 4. (2^10 + 2^11) bytes**

## Solution

Ten frame-buffer bits form an index into 2^10 lookup-table entries. Each entry stores three 8-bit components, so it needs 24 bits=3 bytes. The table size is 2^10×3=3×2^10 bytes. Since 3×2^10=2^10+2×2^10=2^10+2^11, this matches option 4 (3072 bytes).

## Key Points

- Indexed colour LUT size = number of indices × bytes stored per RGB entry.

## Why the other options are incorrect

The other sums do not equal 2^10 entries times 3 bytes per entry. In particular, 2^24 is the number of possible 24-bit colours, not the number of bytes required by a 10-bit-indexed table.
