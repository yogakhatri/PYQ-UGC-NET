# Question 32

*UGC NET CS · 2016 July Paper 2 · Microprocessor Programming · 8085 Loop and Accumulator Arithmetic*

What is the content of the accumulator after this 8085 program executes? MVI A,42H; MVI B,05H; UGC: ADD B; DCR B; JNZ UGC; ADI 25H; HLT.

- **1.** 82 H
- **2.** 78 H
- **3.** 76 H
- **4.** 47 H

> [!TIP]
> **Correct answer: 3. 76 H**

## Solution

Initially A=42H and B=05H. Each pass adds the current B to A and then decrements B. Because `JNZ UGC` repeats until B becomes 00H, the values added are 05H+04H+03H+02H+01H=0FH. Thus A becomes 42H+0FH=51H. Finally `ADI 25H` gives 51H+25H=76H. Therefore the accumulator contains 76H.

## Key Points

- Trace an assembly loop using the register value before each instruction; hexadecimal 05+04+03+02+01=0F.

## Why the other options are incorrect

47H would result from adding 05H only and ignores the loop and final immediate addition. The other values do not match the five loop additions followed by 25H. `DCR B` controls the zero flag; it does not change A directly.
