# Question 63

*UGC NET CS · 2018 Dec Paper 1 And 2 · Basic Computer Organization and Design · Auto-Increment Addressing Mode*

Consider: (i) Auto-increment addressing is useful for creating self-relocating code. (ii) Including auto-increment addressing in an ISA requires an additional ALU for effective-address calculation. (iii) The increment amount depends on the size of the data item accessed. Which statements are true?

- **1.** (i) and (ii) only
- **2.** (ii) and (iii) only
- **3.** (iii) only
- **4.** (ii) only

> [!TIP]
> **Correct answer: 3. (iii) only**

## Solution

Statement (i) is false: auto-increment changes a register after an operand access; position-independent/self-relocating code instead depends on techniques such as PC-relative addressing and relocation support. Statement (ii) is also false because an extra ALU may improve performance by calculating an effective address in parallel, but it is not logically required—the existing ALU can perform the update in another step. Statement (iii) is true: a byte, word, or larger operand advances the address register by the corresponding item size. Hence only (iii) is true, option 3.

## Key Points

- Auto-increment uses an address register, accesses its operand, then advances the register by the operand size.

## Why the other options are incorrect

Options 1, 2, and 4 include (i) or (ii), both of which overstate what auto-increment addressing guarantees or requires. Auto-increment describes a register side effect, not a mandatory hardware datapath organization.

## References

- [Central Connecticut State University — Auto-increment addressing](https://www.cs.ccsu.edu/~kjell/cs254/ch04/ch4_71.html)
