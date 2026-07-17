# Question 15

*UGC NET CS · 2017 Nov Paper 2 · Programming in C++ · Class and Function Templates*

Which of the following is not correct (in C++) ?

- **1.** Class templates and function templates are instantiated in the same way.
- **2.** Class templates differ from function templates in the way they are initiated.
- **3.** Class template is initiated by defining an object using the template argument.
- **4.** Class templates are generally used for storage classes.

> [!TIP]
> **Correct answer: 1. Class templates and function templates are instantiated in the same way.**

## Solution

Class templates and function templates are not instantiated in the same way. A class-template specialization normally requires explicit template arguments in its type, as in `Box<int> b;` (subject to modern deduction features). A function template can often infer its template arguments from a call, as in `max(2,3)`. Therefore statement 1 is the incorrect statement and is the requested answer.

## Key Points

- Function-template arguments are often deduced from call arguments; class templates conventionally form explicit specialized types used to create objects.

## Why the other options are incorrect

Statement 2 correctly notes the different instantiation mechanisms. Statement 3 describes the traditional explicit construction of an object from a class-template specialization. Statement 4 reflects the common use of class templates for generic container/storage classes such as stacks, lists, and vectors.
