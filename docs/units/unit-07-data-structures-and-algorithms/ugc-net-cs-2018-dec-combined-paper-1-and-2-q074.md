# Question 74

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Structures · Postfix Evaluation with a Stack*

For postfix expression 6 2 3 * / 4 2 * + 6 8 * -, what are the top two stack elements after the second multiplication operator is evaluated?

- **1.** 8,2
- **2.** 8,1
- **3.** 6,2
- **4.** 6,3

> [!TIP]
> **Correct answer: 2. 8,1**

## Solution

Evaluate postfix left to right. Push 6,2,3; the first * replaces 2 and 3 by 6, leaving [6,6]. The / replaces these by 6/6=1, leaving [1]. Push 4 and 2, then the second * replaces them by 8, leaving [1,8] from bottom to top. Thus the top element is 8 and the next is 1: option 2.

## Key Points

- Postfix evaluation: operands push; each binary operator pops two values, computes left op right, and pushes one result.

## Why the other options are incorrect

The other pairs either report values before division, reverse operand/order history, or continue beyond the requested second multiplication. Operators pop the right operand first and the left operand second, although multiplication itself is commutative here.
