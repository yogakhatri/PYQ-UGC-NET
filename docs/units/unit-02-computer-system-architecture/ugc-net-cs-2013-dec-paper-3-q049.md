# Question 49

*UGC NET CS · 2013 Dec Paper 3 · Instruction Set Architecture · Addressing Modes*

Match the following : List – I List – II a. Indexed Addressing i. is not used when an operand is moved from memory into a register or from a register to memory. b. Direct Addressing ii. Memory address is computed by adding up two registers plus an (optional) offset. c. Register Addressing iii. Addressing memory by giving a register plus a content offset. d. Base- Indexed Addressing iv. can only be used to access global variables whose address is known at compile time. Codes : a b c d

- **A.** ii i iv iii
- **B.** ii iv i iii
- **C.** iii iv i ii
- **D.** iii i iv ii

> [!TIP]
> **Correct answer: C. iii iv i ii**

## Solution

Match each mode by how it obtains the operand. Indexed addressing uses a register plus a constant/displacement to address memory, so a→iii. Direct addressing embeds a fixed memory address and is suitable for globals known at compile time, so b→iv. Register addressing names a register and does not use a memory address for the operand, so c→i. Base-indexed addressing combines two registers, optionally with an offset, so d→ii. The order is iii, iv, i, ii.

## Key Points

- Direct=fixed address; register=operand in register; indexed=register+displacement; base-indexed=base+index(+displacement).

## Why the other options are incorrect

A and B treat indexed addressing as the two-register form, which belongs to base-indexed addressing. D gets the first mapping right but swaps direct/register or base-indexed behavior. Checking all four positions leaves only C.
