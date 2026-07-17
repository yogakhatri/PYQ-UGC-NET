# Question 49

*UGC NET CS · 2012 Dec Paper 2 · Boolean Algebra · Commutativity and Associativity*

Identify the operation that is commutative but not associative:

- **1.** OR
- **2.** NOR
- **3.** EX-OR
- **4.** NAND

> [!TIP]
> **Correct answer: Both NOR (option 2) and NAND (option 4) are commutative but not associative**

## Solution

NAND and NOR are symmetric in their two operands, so x NAND y = y NAND x and x NOR y = y NOR x: both are commutative. Neither is associative. For x=0, y=0, z=1, (x NAND y) NAND z = 0 but x NAND (y NAND z) = 1. With the same values, (x NOR y) NOR z = 0 but x NOR (y NOR z) = 1. Thus both options 2 and 4 satisfy the wording.

## Key Points

- Do not infer associativity from commutativity.
- OR and XOR have both properties; NAND and NOR are commutative but fail associativity.

## Why the other options are incorrect

OR and XOR are both commutative and associative, so options 1 and 3 do not fit. The item is defective because it asks for one operation but separately lists two correct operations, NOR and NAND.
