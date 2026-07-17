# Question 32

*UGC NET CS · 2010 June Paper 2 · Runtime System · Activation Tree and Records*

Which of the following expression is represented by the parse tree ?

- **A.** (A + B) * C
- **B.** A + * BC
- **C.** A + B * C
- **D.** A * C + B

> [!TIP]
> **Correct answer: A. (A + B) * C**

## Solution

The parse-tree root is multiplication. Its left child is a plus node with leaves A and B; its right child is C. Reading children recursively gives (A+B)*C.

## Key Points

- Parenthesize each internal parse-tree node around the expressions represented by its children.

## Why the other options are incorrect

C omits the grouping and would root the tree at +. B is malformed prefix/infix notation, and D pairs different operands under multiplication.
