# Question 40

*UGC NET CS · 2017 Jan Paper 3 · Java Programming · Abstract Classes and Inheritance*

Which of the following statement(s) with regard to an abstract class in JAVA is/are TRUE ? I. An abstract class is one that is not used to create objects. II. An abstract class is designed only to act as a base class to be inherited by other classes.

- **1.** Only I
- **2.** Only II
- **3.** Neither I nor II
- **4.** Both I and II

> [!TIP]
> **Correct answer: 4. Both I and II**

## Solution

A Java abstract class cannot be instantiated directly, so statement I is true. Its purpose is to provide a partially implemented base type—shared state, concrete behavior, and possibly abstract methods—that subclasses inherit and complete, so statement II is true in the conventional object-oriented sense used by the question. Therefore both statements are true and option 4 is correct.

## Key Points

- Abstract class = non-instantiable base type that can mix implemented and abstract members for subclasses.

## Why the other options are incorrect

Options 1 and 2 each discard one defining property, while option 3 discards both. References may have an abstract-class type, but any actual object must be an instance of a concrete subclass (including an anonymous subclass), not the abstract class itself.
