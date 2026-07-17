# Question 7

*UGC NET CS · 2017 Nov Paper 2 · Data Representation · Number Systems and Conversion*

The Octal equivalent of the binary number 1011101011 is :

- **1.** 7353
- **2.** 1353
- **3.** 5651
- **4.** 5657

> [!TIP]
> **Correct answer: 2. 1353**

## Solution

Because 8=2³, convert binary to octal by grouping bits in sets of three from the right. Pad on the left if necessary: 1011101011₂ = 001 011 101 011₂. The groups represent 1, 3, 5, and 3, so the octal number is 1353₈. Therefore option 2 is correct.

## Key Points

- One octal digit corresponds exactly to three binary bits: 000→0 through 111→7.

## Why the other options are incorrect

The other choices come from grouping in the wrong direction or translating a three-bit group incorrectly. Group boundaries must start at the binary point and move outward; for an integer, start from the rightmost bit.
