# Question 11

*UGC NET CS · 2017 Jan Paper 2 · Programming in C++ · Functions and Parameter Passing*

Which of the following cannot be passed to a function in C++ ?

- **1.** Constant
- **2.** Structure
- **3.** Array
- **4.** Header file

> [!TIP]
> **Correct answer: 4. Header file**

## Solution

A function argument must be an expression or object whose value/reference can be supplied to a parameter. Constants can be passed by value, structures can be passed by value or reference, and an array argument is passed through a pointer-like adjustment or can be bound to an array reference. A header file is source text included during preprocessing, not a runtime value or object. Therefore option 4 is correct.

## Key Points

- Headers participate in translation through #include; function arguments exist in the C++ expression and object model.

## Why the other options are incorrect

A literal such as 5 is a valid constant argument. A structure object is an ordinary object that may be copied or referenced. An array name commonly supplies the address of its first element to a pointer parameter, despite the informal phrase 'passing an array.'
