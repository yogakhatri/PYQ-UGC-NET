# Question 33

*UGC NET CS · 2014 Dec Paper 2 · System Software and Translation · Two-Pass Assembler Symbol Table*

In a two-pass assembler, symbol table is

- **A.** Generated in first pass
- **B.** Generated in second pass
- **C.** Not generated at all
- **D.** Generated and used only in second pass

> [!TIP]
> **Correct answer: A. Generated in first pass**

## Solution

Pass 1 scans the source, maintains the location counter and records each label with its assigned address in the symbol table. This resolves forward references later. Pass 2 consults that completed table to replace symbols with addresses and emit object code.

## Key Points

- Two-pass assembler: pass 1 builds addresses/symbols; pass 2 generates code using them.

## Why the other options are incorrect

Generating the table only in pass 2 would leave forward references unresolved when they are needed. It is certainly generated, so C is false. D is false because creation occurs in pass 1 even though use continues in pass 2.
