# Question 85

*UGC NET CS · 2019 Dec Paper 1 And 2 · Number-Theoretic Algorithms · Modular Exponentiation by Repeated Squaring*

Using repeated squaring, for a=7, b=17 and n=561, what is the value of a^b mod n?

- **1.** 160
- **2.** 166
- **3.** 157
- **4.** 67

> [!TIP]
> **Correct answer: 1. 160**

## Solution

Write 17=16+1 and use repeated squaring. 7² mod 561=49; 7⁴ mod 561=49² mod 561=157; 7⁸ mod 561=157² mod 561=526; and 7¹⁶ mod 561=526² mod 561=103. Therefore 7¹⁷ mod 561=(103×7) mod 561=721 mod 561=160. Option 1 is correct.

## Key Points

- Binary modular exponentiation squares and reduces for each bit, then multiplies residues corresponding to 1-bits of the exponent.

## Why the other options are incorrect

The other residues do not follow from the modular squaring chain. Reducing after every square is essential: it keeps numbers small without changing the final remainder. Since 17 has binary form 10001, only the 16th-power and first-power residues are multiplied at the end.
