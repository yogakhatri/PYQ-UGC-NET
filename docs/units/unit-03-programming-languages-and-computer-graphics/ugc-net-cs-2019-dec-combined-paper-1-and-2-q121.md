# Question 121

*UGC NET CS · 2019 Dec Paper 1 And 2 · Programming in C++ · Overloading, Inheritance and Constructor Order*

Which of the following statements are true regarding C++? (a) Overloading gives the capability to an existing operator to operate on other data types. (b) Inheritance in object oriented programming provides support to reusability. (c) When object of a derived class is defined, first the constructor of derived class is executed then constructor of a base class is executed. (d) Overloading is a type of polymorphism. Choose the correct option from those given below :

- **1.** (a) and (b) only
- **2.** (a), (b) and (c) only
- **3.** (a), (b) and (d) only
- **4.** (b), (c) and (d) only

> [!TIP]
> **Correct answer: 3. (a), (b) and (d) only**

## Solution

Statement (a) is true: operator overloading defines an existing operator for user-defined operand types. Statement (b) is true because a derived class can reuse accessible base-class behaviour. Statement (c) is false—the base-class constructor runs first so the base subobject exists before the derived constructor body; destruction later occurs in reverse order. Statement (d) is true because overloading is compile-time or ad-hoc polymorphism. Thus (a), (b), and (d) only are correct, option 3.

## Key Points

- C++ construction goes base→derived, while overloading supplies compile-time polymorphism and inheritance supports reuse.

## Why the other options are incorrect

Option 1 omits the true polymorphism statement (d). Options 2 and 4 include the reversed construction order in (c). A derived object cannot be initialized safely before its base portion is constructed.
