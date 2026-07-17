# Question 51

*UGC NET CS · 2013 June Paper 3 · Programming in C · Declaration and Statement Syntax Errors*

Trace the error in this program: void main() { int *b, &a; *b = 20 printf("%d, %d", a, *b) }

- **A.** No error
- **B.** Logical error
- **C.** Syntax error
- **D.** Semantic error

> [!TIP]
> **Correct answer: C. Syntax error**

## Solution

The fragment cannot be parsed as valid C. In the declaration int *b, &a;, the token & cannot introduce a C variable declarator. The printed statements also omit required semicolons after *b=20 and the printf call. These are syntax violations detected during compilation, before any execution occurs.

## Key Points

- Classify the earliest failure: invalid declaration grammar and missing semicolons make this a syntax error.

## Why the other options are incorrect

A ignores several invalid tokens. A logical error describes a compilable program that computes the wrong result. A semantic/runtime issue such as dereferencing an uninitialized pointer would matter only after the syntax errors were repaired; the source as printed fails earlier.
