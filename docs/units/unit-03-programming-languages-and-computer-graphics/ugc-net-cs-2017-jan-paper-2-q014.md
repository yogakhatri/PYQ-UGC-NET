# Question 14

*UGC NET CS · 2017 Jan Paper 2 · Programming in C++ · Non-Overloadable Operators*

Which of the following operators cannot be overloaded in C/C++ ?

- **1.** Bitwise right shift assignment
- **2.** Address of
- **3.** Indirection
- **4.** Structure reference

> [!TIP]
> **Correct answer: 4. Structure reference**

## Solution

In C++, the member-access operator . (called 'structure reference' here) cannot be overloaded. Its built-in meaning is fundamental to selecting a member from an object. Therefore option 4 is correct.

## Key Points

- Common non-overloadable C++ operators include ., .*, ::, ?:, and sizeof.

## Why the other options are incorrect

The compound right-shift assignment operator >>= can be overloaded. Unary address-of & and unary indirection * can also be overloaded for class or enumeration operands. The question says C/C++, but user-defined operator overloading is a C++ feature; plain C has no such mechanism.
