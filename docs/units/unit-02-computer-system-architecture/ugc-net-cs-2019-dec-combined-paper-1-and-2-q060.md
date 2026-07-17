# Question 60

*UGC NET CS · 2019 Dec Paper 1 And 2 · Basic Computer Organization and Design · Stored-Program Organization and Instruction Codes*

A computer uses a memory unit of 512 K words of 32 bits each. A binary instruction code is stored in one word of the memory. The instruction has four parts: an addressing mode field to specify one of the two-addresssing mode (direct and indirect), an operation code. a register code part to specify one of the 256 registers and an address part. How many bits are there in addressing mode part. opcode part. register code part and the address part?

- **1.** 1, 3, 9, 19
- **2.** 1, 4, 9, 18
- **3.** 1, 4, 8, 19
- **4.** 1, 3, 8, 20

> [!TIP]
> **Correct answer: 3. 1, 4, 8, 19**

## Solution

Two addressing modes require log2(2)=1 bit. A 512 K-word memory has 512×1024=2^19 word locations, so the address field needs 19 bits. Selecting one of 256=2^8 registers needs 8 bits. The remaining opcode width is 32−1−19−8=4 bits. In the requested order the fields are 1,4,8,19, which is option 3.

## Key Points

- A field selecting N power-of-two alternatives needs log2 N bits; subtract all fixed fields from the instruction width to get the opcode.

## Why the other options are incorrect

Options 1 and 2 allocate 9 bits to a 256-register selector, wasting a bit. Option 4 allocates 20 address bits, which would address 1 M words rather than 512 K, and consequently leaves only 3 opcode bits.
