# Question 45

*UGC NET CS · 2012 Dec Paper 2 · Programming in C · Bitwise AND Expressions*

What is the result of the expression (1 & 2) + (3 & 4), where & is bitwise AND?

- **1.** 1
- **2.** 3
- **3.** 2
- **4.** 0

> [!TIP]
> **Correct answer: 4. 0**

## Solution

Write the operands in binary. 1 is 001 and 2 is 010, so 1 & 2 = 000 = 0. Likewise, 3 is 011 and 4 is 100, so 3 & 4 = 000 = 0. Therefore (1 & 2) + (3 & 4) = 0 + 0 = 0.

## Key Points

- Evaluate bitwise operators position by position before applying the surrounding arithmetic operation.

## Why the other options are incorrect

The nonzero choices result from confusing bitwise AND with logical truth or ordinary arithmetic. A bit survives AND only when that same bit position is 1 in both operands; neither pair shares a set bit.
