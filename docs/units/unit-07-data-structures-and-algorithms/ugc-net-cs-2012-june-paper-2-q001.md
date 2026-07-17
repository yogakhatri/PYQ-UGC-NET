# Question 1

*UGC NET CS · 2012 June Paper 2 · Data Structures · Stack Applications*

The postfix expression AB + CD – * can be evaluated using a

- **A.** stack
- **B.** tree
- **C.** queue
- **D.** linked list

> [!TIP]
> **Correct answer: A. stack**

## Solution

Scan a postfix expression from left to right. Push each operand. When an operator appears, pop the required operands, apply the operator, and push the result. For AB+CD-*, the stack forms (A+B), then (C-D), and finally multiplies those two results. Last-in, first-out access is exactly what is needed, so a stack is the standard evaluator.

## Key Points

- Postfix evaluation uses a LIFO stack: operands push, operators pop operands and push the result.

## Why the other options are incorrect

A tree can represent the expression after construction but is not the direct one-pass evaluation structure asked for. A queue removes the oldest item rather than the most recent operands. A linked list is an implementation building block; only when used with LIFO operations does it become the required stack.
