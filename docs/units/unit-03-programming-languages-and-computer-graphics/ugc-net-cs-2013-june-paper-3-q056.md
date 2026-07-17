# Question 56

*UGC NET CS · 2013 June Paper 3 · Computer Graphics and Image Processing · Counting Binary Images*

The number of distinct binary images that can be generated with size M × N is

- **A.** M + N
- **B.** M × N
- **C.** 2^(M+N)
- **D.** 2^(MN)

> [!TIP]
> **Correct answer: D. 2^(MN)**

## Solution

An M×N image contains MN pixel positions. In a binary image each position has two independent choices, 0 or 1. By the multiplication principle, the number of possible assignments is 2×2×…×2 over MN positions, which equals 2^(MN).

## Key Points

- For k possible values at each of P independent pixels, the number of images is k^P; here k=2 and P=MN.

## Why the other options are incorrect

M+N and M×N count dimensions or positions rather than assignments of values to all positions. 2^(M+N) treats row and column counts as independent binary choices; the exponent must be the number of pixels, MN.
