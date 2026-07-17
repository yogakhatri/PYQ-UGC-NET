# Question 2

*UGC NET CS · 2021 Nov With Answers · Programming in C · Bitwise Population Count and Power-of-Two Tests*

What does this C function return? int f(unsigned int N) { unsigned int counter=0; while (N>0) { counter += N & 1; N = N >> 1; } return counter == 1; }

- **1.** 1 if N is odd, otherwise 0
- **2.** 1 if N is a power of 2, otherwise 0
- **3.** 1 if the binary representation of N is all 1's, otherwise 0
- **4.** 1 if the binary representation of N has any 1's, otherwise 0

> [!TIP]
> **Correct answer: 2. 1 if N is a power of 2, otherwise 0**

## Solution

Each loop adds N&1, the least-significant bit of N, to counter and then shifts N right. The loop therefore counts the number of 1 bits in the original binary representation. The final comparison is true only when that count is exactly one. A positive unsigned integer has exactly one set bit precisely when it is a power of two; N=0 returns false. Thus option 2.

## Key Points

- Repeated N&1 plus right shift computes population count; popcount one characterizes powers of two.

## Why the other options are incorrect

Oddness checks only the lowest bit, while this function examines every bit. A number of the form 2^k−1 has all 1s and usually produces a count greater than one. 'Any 1' would require counter>0, not counter==1.
