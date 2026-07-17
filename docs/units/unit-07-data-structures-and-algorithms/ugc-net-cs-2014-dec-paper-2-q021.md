# Question 21

*UGC NET CS · 2014 Dec Paper 2 · Stacks and Expression Processing · Infix-to-Postfix Conversion*

Convert the following infix expression into its equivalent post fix expression (A + B^ D) / (E – F) + G

- **A.** ABD^ + EF – / G+
- **B.** ABD + ^EF – / G+
- **C.** ABD + ^EF / – G+
- **D.** ABD^ + EF / – G+

> [!TIP]
> **Correct answer: A. ABD^ + EF – / G+**

## Solution

Convert each parenthesized part first. B^D becomes B D ^, so A+B^D becomes A B D ^ +. E−F becomes E F −. Dividing the two gives A B D ^ + E F − /. Finally add G, producing A B D ^ + E F − / G +.

## Key Points

- Postfix emits operands first and writes each operator immediately after its complete operand subexpressions.

## Why the other options are incorrect

B applies + before exponentiation. C and D place the division and subtraction in the wrong order for the denominator E−F. A alone preserves exponentiation, both parentheses, division and the final addition.
