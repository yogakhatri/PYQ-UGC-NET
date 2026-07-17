# Question 42

*UGC NET CS · 2013 June Paper 3 · Basic Computer Organization and Design · Zero-, One-, Two- and Three-Address Formats*

Computers can have instruction formats with

- **A.** only two address and three address instructions
- **B.** only one address and two address instructions
- **C.** only one address, two address and three address instructions
- **D.** zero address, one address, two address and three address instructions

> [!TIP]
> **Correct answer: D. zero address, one address, two address and three address instructions**

## Solution

Instruction formats are often classified by how many explicit operand addresses they contain. A stack machine uses zero-address instructions because operands are implicit on the stack; an accumulator machine often uses one address; many register machines use two addresses; and three-address instructions explicitly name two sources and one destination. Computer designs can therefore use all four formats.

## Key Points

- Address count ranges from zero for implicit stack operands to three for two explicit sources plus a destination.

## Why the other options are incorrect

A, B and C exclude at least one well-established format. In particular, any answer omitting zero-address stack instructions is incomplete, and three-address code is also a standard organization.
