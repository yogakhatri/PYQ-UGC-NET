# Question 35

*UGC NET CS · 2017 Jan Paper 2 · System Software · Linking and External-Symbol Resolution*

Which of the following statement(s) regarding a linker software is/are true ? I. A function of a linker is to combine several object modules into a single load module. II A function of a linker is to replace absolute references in an object module by symbolic references to locations in other modules.

- **1.** Only I
- **2.** Only II
- **3.** Both I and II
- **4.** Neither I nor II

> [!TIP]
> **Correct answer: 1. Only I**

## Solution

A linker combines separately assembled or compiled object modules and required libraries into one executable or load module, so statement I is true. It also resolves symbolic external references and relocates addresses. Statement II reverses that direction: the linker replaces unresolved symbolic references with resolved addresses, not absolute references with symbolic ones. Therefore only I is true, option 1.

## Key Points

- Compiler/assembler produces object modules with symbols and relocation records; linker combines modules, resolves symbols, and relocates addresses.

## Why the other options are incorrect

Options 2 and 3 accept the reversed description in II. Option 4 incorrectly denies the linker's central module-combination role.
