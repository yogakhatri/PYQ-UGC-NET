# Question 136

*UGC NET CS · 2019 Dec Paper 1 And 2 · Instruction Set Architecture · Effective-Address Calculation*

An instruction is stored at location 500, with its address field at location 501. The address field contains 400, and processor register Ri contains 200. Match each addressing mode with its effective address. List I: A. Direct; B. Register indirect; C. Indexed with Ri; D. Relative. List II: I. 200; II. 902; III. 400; IV. 600.

- **1.** A-III, B-I, C-IV, D-II
- **2.** A-I, B-II, C-III, D-IV
- **3.** A-IV, B-II, C-III, D-I
- **4.** A-IV, B-III, C-II, D-I

> [!TIP]
> **Correct answer: 1. A-III, B-I, C-IV, D-II**

## Solution

For direct addressing, the address field itself is the effective address, so A=400=III. For register-indirect addressing, the effective address is the content of Ri, so B=200=I. Indexed addressing adds the address field and index register: 400+200=600, so C=IV. In relative addressing, the displacement is added to the program counter after the two-word instruction has been fetched. With words at 500 and 501, the next-instruction PC is 502; hence 502+400=902, so D=II. The mapping A-III, B-I, C-IV, D-II is option 1.

## Key Points

- Direct uses A, indirect uses (R), indexed uses A+(R), and PC-relative uses next-PC+A.

## Why the other options are incorrect

Options 2–4 confuse an operand's field, a register's contents, and sums involving them. The common relative-addressing trap is adding 400 to 500 or 501; the PC points to 502 after fetching the complete instruction.
