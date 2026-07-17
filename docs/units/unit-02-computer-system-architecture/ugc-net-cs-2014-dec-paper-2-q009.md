# Question 9

*UGC NET CS · 2014 Dec Paper 2 · Data Representation · Normalized Floating-Point Range*

The range of representable normalized positive magnitudes in a 32-bit floating-point binary-fraction representation with 1 sign bit, an 8-bit excess-128 exponent and a 23-bit mantissa is

- **A.** 2^−128 to (1−2^−23)×2^127
- **B.** (1−2^−23)×2^−127 to 2^128
- **C.** (1−2^−23)×2^−127 to 2^23
- **D.** 2^−129 to (1−2^−23)×2^127

> [!TIP]
> **Correct answer: D. 2^−129 to (1−2^−23)×2^127**

## Solution

With an 8-bit excess-128 exponent, stored values 0 through 255 represent exponents −128 through 127. A normalized 23-bit binary fraction ranges from 0.100…₂=2^−1 to 0.111…₂=1−2^−23. Thus the smallest positive normalized magnitude is 2^−1·2^−128=2^−129, and the largest is (1−2^−23)·2^127.

## Key Points

- Range = normalized mantissa endpoint × exponent endpoint; for a binary fraction the minimum mantissa is 0.1₂.

## Why the other options are incorrect

A misses the leading fractional factor 2^−1 in the minimum. B reverses and misstates the endpoints. C incorrectly uses the mantissa bit count as the maximum exponent. The question is not using IEEE-754's bias-127 hidden-leading-one convention; it explicitly specifies excess 128 and a binary fraction.
