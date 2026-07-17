# Question 37

*UGC NET CS · 2016 July Paper 3 · Object-Oriented Programming · Constructor Return-Type Semantics*

Implicit return type of a class constructor is :

- **1.** not of class type itself
- **2.** class type itself
- **3.** a destructor of class type
- **4.** a destructor not of class type

> [!TIP]
> **Correct answer: 2. class type itself**

## Solution

In the textbook terminology used by this item, a constructor's implicit result is an initialized instance of its own class, so the intended answer is 'class type itself,' option 2. For example, constructing `Widget` yields a `Widget` object/reference to the caller.

## Key Points

- A constructor has no declared return type; conceptually its construction expression yields an instance of the class being constructed.

## Why the other options are incorrect

Option 1 contradicts the intended object type, while options 3 and 4 confuse construction with destruction. Formally, Java and C++ constructors do not declare a return type—not even `void`; calling the class type an 'implicit return type' is explanatory shorthand, not a normal method signature.
