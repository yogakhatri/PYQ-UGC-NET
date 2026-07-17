# Question 3

*UGC NET CS · 2016 July Paper 2 · Sets and Relations · Representation and Properties of Relations*

Suppose that R1 and R2 are reflexive relations on a set A. Which of the following statements is correct ?

- **1.** R1 ∩ R2 is reflexive and R1 ∪ R2 is irreflexive.
- **2.** R1 ∩ R2 is irreflexive and R1 ∪ R2 is reflexive.
- **3.** Both R1 ∩ R2 and R1 ∪ R2 are reflexive.
- **4.** Both R1 ∩ R2 and R1 ∪ R2 are irreflexive.

> [!TIP]
> **Correct answer: 3. Both R1 ∩ R2 and R1 ∪ R2 are reflexive.**

## Solution

Reflexivity means every diagonal pair (a,a), for a∈A, belongs to the relation. Since both R₁ and R₂ contain every such pair, each diagonal pair belongs to their intersection and also to their union. Therefore both R₁∩R₂ and R₁∪R₂ are reflexive.

## Key Points

- Properties forced by membership of every diagonal pair survive both union and intersection.

## Why the other options are incorrect

A relation is irreflexive only when no diagonal pair occurs. Here all diagonal pairs are guaranteed in both original relations, so neither the intersection nor the union can be irreflexive. Options 1, 2, and 4 each make at least one such false claim.
