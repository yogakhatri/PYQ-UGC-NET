# Question 19

*UGC NET CS · 2016 July Paper 3 · Programming Language Concepts · Abstract and Parameterized Data Types*

Given the following statements : (A) To implement Abstract Data Type, a programming language require a syntactic unit to encapsulate type definition. (B) To implement ADT, a programming language requires some primitive operations that are built in the language processor. (C) C++, Ada, Java 5.0, C#2005 provide support for parameterised ADT. Which one of the following options is correct ?

- **1.** (A), (B) and (C) are false.
- **2.** (A) and (B) are true; (C) is false.
- **3.** (A) is true; (B) and (C) are false.
- **4.** (A), (B) and (C) are true.

> [!TIP]
> **Correct answer: 4. (A), (B) and (C) are true.**

## Solution

A is true: an ADT needs a language construct such as a class, package, or module to encapsulate its representation and operation declarations. B is true in the intended language-design sense: the processor must support primitive mechanisms for defining, creating, accessing, and enforcing the abstraction. C is true: C++ templates, Ada generics, Java 5 generics, and C# 2005 generics support parameterized ADTs. Hence all three statements are true.

## Key Points

- ADT support combines encapsulating syntax, controlled primitive operations, and—when generic—type parameters.

## Why the other options are incorrect

Options 1–3 each reject at least one required or historically supported feature. Parameterization lets one abstraction—such as Stack<T>—work for multiple element types without duplicating its definition.
