# Question 5

*UGC NET CS · 2014 Dec Paper 3 · 8085 Microprocessor · 16-Bit Loop Counter*

How many times will the following loop be executed ? LXI B, 0007 H LOP : DCX B MOV A, B ORA C JNZ LOP

- **A.** 05
- **B.** 07
- **C.** 09
- **D.** 00

> [!TIP]
> **Correct answer: B. 07**

## Solution

LXI B,0007H loads the BC register pair with 7. Each iteration first executes DCX B, decreasing BC by one. MOV A,B followed by ORA C sets the zero flag only when both high byte B and low byte C are zero. The successive post-decrement values are 0006,0005,…,0000, so JNZ repeats until the seventh iteration reaches zero. The loop body executes 7 times.

## Key Points

- ORA of the two bytes is a standard 8085 test for whether a 16-bit register pair equals zero.

## Why the other options are incorrect

5 and 9 do not match the 16-bit countdown. 0 would be plausible only if the loop tested before executing, but the decrement and test are inside a body entered immediately.
