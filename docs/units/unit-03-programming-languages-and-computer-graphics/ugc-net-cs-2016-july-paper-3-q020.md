# Question 20

*UGC NET CS · 2016 July Paper 3 · Programming Language Concepts · Static, Stack-Dynamic and Heap-Dynamic Variables*

Match the following types of variables with the corresponding programming languages : (a) Static variables (i) Local variables in Pascal (b) Stack dynamic (ii) All variables in APL (c) Explicit heap dynamic (iii) Fortran 77 (d) Implicit heap dynamic (iv) All objects in JAVA Codes : (a) (b) (c) (d)

- **1.** (i) (iii) (iv) (ii)
- **2.** (iv) (i) (iii) (ii)
- **3.** (iii) (i) (iv) (ii)
- **4.** (ii) (i) (iii) (iv)

> [!TIP]
> **Correct answer: 3. (iii) (i) (iv) (ii)**

## Solution

Fortran 77 variables are the classic example of static allocation, so (a)→(iii). Pascal local variables are normally allocated on the run-time stack when a block is entered, so (b)→(i). Java objects created explicitly with `new` are explicit heap-dynamic objects, so (c)→(iv). APL variables acquire storage and often type/shape through assignment, illustrating implicit heap dynamics, so (d)→(ii). The sequence is (iii),(i),(iv),(ii), option 3.

## Key Points

- Static=fixed lifetime; stack-dynamic=block activation; explicit heap=`new`/allocation; implicit heap=assignment-driven allocation.

## Why the other options are incorrect

The other codes misclassify at least one lifetime. The key distinction is whether allocation is fixed before execution, tied to block activation, explicitly requested by the program, or triggered implicitly by assignment.
