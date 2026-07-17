# Question 50

*UGC NET CS · 2014 Dec Paper 3 · File and Input/Output Systems · Linked-List Free-Space Accounting*

How many disk blocks are required to keep a linked list of free disk-block numbers for a 16 GiB disk with 1 KiB blocks, if each disk-block number occupies 32 bits?

- **A.** 1024 blocks
- **B.** 16794 blocks
- **C.** 20000 blocks
- **D.** 1048576 blocks

> [!TIP]
> **Correct answer: No listed option is correct. A standard linked-list grouping needs 65,794 blocks (65,536 even if no next-block slot were reserved).**

## Solution

The disk has (16×2³⁰)/(2¹⁰)=16×2²⁰=16,777,216 blocks. A 1 KiB list block has 8,192 bits, so it can hold 8,192/32=256 block numbers. In the usual linked-list grouping, one 32-bit slot points to the next list block, leaving 255 free-block numbers. Thus the required count is ⌈16,777,216/255⌉=65,794. Even the simplified calculation 16,777,216/256 gives 65,536, so none of 1,024, 16,794, 20,000, or 1,048,576 is correct.

## Key Points

- Convert disk capacity to a block count, divide block size by address size, reserve a link slot, and use a ceiling.

## Why the other options are incorrect

A and D are powers of two but do not follow from the number of disk blocks and addresses per list block. C is an unsupported round number. B appears plausibly to contain a printing error—16,794 instead of 65,794—but the printed value is still wrong and should not be selected as mathematically correct.
