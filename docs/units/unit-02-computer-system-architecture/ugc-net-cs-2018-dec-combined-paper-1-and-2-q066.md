# Question 66

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Representation · IEEE-754 Single-Precision Encoding*

The decimal floating point number -40.1 represented using IEEE-754 32-bit representation and written in hexadecimal form is

- **1.** 0xC2206666
- **2.** 0xC2206000
- **3.** 0xC2006666
- **4.** 0xC2006000

> [!TIP]
> **Correct answer: 1. 0xC2206666**

## Solution

First encode the magnitude. The binary expansion is 40.1≈101000.000110011…₂=1.0100000011001100…₂×2⁵. The sign bit is 1 because the number is negative. The biased exponent is 5+127=132=10000100₂. Rounding the repeating fraction to 23 stored bits gives 01000000110011001100110. Therefore the 32 bits are 1|10000100|01000000110011001100110 = 1100 0010 0010 0000 0110 0110 0110 0110₂ = C2206666₁₆, so option 1 is correct.

## Key Points

- IEEE-754 single precision stores sign (1 bit), biased exponent (8 bits, bias 127), and fraction (23 bits), then the 32 bits can be grouped into hexadecimal nibbles.

## Why the other options are incorrect

C200… uses the wrong exponent/fraction boundary for 40.1, while …6000 truncates away significant repeating fractional bits. Since 0.1 has no finite binary expansion, its single-precision representation necessarily contains the rounded repeating pattern.
