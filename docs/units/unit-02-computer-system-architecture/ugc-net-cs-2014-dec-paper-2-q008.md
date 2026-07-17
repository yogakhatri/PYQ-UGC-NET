# Question 8

*UGC NET CS · 2014 Dec Paper 2 · Stack Organization · Reverse-Polish Stack Evaluation*

How many PUSH and POP operations are needed, under the question's stack-machine convention, to evaluate (A×B)+(C×D/E) in reverse Polish notation?

- **A.** 4 PUSH and 3 POP instructions
- **B.** 5 PUSH and 4 POP instructions
- **C.** 6 PUSH and 2 POP instructions
- **D.** 5 PUSH and 3 POP instructions

> [!TIP]
> **Correct answer: Intended answer: B, 5 PUSH and 4 POP instructions, under the counting convention assumed by the options.**

## Solution

The postfix form is A B * C D * E / +. It contains five operands, so each operand is pushed once: five PUSH instructions. It contains four binary operators, and the question's convention counts one stack-reduction/POP instruction for each operator, giving four POPs. This matches B. A literal low-level implementation may count two operand pops and one result push per operator; none of the options uses that convention, so the exam is clearly using the simplified expression-stack count.

## Key Points

- Count five operand tokens and four binary-operator reductions in the postfix expression.

## Why the other options are incorrect

A omits one operand and one operator reduction. C invents a sixth operand push. D has the correct five operands but counts only three of the four operators (*,*,/,+).
