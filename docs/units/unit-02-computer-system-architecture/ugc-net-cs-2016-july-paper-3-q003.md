# Question 3

*UGC NET CS · 2016 July Paper 3 · Microprocessor Programming · 8085 DAD Register-Pair Instruction*

Which of the following in 8085 microprocessor performs HL = HL + DE ?

- **1.** DAD D
- **2.** DAD H
- **3.** DAD B
- **4.** DAD SP

> [!TIP]
> **Correct answer: 1. DAD D**

## Solution

In 8085, `DAD rp` performs 16-bit addition `HL ← HL + rp`, where `rp` is a register pair. The code letter D denotes the DE pair, so `DAD D` performs `HL ← HL + DE`.

## Key Points

- 8085 `DAD rp`: HL is the implicit destination and the named register pair is the 16-bit source.

## Why the other options are incorrect

`DAD H` adds HL to itself, `DAD B` adds BC, and `DAD SP` adds the stack pointer. The destination remains HL in every case; the operand name selects the source pair.
