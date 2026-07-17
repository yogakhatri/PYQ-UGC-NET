# Question 17

*UGC NET CS · 2013 Dec Paper 2 · Programming in C · Scalar Initializations and Conversions*

Which of the following has compilation error in C ?

- **A.** int n = 32
- **B.** char ch = 65
- **C.** float f = (float) 3.2
- **D.** none of the above

> [!TIP]
> **Correct answer: D. none of the above**

## Solution

All three declarations are valid C. int n=32 initializes an integer. char ch=65 converts the representable integer value 65 to char, typically the code for 'A'. float f=(float)3.2 explicitly converts the double literal 3.2 to float. Hence none has a compilation error.

## Key Points

- C permits scalar initialization with representable converted values; distinguish a diagnostic warning from a language constraint error.

## Why the other options are incorrect

A, B and C each point to a legal scalar initialization. A compiler may warn about conversions under strict warning settings, but a warning is not a required C compilation error for these values and casts.
