# Question 15

*UGC NET CS · 2017 Jan Paper 2 · Programming in C · Bitwise AND Expressions*

If X is a binary number which is power of 2, then the value of X & (X – 1) is :

- **1.** 11….11
- **2.** 00…..00
- **3.** 100…..0
- **4.** 000……1

> [!TIP]
> **Correct answer: 2. 00…..00**

## Solution

A positive power of two has exactly one set bit: X=100…0₂. Subtracting one clears that position and makes every lower bit 1: X−1=011…1₂. The two numbers therefore have no position in which both bits are 1, so X & (X−1)=000…0₂. This is option 2.

## Key Points

- The test X>0 and (X & (X−1))=0 recognizes powers of two because subtraction removes the only set bit.

## Why the other options are incorrect

All-ones is X−1, not the AND result. 100…0 is X itself. 000…1 would require the least-significant bit to be set in both operands, which cannot happen for a power of two larger than 1; for X=1 the result is still zero.
