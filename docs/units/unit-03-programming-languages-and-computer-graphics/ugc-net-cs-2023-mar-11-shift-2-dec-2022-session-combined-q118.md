# Question 118

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Programming in C++ · Templates and class hierarchies*

Match List I with List II LISTI LIST II A. If the implementation of generated or derived classes differ only through a parameter we have I. to use class hierarchy B. If the actual types of objects used cannot be known at compile time, then we have II. improved run time efficiency C. If inline opcrations are ossential and templates are used then we have III. to use templates D. To gain access to differing instances for derived classes through base we have IV. to use explicit casting Choose the correct answer from the options given below:

- **1.** A-I, B-II, C-IV, D-I
- **2.** A-III, B-I, C-II, D-IV
- **3.** A-I, B-III, C-II, D-IV
- **4.** A-II, B-I, C-III, D-IV

> [!TIP]
> **Correct answer: 2. A-III, B-I, C-II, D-IV**

## Solution

Parameter-only variation suggests templates (A–III). Runtime-unknown types require a class hierarchy and dynamic polymorphism (B–I). Templates enable compile-time inlining and runtime efficiency (C–II). Recovering a derived instance through a base reference may require explicit casting (D–IV).

## Key Points

- Templates provide compile-time polymorphism; class hierarchies provide runtime polymorphism.

## Why the other options are incorrect

Other mappings confuse compile-time generic programming with runtime polymorphism.
