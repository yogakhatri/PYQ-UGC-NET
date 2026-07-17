# Question 12

*UGC NET CS · 2016 July Paper 2 · Programming in C · Reading Complex Declarators*

What does the C declaration int (*f())[]; declare?

- **1.** a function returning a pointer to an array of integers.
- **2.** a function returning an array of pointers to integers.
- **3.** array of functions returning pointers to integers.
- **4.** an illegal statement.

> [!TIP]
> **Correct answer: 1. a function returning a pointer to an array of integers.**

## Solution

Parse from the identifier outward. f() says f is a function. The parentheses in (*f()) make the function's return value a pointer. The following [] says that pointer points to an array, and the leading int says the array elements are integers. Hence f is a function returning a pointer to an array of integers.

## Key Points

- Read C declarators inside-out, respecting that postfix () and [] bind more tightly than prefix * unless parentheses change the grouping.

## Why the other options are incorrect

C functions cannot return arrays directly, so option 2 misreads the binding. Arrays of functions are illegal in C, ruling out option 3. A pointer to an incomplete array type can be declared, so the empty array bound does not make this declaration illegal.
