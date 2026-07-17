# Question 29

*UGC NET CS · 2013 Dec Paper 2 · Linking and Loading · Program Relocation*

The process of assigning load addresses to the va rious parts of the program and adjusting the code and data in the program to reflect the assigned addresses is called _______.

- **A.** Symbol resolution
- **B.** Parsing
- **C.** Assembly
- **D.** Relocation

> [!TIP]
> **Correct answer: D. Relocation**

## Solution

Relocation assigns actual load addresses to program sections and adjusts address-sensitive instructions and data so they refer to the correct locations. A relocating linker or loader uses relocation entries emitted by the assembler to perform these changes.

## Key Points

- Relocation = place program parts at load addresses and patch address-dependent code/data to match those placements.

## Why the other options are incorrect

Symbol resolution matches references with definitions but does not by itself adjust every address after placement. Parsing analyzes grammatical structure, and assembly translates assembly language into object code. The address-adjustment process specifically is relocation.
