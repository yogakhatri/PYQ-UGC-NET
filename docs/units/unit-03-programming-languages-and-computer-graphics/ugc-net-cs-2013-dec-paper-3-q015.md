# Question 15

*UGC NET CS · 2013 Dec Paper 3 · Programming in C++ · Function Overloading as Ad-Hoc Polymorphism*

Which of the following correctly describes overloading of functions ?

- **A.** Virtual polymorphism
- **B.** Transient polymorphism
- **C.** Ad-hoc polymorphism
- **D.** Pseudo polymorphism

> [!TIP]
> **Correct answer: C. Ad-hoc polymorphism**

## Solution

Function overloading provides several implementations under one function name, with selection based on the compile-time argument types and arity. This is ad-hoc polymorphism because behavior is defined separately for a finite set of type signatures.

## Key Points

- Overloading is compile-time ad-hoc polymorphism; overriding through virtual methods is runtime subtype polymorphism.

## Why the other options are incorrect

Virtual polymorphism refers to subtype/dynamic dispatch, not overload resolution. 'Transient' and 'pseudo' are not the standard classification of function overloading.
