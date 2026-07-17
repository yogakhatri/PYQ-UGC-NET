# Question 69

*UGC NET CS · 2019 June Paper 1 And 2 · Digital Logic Circuits and Components · Memory Unit*

How many address lines and data lines are required to provide a memory capacity of 16K x 16?

- **1.** 10,4
- **2.** 16,16
- **3.** 14,16
- **4.** 4,16

> [!TIP]
> **Correct answer: 3. 14,16**

## Solution

A 16K×16 memory contains 16K addressable words, each 16 bits wide. Since 16K=16×1024=2^4×2^10=2^14, fourteen address lines are needed to select one word. Each selected word supplies sixteen bits, so sixteen data lines are required.

## Key Points

- For 2^a×w memory, a is the number of address lines and w is the number of data lines.

## Why the other options are incorrect

- **Option 1:** ten address lines select only 1K words, and four data lines give a four-bit word.
- **Option 2:** sixteen address lines would select 64K words.
- **Option 4:** four address lines select only sixteen words.
