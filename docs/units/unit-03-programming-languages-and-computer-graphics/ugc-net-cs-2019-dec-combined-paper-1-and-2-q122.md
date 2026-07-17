# Question 122

*UGC NET CS · 2019 Dec Paper 1 And 2 · Programming in C · Pointer Declarations and Address-of Operator*

Assume r and a are declared int variables. Which statements are legal in C? (a) int *P=&44; (b) int *P=&r; (c) int P=&a; (d) int P=a;

- **1.** (a) and (b)
- **2.** (b) and (c)
- **3.** (b) and (d)
- **4.** (a) and (d)

> [!TIP]
> **Correct answer: 3. (b) and (d)**

## Solution

Statement (a) is illegal because 44 is an integer literal, not an lvalue object whose address can be taken. Statement (b) is legal: &r has type pointer to int and initializes int *P. Statement (c) attempts to initialize an int with an int pointer and violates the required type constraints. Statement (d) is an ordinary integer initialization and is legal. Hence (b) and (d), option 3.

## Key Points

- Unary &: operand must designate an addressable object; pointer and integer initializers must also have compatible types.

## Why the other options are incorrect

Options 1 and 4 include the invalid address-of-literal expression. Option 2 includes the pointer-to-integer mismatch in (c). A permissive compiler may issue a diagnostic and extension-convert a pointer, but that does not make (c) a legal strictly conforming C statement.
