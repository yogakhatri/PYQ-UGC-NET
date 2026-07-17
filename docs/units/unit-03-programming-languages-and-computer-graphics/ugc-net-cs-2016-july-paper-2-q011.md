# Question 11

*UGC NET CS · 2016 July Paper 2 · Programming in C · Operator Precedence and Logical OR*

In C, given i=0, j=1, k=−1, x=0.5, and y=0.0, what is the value of the expression x*y < i+j || k?

- **1.** –1
- **2.** 0
- **3.** 1
- **4.** 2

> [!TIP]
> **Correct answer: 3. 1**

## Solution

C precedence evaluates multiplication and addition before <, and relational comparison before logical OR. Thus x*y=0.5·0.0=0, i+j=1, and 0<1 evaluates to integer 1. The left operand of || is already true, so k is not needed because of short-circuiting, and the logical-OR expression evaluates to 1.

## Key Points

- C order here: * and + → < → ||; logical results are canonical integers 0 or 1.

## Why the other options are incorrect

Logical operators return 0 or 1 in C, not the original operand −1, so option 1 is impossible here. Options 0 and 2 do not follow from the true comparison. The nonzero value k=−1 would also count as true if evaluated, but short-circuiting prevents that evaluation.
