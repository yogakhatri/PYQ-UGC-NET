# Question 58

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Digital Logic Circuits and Components · Registers and Counters*

18110-87008 Let R1 and R2 be two 4-bit registers that store numbers in 2's complement form. For the operation R1 + R2, which one of the following values of R1 and R2 gives an arithmetic overflow?

- **1.** R1 = 1011 and R2 = 1110
- **2.** R1 = 1100 and R2 = 1010
- **3.** R1 = 0011 and R2 = 0100
- **4.** R1 = 1001 and R2 = 1111

> [!TIP]
> **Correct answer: 2. R1 = 1100 and R2 = 1010**

## Solution

Four-bit two's complement spans −8 to +7. Option 2 adds 1100(−4)+1010(−6)=−10, outside the range, so overflow occurs. The stored four-bit result wraps to +6, revealing the sign error.

## Key Points

- Signed overflow occurs when same-sign operands produce an opposite-sign result.

## Why the other options are incorrect

Option 1 gives −7, option 3 gives +7, and option 4 gives −8; all are representable.
