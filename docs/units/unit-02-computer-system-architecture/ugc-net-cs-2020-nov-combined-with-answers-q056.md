# Question 56

*UGC NET CS · 2020 Nov With Answers · Basic Computer Organization and Design · Basic-Computer Program Tracing*

In a 16-bit basic computer, the following program and data are stored at hexadecimal locations: 210 CLA; 211 ADD 217; 212 INC; 213 STA 217; 214 LDA 218; 215 CMA; 216 AND 217; M[217]=1234H; M[218]=9CE2H. What is the accumulator content after execution?

- **1.** 1002H
- **2.** 2011H
- **3.** 2022H
- **4.** 0215H

> [!TIP]
> **Correct answer: 4. 0215H**

## Solution

Trace the program in hexadecimal. CLA sets AC=0000H. ADD 217 gives AC=1234H, and INC makes it 1235H. STA 217 therefore changes M[217] to 1235H. LDA 218 loads 9CE2H. CMA takes the 16-bit one's complement, producing 631DH. Finally AND 217 computes 631DH AND 1235H nibble by nibble: 6&1=0, 3&2=2, 1&3=1, D&5=5. The result is 0215H, option 4.

## Key Points

- Program tracing requires updating memory after STA, then applying 16-bit complement and bitwise AND exactly.

## Why the other options are incorrect

The other values result from forgetting that STA changes location 217 before the final AND, complementing the wrong operand, or performing arithmetic rather than bitwise AND. CMA flips every one of the 16 bits.
