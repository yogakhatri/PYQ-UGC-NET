# Question 4

*UGC NET CS · 2017 Jan Paper 3 · Instruction Set Architecture · Addressing Modes and Operand Location*

Match the following : Addressing Mode Location of operand a. Implied i. Registers which are in CPU b. Immediate ii. Register specifies the address of the operand. c. Register iii. Specified in the register d. Register Indirect iv. Specified implicitly in the definition of instruction Codes : a b c d

- **1.** iv iii i ii
- **2.** iv i iii ii
- **3.** iv ii i iii
- **4.** iv iii ii i

> [!TIP]
> **Correct answer: 1. iv iii i ii**

## Solution

Implied addressing has no explicit operand field because the operand is fixed by the instruction definition, so a→iv. An immediate operand is contained in the instruction word and is therefore available with the instruction in the instruction register, matching the paper's wording b→iii. Register addressing names a CPU register that contains the operand, so c→i. Register-indirect addressing names a register that contains the operand's memory address, so d→ii. The code iv, iii, i, ii is option 1.

## Key Points

- Immediate=value in instruction; register=value in named CPU register; register indirect=address in named register; implied=operand fixed by opcode.

## Why the other options are incorrect

The other codes confuse a register that holds an operand with one that holds an address, or treat an explicitly encoded immediate value as implied. Register and register-indirect addressing differ by exactly this extra level of indirection.
