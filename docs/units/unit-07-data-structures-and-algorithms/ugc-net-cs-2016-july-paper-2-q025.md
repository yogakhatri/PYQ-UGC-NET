# Question 25

*UGC NET CS · 2016 July Paper 2 · Trees and Binary Trees · Full Parenthesization and Catalan Numbers*

In how many distinct ways can the five-operand string A ∩ B − A ∩ B − A be fully parenthesized as an infix expression?

- **1.** 15
- **2.** 14
- **3.** 13
- **4.** 12

> [!TIP]
> **Correct answer: 2. 14**

## Solution

The expression has five operands and four binary-operator positions. The number of ways to fully parenthesize n operands, while preserving their order, is the Catalan number C_{n−1}. Thus the count is C₄=(1/5)·C(8,4)=70/5=14.

## Key Points

- Full parenthesizations of n ordered operands = Catalan C_{n−1}.

## Why the other options are incorrect

The operator symbols and repeated operands do not change the number of binary-tree shapes; full parenthesization depends only on having five ordered operands. Values 12, 13, and 15 are not C₄.
