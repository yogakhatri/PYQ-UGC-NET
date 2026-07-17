# Question 5

*UGC NET CS · 2016 July Paper 3 · Instruction Set Architecture · Displacement Addressing Mode*

The _____ addressing mode is similar to register indirect addressing mode, except that an offset is added to the contents of the register. The offset and register are specified in the instruction.

- **1.** Base indexed
- **2.** Base indexed plus displacement
- **3.** Indexed
- **4.** Displacement

> [!TIP]
> **Correct answer: 4. Displacement**

## Solution

Displacement addressing forms the effective address by adding a constant displacement encoded in the instruction to the contents of a specified register: EA=(register)+offset. This is exactly register-indirect addressing extended by an offset, so option 4 is correct.

## Key Points

- Displacement mode computes EA=register contents+instruction-supplied offset.

## Why the other options are incorrect

Base-indexed addressing combines a base and an index register. Base-indexed-plus-displacement uses two register contributions plus a constant. Indexed addressing is a specific displacement-style variant, but the generic mode defined by the question's one-register-plus-offset formula is displacement addressing.
