# Question 61

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Object-Oriented Programming · Abstract Class*

3 option 1D=457301 810-87011 Allowing different derived classes to be used interchangeably through the interface provided by a common base class is called

- **1.** Derived polymorphism
- **2.** Compile time polymorphism
- **3.** Static polymorphism
- **4.** Run time polymorphism

> [!TIP]
> **Correct answer: 4. Run time polymorphism**

## Solution

Using different derived objects through a common base interface relies on virtual dispatch: the actual overridden method is selected from the runtime object type. This is runtime polymorphism.

## Key Points

- Base reference + virtual method + derived object = runtime polymorphism.

## Why the other options are incorrect

Compile-time/static polymorphism refers to overloading or templates; ‘derived polymorphism’ is not the standard category.
