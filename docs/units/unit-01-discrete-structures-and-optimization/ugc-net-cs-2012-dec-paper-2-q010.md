# Question 10

*UGC NET CS · 2012 Dec Paper 2 · Counting, Mathematical Induction and Discrete Probability · Inclusion-Exclusion for Bit Strings*

The number of bit strings of length eight that either start with a 1 bit or end with the two bits 00 is:

- **1.** 32
- **2.** 64
- **3.** 128
- **4.** 160

> [!TIP]
> **Correct answer: 4. 160**

## Solution

Let A be the length-8 strings that start with 1 and B those that end with 00. For A, the remaining seven bits are free, so |A|=2^7=128. For B, the first six bits are free, so |B|=2^6=64. Strings in both sets start with 1 and end with 00; five middle bits remain free, giving |A intersection B|=2^5=32. Inclusion-exclusion gives 128+64-32=160.

## Key Points

- For an 'either ...
- or ...' count, use |A union B|=|A|+|B|-|A intersection B|.

## Why the other options are incorrect

32 counts only the overlap, 64 counts only strings ending in 00, and 128 counts only strings starting in 1. Simply adding 128 and 64 would also be wrong because it double-counts the 32 strings satisfying both conditions.
