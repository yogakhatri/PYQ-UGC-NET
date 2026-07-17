# Question 12

*UGC NET CS · 2017 Jan Paper 2 · Programming in C++ · Function Overloading as Ad-Hoc Polymorphism*

Which one of the following is correct for overloaded functions in C++ ?

- **1.** Compiler sets up a separate function for every definition of function.
- **2.** Compiler does not set up a separate function for every definition of function.
- **3.** Overloaded functions cannot handle different types of objects.
- **4.** Overloaded functions cannot have same number of arguments.

> [!TIP]
> **Correct answer: 1. Compiler sets up a separate function for every definition of function.**

## Solution

Each overload is a distinct function with its own parameter-type list and, normally, its own definition and generated function body. During overload resolution the compiler chooses the best matching overload for a call. Thus the compiler sets up a separate function for every overload definition, as stated in option 1.

## Key Points

- Overloading reuses one name for several compile-time-distinguishable function signatures.

## Why the other options are incorrect

Option 2 denies the distinct implementations that overloading creates. Handling different argument types is the main purpose of overloading, so option 3 is false. Overloads may have the same number of arguments as long as parameter types or qualifying details distinguish their signatures, so option 4 is false.
