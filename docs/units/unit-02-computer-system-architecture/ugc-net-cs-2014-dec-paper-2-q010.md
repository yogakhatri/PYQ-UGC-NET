# Question 10

*UGC NET CS · 2014 Dec Paper 2 · Combinational Logic with ROM · ROM Address and Word Sizing*

The size of the ROM required to build an 8-bit adder/subtractor with mode control, carry input, carry output and two’s complement overflow output is given as

- **A.** 2^16 × 8
- **B.** 2^18 × 10
- **C.** 2^16 × 10
- **D.** 2^18 × 8

> [!TIP]
> **Correct answer: B. 2^18 × 10**

## Solution

A ROM needs one address bit for every input bit. The two 8-bit operands contribute 16 address inputs, while mode control and carry input add two more, for 18 address bits and 2^18 words. Each word must produce the 8-bit sum/difference plus carry output and overflow output, totaling 10 output bits. The required organization is therefore 2^18×10.

## Key Points

- ROM realization: 2^(number of input variables) words × number of output functions bits.

## Why the other options are incorrect

The 2^16 choices ignore mode and carry input. The 8-bit-wide choices omit the carry and overflow outputs. Only B includes all 18 inputs and all 10 outputs.
