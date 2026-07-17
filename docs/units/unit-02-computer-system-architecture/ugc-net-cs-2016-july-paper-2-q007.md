# Question 7

*UGC NET CS · 2016 July Paper 2 · Data Representation · IEEE 754 Double Precision*

The IEEE-754 double-precision format to represent floating point numbers, has a length of _____ bits.

- **1.** 16
- **2.** 32
- **3.** 48
- **4.** 64

> [!TIP]
> **Correct answer: 4. 64**

## Solution

IEEE 754 binary64, commonly called double precision, occupies 64 bits: 1 sign bit, 11 exponent bits, and 52 stored fraction bits. Normal finite numbers also have an implicit leading significand bit, giving 53 bits of precision without increasing storage beyond 64 bits.

## Key Points

- binary64 layout = 1 sign + 11 exponent + 52 fraction = 64 stored bits.

## Why the other options are incorrect

Thirty-two bits is binary32 single precision. Sixteen-bit formats are half precision variants, while 48 is not the IEEE 754 binary64 width. Only option 4 matches the standard layout.
