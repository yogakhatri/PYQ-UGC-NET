# Question 48

*UGC NET CS · 2013 June Paper 3 · Programming in C · Arrays as Function Arguments*

When an array is passed as a parameter to a function which of the following statements is correct ?

- **A.** The function can change values in the original array.
- **B.** The function cannot change values in the original array.
- **C.** Results in compilation error.
- **D.** Results in runtime error.

> [!TIP]
> **Correct answer: A. The function can change values in the original array.**

## Solution

In a C function parameter, an array declaration is adjusted to a pointer to its first element. The function therefore accesses the caller's actual array storage through that pointer. Unless the parameter points to const-qualified elements, an assignment such as a[0]=value changes the original array element.

## Key Points

- C passes array access through a pointer to the original elements, not by copying the whole array.

## Why the other options are incorrect

B would be true only if a separate copy were made or mutation were forbidden with const; ordinary array passing does neither. Passing an array is valid C and does not itself cause a compile-time or run-time error, so C and D are false.
