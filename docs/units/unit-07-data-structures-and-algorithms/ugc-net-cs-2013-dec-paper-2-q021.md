# Question 21

*UGC NET CS · 2013 Dec Paper 2 · Data Structures · Postfix Expression Evaluation*

What is the value of the postfix expression ? a b c d + – ∗ (where a = 8, b = 4, c = 2 and d = 5)

- **A.** -3/8
- **B.** -8/3
- **C.** 24
- **D.** –24

> [!TIP]
> **Correct answer: D. –24**

## Solution

Evaluate postfix with a stack. Push 8, 4, 2 and 5. The + operator combines 2 and 5 to give 7, leaving 8, 4, 7. The - operator pops 7 then 4 and computes 4-7=-3. Finally * computes 8 x (-3)=-24.

## Key Points

- Postfix evaluation rule: push operands; on an operator, compute second-pop operator first-pop and push the result.

## Why the other options are incorrect

The fractional options result from reversing or changing the operators, while 24 loses the negative sign. For every binary postfix operator, the first popped value is the right operand and the second popped value is the left operand.
