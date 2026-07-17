# Question 43

*UGC NET CS · 2013 June Paper 3 · Instruction Set Architecture · Program-Control versus Data-Manipulation Instructions*

Which is not a typical program control instruction ?

- **A.** BR
- **B.** JMP
- **C.** SHL
- **D.** TST

> [!TIP]
> **Correct answer: C. SHL**

## Solution

BR (branch) and JMP (jump) directly change the program counter. TST examines a value and sets condition flags used to control a following conditional transfer, so it is commonly grouped with control-support instructions in this classification. SHL shifts operand bits left and is a logical/data-manipulation operation; it does not itself direct instruction sequencing. Therefore SHL is the non-control instruction.

## Key Points

- Control instructions alter or decide sequencing; SHL primarily transforms an operand's bit pattern.

## Why the other options are incorrect

BR and JMP are canonical transfer-of-control instructions. TST supports conditional control by establishing status flags. SHL instead transforms data, even though its flags may later be tested by a separate branch.
