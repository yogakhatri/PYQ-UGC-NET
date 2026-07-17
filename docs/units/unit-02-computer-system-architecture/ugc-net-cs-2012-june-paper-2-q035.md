# Question 35

*UGC NET CS · 2012 June Paper 2 · Data Representation · Signed Integer Range*

If a signed integer occupies two bytes, what is its maximum value?

- **A.** 2^16-1
- **B.** 2^15-1
- **C.** 2^16
- **D.** 2^15

> [!TIP]
> **Correct answer: B. 2^15-1**

## Solution

Two bytes contain 16 bits. In the usual two's-complement signed representation, one bit position determines the negative range, leaving the maximum positive bit pattern 0 followed by fifteen 1s. Its value is 2^15-1=32767.

## Key Points

- An n-bit two's-complement integer ranges from -2^(n-1) to 2^(n-1)-1.

## Why the other options are incorrect

2^16-1=65535 is the maximum unsigned 16-bit value. 2^16 is outside the 16-bit unsigned range. 2^15=32768 is one greater than the maximum signed positive value.
