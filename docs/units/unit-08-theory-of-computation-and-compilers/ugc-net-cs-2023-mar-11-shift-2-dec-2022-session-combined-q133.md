# Question 133

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Context-Free Language · Chomsky and Greibach Normal Forms*

What is the safest order while simplifying Context Free Grammar?

- **1.** Elimination of s-productions, Unit productions and then Useless symbols & productions.
- **2.** Elimination of useless symbols & productions, e-productions and then Unit productions.
- **3.** Elimination of Unit productions, -productions and then Useless symbols and productions.
- **4.** Elimination of &-productions, Useless symbols and productions and then Unit productions.

> [!TIP]
> **Correct answer: 1. Elimination of s-productions, Unit productions and then Useless symbols & productions.**

## Solution

Eliminate ε-productions first because doing so may create unit productions. Then eliminate unit productions because their removal may expose useless symbols. Removing useless symbols last avoids reintroducing them. Thus ε → unit → useless is the safest order.

## Key Points

- Order grammar transformations so later steps clean artifacts introduced by earlier ones.

## Why the other options are incorrect

Other orders can require repeating an earlier cleanup after a later transformation creates new unit or useless productions.
