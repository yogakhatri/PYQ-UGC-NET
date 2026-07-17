# Question 94

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Boolean Algebra · Boolean Functions and their Representation*

Consider the Boolean expression given by F=(X+Y+Z)(X'+Y)(Y'+Z). Which of the following Boolean expressions is/are equivalent to F' (Complement of F)? A. (X'+Y'+Z)(X+Y')(Y+Z') B. (XY +Z') C. (X+Z')Y+Z') D. (XY + YZ +XY'Z) Choose the correct answer from the options given below:

- **1.** A, B and C Only
- **2.** B, C and D Only
- **3.** A, C and D Only
- **4.** A, B and D Only

> [!TIP]
> **Correct answer: 2. B, C and D Only**

## Solution

De Morgan gives F'=X'Y'Z'+XY'+YZ' (D). This simplifies to Z'+XY' (B): when Z'=1 the three terms cover both Y values, while for Z=1 only XY' remains. C=(X+Z')(Y'+Z') also simplifies to Z'+XY'. A incorrectly complements literals without changing the product of sums into a sum.

## Key Points

- Complement a product into a sum of complemented factors, then use absorption/consensus.

## Why the other options are incorrect

Options containing A accept an invalid De Morgan transformation; B,C,D are equivalent.
