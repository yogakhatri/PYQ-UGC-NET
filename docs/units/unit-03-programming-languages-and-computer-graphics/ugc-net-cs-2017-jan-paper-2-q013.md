# Question 13

*UGC NET CS · 2017 Jan Paper 2 · Programming in C++ · Storage Classes, Scope, and Linkage*

Which of the following storage classes have global visibility in C/C++ ?

- **1.** Auto
- **2.** Extern
- **3.** Static
- **4.** Register

> [!TIP]
> **Correct answer: 2. Extern**

## Solution

The extern storage-class specifier declares an object or function whose definition may occur elsewhere and normally has external linkage, allowing the same entity to be referenced across translation units. In the textbook terminology of the question, this is global visibility. Therefore option 2 is correct.

## Key Points

- Keep scope, storage duration, and linkage separate: extern is associated with external linkage; static commonly restricts file-scope linkage or extends local lifetime.

## Why the other options are incorrect

auto and register describe block-scope automatic objects. static does not by itself mean globally visible: at file scope it gives internal linkage, restricting the name to that translation unit, while a block-scope static name remains visible only in its block even though its lifetime spans the program.
