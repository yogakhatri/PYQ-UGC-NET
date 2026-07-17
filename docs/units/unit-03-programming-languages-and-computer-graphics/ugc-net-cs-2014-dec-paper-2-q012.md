# Question 12

*UGC NET CS · 2014 Dec Paper 2 · Programming in C · Reading Complex Declarators*

What does the C declaration char *(*(*a[N])())(); mean?

- **A.** A pointer to a function returning an array of N pointers to functions returning character pointers.
- **B.** A function returning an array of N pointers to functions returning pointers to characters.
- **C.** An array of N pointers to functions returning pointers to characters.
- **D.** An array of N pointers to functions returning pointers to functions returning pointers to characters.

> [!TIP]
> **Correct answer: D. An array of N pointers to functions returning pointers to functions returning pointers to characters.**

## Solution

Read outward from a. First, a[N] says a is an array of N elements. *a[N] makes each element a pointer; (*a[N])() makes it a pointer to a function. That function returns another pointer, and the next () shows that pointer targets another function. The outer char * says the second function returns a pointer to char. Hence a is an array of N pointers to functions returning pointers to functions returning pointers to char.

## Key Points

- For complex C declarators, start at the identifier and spiral outward, respecting parentheses before prefix stars.

## Why the other options are incorrect

A and B incorrectly make a function return an array, which C does not permit. C stops after only one function level and misses the second parenthesized function call. D alone reflects both pointer-to-function layers.
