# Question 43

*UGC NET CS · 2015 Dec Paper 2 · Parsing and Formal Languages · LL, LR, Regular Expressions and CFL Closure*

Which of the following statements is false ?

- **1.** Top-down parsers are LL parsers where first L stands for left - to - right scan and second L stands for a leftmost derivation.
- **2.** (000)* matches only strings containing an odd number of zeroes, including the empty string.
- **3.** Bottom-up parsers are in the LR family, where L stands for left - to - right scan and R stands for rightmost derivation.
- **4.** Context-free languages are closed under reversal: if L is context-free, then L^R={w^R : w∈L} is context-free.

> [!TIP]
> **Correct answer: 2. (000)* matches only strings containing an odd number of zeroes, including the empty string.**

## Solution

The expression `(000)*` concatenates zero or more blocks of exactly three zeros, so it generates ε, 000, 000000, and so on—lengths 0,3,6,9,… . Those are multiples of three, not exclusively odd counts; the empty string itself has zero zeros. Hence statement 2 is false.

## Key Points

- A starred fixed block `(000)*` produces lengths divisible by three.

## Why the other options are incorrect

LL parsing scans left to right and constructs a leftmost derivation. LR parsing scans left to right and corresponds to a rightmost derivation in reverse. Context-free languages are closed under reversal, obtainable by reversing productions appropriately. These statements are true in the intended textbook sense.
