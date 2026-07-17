# Question 95

*UGC NET CS · 2018 July Paper 2 · Data Representation · Binary-to-Hexadecimal Conversion*

The hexadecimal equivalent of the binary integer number 110101101 is :

- **1.** D24
- **2.** 1 B D
- **3.** 1 A E
- **4.** 1 A D

> [!TIP]
> **Correct answer: 4. 1 A D**

## Solution

Pad the binary number on the left and group four bits at a time: 110101101₂=0001 1010 1101₂. The groups translate to hexadecimal digits 1, A, and D. Hence the result is 1AD₁₆, option 4.

## Key Points

- One hexadecimal digit corresponds exactly to four binary bits.

## Why the other options are incorrect

D24 groups bits from the wrong side. 1BD would require middle bits 1011, while 1AE would require the last group 1110. Binary-to-hex grouping always begins at the radix point and proceeds outward in groups of four.
