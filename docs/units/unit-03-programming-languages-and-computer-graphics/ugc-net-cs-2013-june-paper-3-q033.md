# Question 33

*UGC NET CS · 2013 June Paper 3 · Programming-Language Design · Arithmetic-Expression Design Issues*

Consider these questions about arithmetic expressions: (a) What are the operator-precedence rules? (b) What are the operator-associativity rules? (c) What is the order of operand evaluation? (d) Are there restrictions on operand-evaluation side effects? Which must be considered primary design issues for arithmetic expressions?

- **A.** (a), (b) and (c)
- **B.** (a), (c) and (d)
- **C.** (a), (b) and (d)
- **D.** (a), (b), (c) and (d)

> [!TIP]
> **Correct answer: D. (a), (b), (c) and (d)**

## Solution

All four questions affect the meaning of an arithmetic expression. Precedence decides which operator binds first; associativity resolves operators of equal precedence; operand-evaluation order decides which operand is computed first; and side-effect restrictions determine whether that order can change program state. A language specification must define or deliberately leave constrained behavior for every one of these issues.

## Key Points

- Expression semantics depend on precedence, associativity, evaluation order and the treatment of side effects.

## Why the other options are incorrect

A omits side effects, B omits associativity, and C omits operand-evaluation order. Each omitted issue can change an expression's result or portability, so none of those partial lists is complete.
