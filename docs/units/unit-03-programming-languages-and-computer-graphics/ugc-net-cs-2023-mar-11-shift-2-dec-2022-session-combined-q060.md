# Question 60

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Programming in C · Signed and unsigned integer types*

Which of the following is wrong about the data types?

- **1.** The number is always positive when qualifier 'unsigned' is used.
- **2.** The number can be positive or negative when the qualifier 'signed' is used
- **3.** The range of values for signed data types is more than that of unsigned data types
- **4.** The left most bit in unsigned data type is used to represent the value

> [!TIP]
> **Correct answer: 3. The range of values for signed data types is more than that of unsigned data types**

## Solution

For the same bit width, an unsigned integer uses every bit for magnitude and therefore represents 2^n nonnegative values. A typical n-bit signed representation uses one bit’s worth of encoding to distinguish negative from nonnegative values, so its maximum positive magnitude is smaller. Thus the claim that the signed type has a greater range of values than the unsigned type is wrong.

## Key Points

- For n bits, unsigned commonly spans 0 to 2^n−1; two’s-complement signed spans −2^(n−1) to 2^(n−1)−1.

## Why the other options are incorrect

Unsigned values are nonnegative, and signed values may be positive or negative. In an unsigned representation the most significant bit contributes to the numeric value rather than serving as a sign bit, so statements 1, 2, and 4 express the intended distinctions.
