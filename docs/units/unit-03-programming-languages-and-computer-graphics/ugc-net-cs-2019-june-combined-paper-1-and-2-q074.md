# Question 74

*UGC NET CS · 2019 June Paper 1 And 2 · Programming in C++ · Bitwise operations*

Consider the C++ function: unsigned int f(unsigned int n){ unsigned int b=0; while(n){ b += n & 1; n >>= 1; } return b; }. The function returns the integer representing which property P in the binary representation of positive integer n?

- **1.** number of 0s
- **2.** number of bits
- **3.** number of consecutive 1s
- **4.** number of 1s

> [!TIP]
> **Correct answer: 4. number of 1s**

## Solution

In each iteration, n&1 extracts the least-significant bit. That bit is added to b, so b increases only when the extracted bit is 1. The right shift n>>=1 then discards the bit just examined. When n becomes zero, every original bit has been processed and b equals the number of 1 bits in the binary representation.

## Key Points

- Repeatedly add n&1 and right-shift n to compute the population count of an integer.

## Why the other options are incorrect

- **Option 1:** zero bits never increase b.
- **Option 2:** leading and encountered zero bits are not counted, so b is not the bit length.
- **Option 3:** the function counts all 1 bits, whether consecutive or separated.
