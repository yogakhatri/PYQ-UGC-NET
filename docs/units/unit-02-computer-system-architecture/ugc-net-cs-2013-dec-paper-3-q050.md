# Question 50

*UGC NET CS · 2013 Dec Paper 3 · Basic Computer Organization and Design · Instruction-Format Design Criteria*

Which of the following is a design criteria for instruction formats ?

- **A.** The size of instructions
- **B.** The number of bits in the address fields
- **C.** The sufficient space in the instruction format to express all the operations desired.
- **D.** All of these

> [!TIP]
> **Correct answer: D. All of these**

## Solution

An instruction format must balance several linked constraints. Its total size affects memory use and fetch bandwidth; the number of address bits determines the directly addressable register or memory space; and the opcode/function fields must provide enough distinct encodings for every required operation. Since A, B and C are all genuine design criteria, the inclusive answer is all of these.

## Key Points

- An instruction format divides a finite bit budget among opcode, operand/address and mode fields.

## Why the other options are incorrect

A, B and C each identify only one part of the design problem. Selecting any one alone ignores the trade-off among instruction length, operand-address capacity and opcode capacity.
