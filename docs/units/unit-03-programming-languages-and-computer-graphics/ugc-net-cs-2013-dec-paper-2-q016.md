# Question 16

*UGC NET CS · 2013 Dec Paper 2 · Programming in C · Pointers*

What does the following declaration mean ? int (*ptr) [10];

- **A.** ptr is an array of pointers of 10 integers.
- **B.** ptr is a pointer to an array of 10 integers.
- **C.** ptr is an array of 10 integers.
- **D.** none of the above.

> [!TIP]
> **Correct answer: B. ptr is a pointer to an array of 10 integers.**

## Solution

Read the C declaration outward from ptr. Parentheses make *ptr bind first, so ptr is a pointer. After the closing parenthesis comes [10], meaning the pointed-to object is an array of ten elements. The leading int makes each array element an integer. Thus ptr points to an array of 10 integers.

## Key Points

- In C declarations, parentheses change binding: int (*p)[10] is pointer-to-array, while int *p[10] is array-of-pointers.

## Why the other options are incorrect

An array of pointers would be written int *ptr[10] without parentheses around *ptr. The declaration does not allocate an array object named ptr; ptr itself is one pointer. Therefore 'none' is false.
