# Question 41

*UGC NET CS · 2013 June Paper 3 · Instruction Set Architecture · Addressing Modes*

Which one of the following is not an addressing mode ?

- **A.** Register indirect
- **B.** Autoincrement
- **C.** Relative indexed
- **D.** Immediate operand

> [!TIP]
> **Correct answer: Intended answer: D, Immediate operand. The standard mode name is immediate addressing, so the question relies on terminology and is not ideally worded.**

## Solution

Register indirect, autoincrement and relative indexed are all conventional names of effective-address calculation modes. 'Immediate operand' describes where the operand value appears—inside the instruction—rather than giving the conventional mode name, which is 'immediate addressing.' On that literal naming distinction, D is the intended choice. Be aware that architecture texts routinely do classify immediate addressing as an addressing mode, making the wording ambiguous if 'immediate operand' is treated as shorthand for it.

## Key Points

- Distinguish the immediate operand (value embedded in the instruction) from the conventional term immediate addressing mode.

## Why the other options are incorrect

A obtains the effective address from a register's contents. B uses a register indirectly and then increments it. C combines PC-relative and indexed displacement ideas. All three are recognizably named addressing modes, whereas D is phrased as an operand type rather than a mode name.
