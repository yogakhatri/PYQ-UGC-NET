# Question 96

*UGC NET CS · 2018 July Paper 2 · Data Representation · Eight-Bit Two's-Complement Addition*

Compute (−14)₁₀+(−15)₁₀ and give the result in 8-bit two's-complement representation.

- **1.** 11100011
- **2.** 00011101
- **3.** 10011101
- **4.** 11110011

> [!TIP]
> **Correct answer: 1. 11100011**

## Solution

The decimal sum is −14+(−15)=−29. In 8-bit two's complement, +29 is 00011101; invert the bits to 11100010 and add 1 to obtain 11100011. Thus option 1 is correct. Equivalently, 256−29=227, whose binary form is 11100011.

## Key Points

- To encode −x in n-bit two's complement, invert the n-bit +x representation and add 1.

## Why the other options are incorrect

00011101 represents +29, not −29. 10011101 is sign-magnitude-style thinking rather than two's complement. 11110011 represents −13 in 8-bit two's complement.
