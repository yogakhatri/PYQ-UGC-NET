# Question 40

*UGC NET CS · 2016 July Paper 3 · Object-Oriented Programming · Instantiation of Abstract Classes*

Which of the following statements is correct ?

- **1.** Every class containing abstract method must not be declared abstract.
- **2.** Abstract class cannot be directly initiated with ‘new’ operator.
- **3.** Abstract class cannot be initiated.
- **4.** Abstract class contains definition of implementation.

> [!TIP]
> **Correct answer: 2. Abstract class cannot be directly initiated with ‘new’ operator.**

## Solution

An abstract class cannot be instantiated directly with the `new` operator; it exists to provide a partial abstraction and must be realized through a concrete subclass. Therefore option 2 is the precise correct statement.

## Key Points

- Abstract classes may define state, constructors, and concrete methods, but cannot be directly instantiated.

## Why the other options are incorrect

A class containing an abstract method must itself be declared abstract, so option 1 reverses the rule. Option 3 is too broad: abstract-class constructors and implemented members can participate when a concrete subclass is instantiated, even though the abstract class cannot be instantiated directly. Option 4 is not universally true because an abstract class need not provide a particular implementation.
