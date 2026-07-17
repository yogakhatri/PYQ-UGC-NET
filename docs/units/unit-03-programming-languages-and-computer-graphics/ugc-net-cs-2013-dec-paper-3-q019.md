# Question 19

*UGC NET CS · 2013 Dec Paper 3 · Programming in C++ · new and delete Operators*

Important advantage of using new and delete operators in C++ is

- **A.** Allocation of memory
- **B.** Frees the memory previously allocated
- **C.** Initialization of memory easily
- **D.** Allocation of memory and frees the memory previously allocated.

> [!TIP]
> **Correct answer: D. Allocation of memory and frees the memory previously allocated.**

## Solution

new obtains dynamic storage (and initializes/constructs the object), while delete destroys the object and releases storage previously obtained with new. Together they provide the allocation and deallocation lifecycle.

## Key Points

- Use new/delete as a matched pair; in modern C++, prefer RAII containers and smart pointers to manual ownership.

## Why the other options are incorrect

A and B each name only half of the pair's purpose. C notes an advantage of new over raw byte allocation but omits the central allocation/deallocation combination asked by the item.
