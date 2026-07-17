# Question 6

*UGC NET CS · 2016 July Paper 2 · Boolean Algebra · Exclusive-OR Parity*

Which of the following logic expressions is incorrect ?

- **1.** 1⊕0=1
- **2.** 1⊕1⊕1=1
- **3.** 1⊕1⊕0=1
- **4.** 1⊕1=0

> [!TIP]
> **Correct answer: 3. 1⊕1⊕0=1**

## Solution

Exclusive OR is addition modulo 2: its result is 1 exactly when an odd number of input bits are 1. In 1⊕1⊕0 there are two ones, so the result is 0, not 1. Therefore expression 3 is incorrect.

## Key Points

- Multi-input XOR is a parity function: odd ones → 1, even ones → 0.

## Why the other options are incorrect

1⊕0=1 and 1⊕1=0 follow directly from the XOR truth table. Associativity gives 1⊕1⊕1=(1⊕1)⊕1=0⊕1=1, so option 2 is also correct.
