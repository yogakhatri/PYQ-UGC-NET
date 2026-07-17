# Question 18

*UGC NET CS · 2013 Dec Paper 3 · Programming in C++ · C and C++ Dynamic Allocation Systems*

C++ actually supports the following two complete dynamic systems :

- **A.** One defined by C++ and the other not defined by C.
- **B.** One defined by C and one specific to C++
- **C.** Both are specific to C++
- **D.** Both of them are improvements of C

> [!TIP]
> **Correct answer: B. One defined by C and one specific to C++**

## Solution

C++ retains C's dynamic allocation system, malloc/calloc/realloc with free, and adds its own type-aware new/delete system. new allocates storage and constructs objects; delete destroys objects and releases storage.

## Key Points

- Do not mix allocation families: pair malloc with free and new with delete.

## Why the other options are incorrect

The two systems are not both unique to C++, nor are both merely unspecified or generic improvements. One is inherited from the C library and the other is native C++ syntax and semantics.
