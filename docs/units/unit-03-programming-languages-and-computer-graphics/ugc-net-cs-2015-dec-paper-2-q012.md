# Question 12

*UGC NET CS · 2015 Dec Paper 2 · Object-Oriented Programming · Public Inheritance and Code Reuse*

Consider the following two statements : (a) A publicly derived class is a subtype of its base class. (b) Inheritance provides for code reuse. Which one of the following statements is correct ?

- **1.** Both the statements (a) and (b) are correct.
- **2.** Neither of the statements (a) and (b) are correct.
- **3.** Statement (a) is correct and (b) is incorrect.
- **4.** Statement (a) is incorrect and (b) is correct.

> [!TIP]
> **Correct answer: 1. Both the statements (a) and (b) are correct.**

## Solution

Under public inheritance in C++, a derived object can be used where an accessible base object is expected; this models the ‘is-a’ subtype relation. Inheritance also lets the derived class reuse accessible data and member functions implemented by the base class. Thus both statements are correct.

## Key Points

- Public inheritance supports substitutability and implementation reuse.

## Why the other options are incorrect

Options 2–4 deny at least one standard effect of public inheritance. Private inheritance would not express the same public subtype relationship, but the question explicitly says publicly derived.
