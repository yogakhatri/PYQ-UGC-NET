# Question 54

*UGC NET CS · 2013 June Paper 3 · Error Detection and Correction · Hamming Distance*

Hamming distance between 100101000110 and 110111101101 is

- **A.** 3
- **B.** 4
- **C.** 5
- **D.** 6

> [!TIP]
> **Correct answer: D. 6**

## Solution

Hamming distance is the number of positions at which equal-length binary strings differ. Comparing 100101000110 with 110111101101 gives mismatches at positions 2, 5, 7, 9, 11 and 12. There are six mismatches, so the distance is 6.

## Key Points

- Hamming distance = population count of the XOR of the two codewords.

## Why the other options are incorrect

The counts 3, 4 and 5 stop before all mismatching positions have been included. A position-by-position XOR gives 010010101011, whose six 1s confirm the result.
