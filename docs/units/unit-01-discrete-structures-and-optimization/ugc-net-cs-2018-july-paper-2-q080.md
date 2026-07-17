# Question 80

*UGC NET CS · 2018 July Paper 2 · Counting, Mathematical Induction and Discrete Probability · Five-Card Poker Combinations*

How many atomic events are in the sample space of all five-card poker hands dealt from a standard 52-card deck?

- **1.** 2, 598, 960
- **2.** 3, 468, 960
- **3.** 3, 958, 590
- **4.** 2, 645, 590

> [!TIP]
> **Correct answer: 1. 2, 598, 960**

## Solution

A five-card poker hand is an unordered selection of 5 distinct cards from 52. Thus the number of atomic outcomes is C(52,5)=52!/(5!47!)=(52×51×50×49×48)/(5×4×3×2×1)=2,598,960. Therefore option 1 is correct.

## Key Points

- Poker hands are combinations because card order within a hand does not matter.

## Why the other options are incorrect

The other numbers do not equal the required combination. Using a permutation would incorrectly treat different deal orders of the same five cards as distinct hands; each unordered hand would then be counted 5! times.
