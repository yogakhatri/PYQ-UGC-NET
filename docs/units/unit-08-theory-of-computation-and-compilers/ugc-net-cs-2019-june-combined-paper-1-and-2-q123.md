# Question 123

*UGC NET CS · 2019 June Paper 1 And 2 · Code Generation and Optimization · Constant Folding*

Replacing the expression 4*2.14 by 8.56 is known as:

- **1.** constant folding
- **2.** induction variable
- **3.** strength reduction
- **4.** code reduction

> [!TIP]
> **Correct answer: 1. constant folding**

## Solution

Both operands in 4*2.14 are compile-time constants. Evaluating the multiplication during compilation and replacing it with the constant result 8.56 is constant folding. It removes the need to perform that multiplication at run time.

## Key Points

- Constant folding evaluates constant-only expressions at compile time.

## Why the other options are incorrect

- **Induction-variable optimization:** simplifies variables that change regularly in loops.
- **Strength reduction:** replaces an expensive operation with a cheaper equivalent, such as multiplication by a shift.
- **Code reduction:** is a broad description, not the specific named transformation.
