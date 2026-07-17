# Question 30

*UGC NET CS · 2015 June Paper 2 · IP Addressing · Classless Addressing and Block Alignment*

Which of the following is/are restriction(s) in classless addressing ?

- **1.** The number of addresses needs to be a power of 2.
- **2.** The mask needs to be included in the address to define the block.
- **3.** The starting address must be divisible by the number of addresses in the block.
- **4.** All of the above

> [!TIP]
> **Correct answer: 4. All of the above**

## Solution

In classless IPv4 addressing, a prefix length `/p` leaves `32 - p` host bits, so a block contains `2^(32-p)` addresses—a power of two. The prefix length or equivalent mask is required to identify the block size. A valid block begins on its own size boundary, meaning the numeric starting address is divisible by the number of addresses in the block. All three restrictions are therefore true.

## Key Points

- A CIDR block has power-of-two size, carries its prefix/mask, and starts at an address aligned to that size.

## Why the other options are incorrect

Options 1–3 each state one necessary CIDR property but omit the other two. Since every listed statement is correct, the complete choice is `All of the above`.
