# Question 30

*UGC NET CS · 2013 Dec Paper 2 · Syntax Analysis · Top-Down and Bottom-Up Derivations*

Which of the following derivations does a top-down parser use while parsing an input string ? The input is scanned from left to right.

- **A.** Leftmost derivation
- **B.** Leftmost derivation traced out in reverse
- **C.** Rightmost derivation traced out in reverse
- **D.** Rightmost derivation

> [!TIP]
> **Correct answer: A. Leftmost derivation**

## Solution

A top-down parser begins with the start symbol and repeatedly expands the leftmost unexpanded nonterminal to predict the input from left to right. It therefore constructs a leftmost derivation of the input string.

## Key Points

- Top-down parsing produces a leftmost derivation; bottom-up LR parsing produces a rightmost derivation in reverse.

## Why the other options are incorrect

A bottom-up LR parser reconstructs a rightmost derivation in reverse. The reverse-derivation descriptions therefore belong to bottom-up parsing, while a rightmost derivation is not the standard expansion strategy of a left-to-right top-down parser.
