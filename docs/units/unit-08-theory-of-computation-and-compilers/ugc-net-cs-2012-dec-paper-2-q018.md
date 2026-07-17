# Question 18

*UGC NET CS · 2012 Dec Paper 2 · Syntax Analysis · Grammar Precedence*

Given the grammar E -> E*F | F+E | F and F -> F-F | id, which is true?

- **1.** * has higher precedence than +
- **2.** - has higher precedence than *
- **3.** + and - have the same precedence
- **4.** + has higher precedence than *

> [!TIP]
> **Correct answer: 2. - has higher precedence than ***

## Solution

The nonterminal hierarchy determines precedence. Subtraction is generated inside F by F -> F-F, while multiplication and addition are generated at the E level. Whenever an E-level operator needs an F operand, a subtraction expression can already be formed as that F. Thus '-' binds more tightly than '*', making statement 2 true.

## Key Points

- In an expression grammar, operators introduced in a lower/deeper nonterminal generally have higher precedence.
- Here '-' is inside F, below the E-level operators.

## Why the other options are incorrect

The grammar does not support the usual arithmetic assumption that '*' must outrank '+': precedence must be read from these productions, not imported from convention. '+' and '-' are on different nonterminal levels, so they do not have equal precedence. The productions likewise do not establish '+' as having higher precedence than '*'.
