# Question 18

*UGC NET CS · 2013 Dec Paper 2 · Programming in C++ · Non-Overloadable Operators*

Which of the following operators cannot be overloaded in C++?

- **A.** *
- **B.** +=
- **C.** ==
- **D.** ::

> [!TIP]
> **Correct answer: D. ::**

## Solution

C++ permits overloading arithmetic operators such as *, compound assignment operators such as +=, and comparison operators such as ==, subject to the language's operator-overload rules. The scope-resolution operator :: is fixed by the language grammar and cannot be overloaded.

## Key Points

- Non-overloadable C++ operators include ::, ., .*, ?: and sizeof; scope resolution is the answer here.

## Why the other options are incorrect

Options A, B and C all name overloadable operators. Overloading cannot change their precedence, associativity or number of operands, but user-defined behavior may be supplied when at least one operand has class or enumeration type.
