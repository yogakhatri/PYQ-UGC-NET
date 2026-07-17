# Question 39

*UGC NET CS · 2012 Dec Paper 2 · Programming in C++ · C++ Type Categories*

Match C++ data types: a. User-defined type; b. Built-in type; c. Derived type; d. Long double. 1. Qualifier; 2. Union; 3. Void; 4. Pointer.

- **1.** a-2,b-3,c-4,d-1
- **2.** a-3,b-1,c-4,d-2
- **3.** a-4,b-1,c-2,d-3
- **4.** a-3,b-4,c-1,d-2

> [!TIP]
> **Correct answer: 1. a-2,b-3,c-4,d-1**

## Solution

A union is a user-defined type, so a-2. Void belongs to the built-in fundamental types, so b-3. A pointer is constructed from another type and is therefore derived, so c-4. In the terminology used by the question, long qualifies/modifies double, so d-1. The complete match is a-2, b-3, c-4, d-1.

## Key Points

- C++ type examples: union is user-defined, void is built-in, pointer is derived, and long modifies double in long double.

## Why the other options are incorrect

The other codes classify void as user-defined or derived, treat a pointer as built-in/user-defined, or fail to associate union with user-defined type. Those assignments conflict with the standard introductory C++ type hierarchy.
