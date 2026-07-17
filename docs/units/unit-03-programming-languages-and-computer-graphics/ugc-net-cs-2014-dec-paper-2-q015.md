# Question 15

*UGC NET CS · 2014 Dec Paper 2 · Programming in C++ · Overloading versus Overriding*

Which of the following differentiates between overloaded functions and overridden functions ?

- **A.** Overloading is a dynamic or runtime binding and overridden is a static or compile time binding.
- **B.** Overloading is a static or compile time binding and overridi ng is dynamic or runtime binding.
- **C.** Redefining a function in a friend class is called overloading , while redefining a function in a derived class is called as overridden function.
- **D.** Redefining a function in a derived class is called function ove rloading, while redefining a function in a friend class is called function overriding.

> [!TIP]
> **Correct answer: B. Overloading is a static or compile time binding and overridi ng is dynamic or runtime binding.**

## Solution

Function overloading selects among same-named functions with different parameter lists at compile time, so it is static binding. Overriding supplies a derived-class implementation of a base virtual function; when called through a base pointer or reference, the actual object's type selects the implementation at run time, so it is dynamic binding.

## Key Points

- Overloading resolves signatures at compile time; virtual overriding dispatches by dynamic object type at run time.

## Why the other options are incorrect

A reverses the binding categories. C and D incorrectly involve friend classes; friendship is unrelated to either overloading or overriding. Overriding specifically concerns inheritance and matching virtual-function signatures.
