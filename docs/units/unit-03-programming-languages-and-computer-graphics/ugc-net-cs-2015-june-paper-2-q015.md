# Question 15

*UGC NET CS · 2015 June Paper 2 · Programming in C++ · Private Base Members*

When the inheritance is private, the private methods in base class are __________ in the derived class (in C++).

- **1.** inaccessible
- **2.** accessible
- **3.** protected
- **4.** public

> [!TIP]
> **Correct answer: 1. inaccessible**

## Solution

A base class's private members can be accessed directly only by the base class itself and its friends. The choice of public, protected, or private inheritance changes how inherited public and protected members are exposed through the derived class; it does not grant the derived class access to base-private methods. They remain inaccessible to derived-class code.

## Key Points

- Inheritance mode remaps public/protected access; base-private members remain inaccessible to the derived class.

## Why the other options are incorrect

Private inheritance converts inherited public and protected interfaces to private accessibility in the derived class, but it does not convert base-private members to accessible, protected, or public members. Therefore options 2–4 confuse inheritance mode with the base member's own access control.
