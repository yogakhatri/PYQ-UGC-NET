# Question 6

*UGC NET CS · 2014 Dec Paper 3 · 8085 Microprocessor · Addition and Status Flags*

Specify the contents of the accumulator and the status of the S, Z and CY flags when 8085 microprocessor performs addition of 87 H and 79 H.

- **A.** 11, 1, 1, 1
- **B.** 10, 0, 1, 0
- **C.** 01, 1, 0, 0
- **D.** 00, 0, 1, 1

> [!TIP]
> **Correct answer: D. 00, 0, 1, 1**

## Solution

Hexadecimal addition gives 87H+79H=100H. The 8085 accumulator retains the low eight bits, 00H, and the ninth bit sets CY=1. Because the 8-bit result is zero, Z=1. Its most significant bit is 0, so S=0. The tuple (accumulator,S,Z,CY) is therefore (00,0,1,1).

## Key Points

- For 8-bit addition, keep the low byte in A; the ninth bit becomes carry, while S and Z describe the low byte.

## Why the other options are incorrect

A and B give nonzero accumulator values and incorrect flag combinations. C misses both the exact zero result and the carry out. D alone follows the 8-bit truncation and flag definitions.
