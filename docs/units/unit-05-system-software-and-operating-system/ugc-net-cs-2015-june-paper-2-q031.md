# Question 31

*UGC NET CS · 2015 June Paper 2 · System Software · Assembler Tables and Directives*

Match the following : (a) Forward Reference Table (i) Assembler directive (b) Mnemonic Table (ii) Uses array data structure (c) Segment Register Table (iii) Contains machine OP code (d) EQU (iv) Uses linked list data structure Codes : (a) (b) (c) (d)

- **1.** (ii) (iii) (iv) (i)
- **2.** (iii) (iv) (ii) (i)
- **3.** (iv) (i) (iii) (ii)
- **4.** (iv) (iii) (ii) (i)

> [!TIP]
> **Correct answer: 4. (iv) (iii) (ii) (i)**

## Solution

A forward reference names a symbol before its definition, so an assembler records each unresolved use in a linked list attached to that symbol: (a)–(iv). A mnemonic table maps instruction mnemonics to information including the machine opcode: (b)–(iii). The segment-register table is represented as an indexed array: (c)–(ii). `EQU` is an assembler directive that assigns a value to a symbol: (d)–(i). The sequence is therefore `(iv), (iii), (ii), (i)`.

## Key Points

- FRT → linked lists; mnemonic table → machine opcodes; segment-register table → array; EQU → assembler directive.

## Why the other options are incorrect

The other codes interchange structures with their contents or roles. In particular, a mnemonic table contains opcodes rather than being an assembler directive, and `EQU` is a directive rather than a data structure. Only option 4 preserves all four associations.
