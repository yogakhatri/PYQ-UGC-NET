# Question 20

*UGC NET CS · 2014 Dec Paper 3 · Lexical Analysis · Scanner Token Counting*

How many tokens will a scanner generate for the statement `x = x * (a + b) - 5;`?

- **A.** 12
- **B.** 11
- **C.** 10
- **D.** 07

> [!TIP]
> **Correct answer: A. 12**

## Solution

A scanner emits one token for each identifier, operator, delimiter, and literal. Reading left to right gives: x, =, x, *, (, a, +, b, ), −, 5, ;. That is 12 tokens. Spaces are only separators and do not become tokens.

## Key Points

- Token counting is lexical: identifiers, literals, operators, parentheses, and the terminating semicolon each count separately.

## Why the other options are incorrect

Counts 11, 10, and 7 arise from omitting punctuation such as parentheses or the semicolon, or from treating a parenthesized expression as one token. Parsing groups expressions later; lexical analysis still emits each operator and delimiter separately.
