# Question 40

*UGC NET CS · 2018 July Paper 2 · Unsolvable Problems and Computational Complexity · Turing-Machine Equivalence and Totality*

S1: No algorithm decides whether arbitrary Turing machines M1 and M2 accept the same language. S2: Determining whether a Turing machine halts on every input is undecidable. Which statements are correct?

- **1.** Both S1 and S2 are correct
- **2.** Both S1 and S2 are not correct
- **3.** Only S1 is correct
- **4.** Only S2 is correct

> [!TIP]
> **Correct answer: 1. Both S1 and S2 are correct**

## Solution

S1 is true: language equivalence for arbitrary Turing machines is undecidable; no algorithm can always determine whether L(M1)=L(M2). S2 is also true: the totality problem—whether a machine halts for every input—is undecidable (and the ordinary machine/input halting problem is undecidable as well). Therefore both statements are correct, option 1.

## Key Points

- Nontrivial semantic properties of Turing-machine languages and universal halting behavior are undecidable.

## Why the other options are incorrect

Options 2–4 claim at least one of these classic undecidable semantic properties is decidable. Rice's theorem supports S1, while reductions from the halting problem establish S2.
