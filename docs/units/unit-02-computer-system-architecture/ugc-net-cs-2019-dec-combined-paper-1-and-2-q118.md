# Question 118

*UGC NET CS · 2019 Dec Paper 1 And 2 · Instruction Set Architecture · RISC Characteristics*

The Reduced Instruction Set Computer (RISC) characteristics are : (a) Single cycle instruction execution (b) Variable length instruction formats (c) Instructions that manipulates operands in memory (d) Efficient instruction pipeline Choose the correct characteristics from the options given below :

- **1.** (a) and (b)
- **2.** (b) and (c)
- **3.** (a) and (d)
- **4.** (c) and (d)

> [!TIP]
> **Correct answer: 3. (a) and (d)**

## Solution

RISC designs use a small set of simple, usually fixed-length instructions with register-to-register ALU operations and explicit load/store memory access. Their simple, regular execution supports the ideal of one instruction completing per cycle in a pipeline and enables efficient pipelining. Thus (a) and (d) are the RISC characteristics, option 3.

## Key Points

- RISC: simple fixed-format load/store instructions designed for fast, regular pipelining.

## Why the other options are incorrect

Variable-length formats in (b) are associated more with CISC and complicate decoding. Statement (c) suggests general operations directly on memory operands; RISC normally confines memory access to load and store instructions. Every other option includes (b) or (c).
