# Question 29

*UGC NET CS · 2015 Dec Paper 3 · Object-Oriented Programming · Pure Virtual Functions and Abstract Classes*

Which of the following is used to make an Abstract class ?

- **1.** Making atleast one member function as pure virtual function
- **2.** Making atleast one member function as virtual function
- **3.** Declaring as Abstract class using virtual keyword
- **4.** Declaring as Abstract class using static keyword

> [!TIP]
> **Correct answer: 1. Making atleast one member function as pure virtual function**

## Solution

In C++, a class is abstract if it contains or inherits at least one pure virtual function that has not been overridden. A pure virtual declaration uses `virtual ReturnType f(...) = 0;`. Objects of the abstract class cannot be instantiated, although pointers and references to it are allowed.

## Key Points

- At least one unimplemented pure virtual function makes a C++ class abstract.

## Why the other options are incorrect

An ordinary virtual function may have an implementation and does not make the class abstract. C++ has no `abstract` declaration formed with a virtual or static class keyword.
