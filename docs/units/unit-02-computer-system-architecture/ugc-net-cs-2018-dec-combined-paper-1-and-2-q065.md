# Question 65

*UGC NET CS · 2018 Dec Paper 1 And 2 · Basic Computer Organization and Design · x86 NEG Instruction and Flags*

After executing x86 instructions MOV AL,153 and NEG AL, what are AL in 8-bit binary, Carry Flag CF, and Sign Flag SF?

- **1.** AL=0110 0110, CF=0, SF=0
- **2.** AL=0110 0111, CF=0, SF=1
- **3.** AL=0110 0110, CF=1, SF=1
- **4.** AL=0110 0111, CF=1, SF=0

> [!TIP]
> **Correct answer: 4. AL=0110 0111, CF=1, SF=0**

## Solution

MOV AL,153 loads 153₁₀=99H=10011001₂. NEG AL replaces the byte by its two's complement: 10011001→01100110 after inversion, then +1→01100111 (67H). x86 NEG sets CF when its original operand is nonzero, so CF=1. The result's most significant bit is 0, so SF=0. Thus AL=01100111, CF=1, SF=0, option 4.

## Key Points

- NEG computes 0−operand; CF indicates a nonzero operand and SF copies the sign bit of the result.

## Why the other options are incorrect

01100110 omits the +1 required after bitwise inversion. CF is not cleared here because the original operand is nonzero. SF follows the result's top bit, which is 0 for 01100111.
