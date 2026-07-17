# Question 10

*UGC NET CS · 2009 Dec Paper 2 · Data Representation · Floating-Point Representation*

How many 1’s are present in the binary representation of 3 × 512 + 7 × 64 + 5 × 8 + 3

- **A.** 8
- **B.** 9
- **C.** 10
- **D.** 11

> [!TIP]
> **Correct answer: B. 9**

## Solution

Write each coefficient in binary and shift: 3×512 contributes bits 10 and 9; 7×64 contributes bits 8,7,6; 5×8 contributes bits 5 and 3; and 3 contributes bits 1 and 0. These positions do not overlap, giving 2+3+2+2=9 one-bits.

## Key Points

- Multiplication by powers of two shifts a coefficient's binary bit pattern without changing its popcount.

## Why the other options are incorrect

The other counts result from treating decimal coefficients as single bits or overlooking the multiple 1s in 3, 5, or 7.
