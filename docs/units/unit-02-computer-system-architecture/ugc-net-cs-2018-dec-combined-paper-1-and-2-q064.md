# Question 64

*UGC NET CS · 2018 Dec Paper 1 And 2 · Basic Computer Organization and Design · Instruction-Format Bit Allocation*

A computer uses a memory unit with 256 K words of 32 bits each. A binary instruction code is stored in one word of memory. The instruction has four parts: an indirect bit, an operation code and a register code part to specify one of 64 registers and an address part. How many bits are there in the operation code, the register code part and the address part ?

- **1.** 7, 6, 18
- **2.** 6, 7, 18
- **3.** 7, 7,18
- **4.** 18, 7, 7

> [!TIP]
> **Correct answer: 1. 7, 6, 18**

## Solution

A memory of 256K words has 256×1024=2¹⁸ word locations, so the address field needs 18 bits. Selecting one of 64=2⁶ registers needs 6 bits. The 32-bit instruction also contains one indirect bit, leaving 32−18−6−1=7 bits for the opcode. Therefore the fields are 7, 6, and 18 bits, option 1.

## Key Points

- A field selecting N possibilities needs log₂N bits; subtract all fixed fields from the instruction length to obtain the opcode width.

## Why the other options are incorrect

The other triples either swap the register and opcode widths or exceed/misallocate the 32-bit word. K in memory capacity means 2¹⁰ here, and because the memory is specified in words, the 18-bit field addresses words directly.
