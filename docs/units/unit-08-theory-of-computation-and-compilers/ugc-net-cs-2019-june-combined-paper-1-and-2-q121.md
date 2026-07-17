# Question 121

*UGC NET CS · 2019 June Paper 1 And 2 · Runtime System · Symbol Table*

Which data structure is used by the compiler for managing variables and their attributes?

- **1.** Binary tree
- **2.** Link list repp.
- **3.** Symbol table -
- **4.** Parse table

> [!TIP]
> **Correct answer: 3. Symbol table -**

## Solution

A compiler stores each identifier and its attributes in a symbol table. Typical attributes include type, scope, storage location, size, parameter information and linkage. Compiler phases consult and update this table during semantic analysis, intermediate-code generation and later stages.

## Key Points

- The symbol table maps source-language names to semantic and storage information.

## Why the other options are incorrect

A binary tree or linked list may be used internally to implement a table, but neither is the compiler abstraction being asked for. A parse table guides syntax analysis and does not hold variable attributes.
