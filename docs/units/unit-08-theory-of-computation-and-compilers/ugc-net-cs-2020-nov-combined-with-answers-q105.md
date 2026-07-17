# Question 105

*UGC NET CS · 2020 Nov With Answers · Unsolvable Problems · CFL Equivalence, Inclusion and Universality*

Let G₁ and G₂ be arbitrary context-free grammars and R an arbitrary regular language. Consider: (A) Is L(G₁)=L(G₂)? (B) Is L(G₂)⊆L(G₁)? (C) Is L(G₁)=R? Which problems are undecidable?

- **1.** (A) only
- **2.** (B) only
- **3.** (A) and (B) only
- **4.** (A), (B) and (C)

> [!TIP]
> **Correct answer: 4. (A), (B) and (C)**

## Solution

Equivalence of two arbitrary context-free grammars (A) is undecidable, and so is inclusion L(G₂)⊆L(G₁) (B). For C, equality between an arbitrary CFL and a supplied regular language is also undecidable: choose the regular language R=Σ*. Then asking whether L(G₁)=R is exactly the universality problem for context-free grammars, which is undecidable. Consequently A, B, and C are all undecidable, option 4.

## Key Points

- Reduce C to CFG universality by choosing R=Σ*; equality and inclusion between arbitrary CFLs are also undecidable.

## Why the other options are incorrect

Options 1–3 omit at least one undecidable problem. The fact that membership and emptiness for CFLs are decidable does not extend to equality, inclusion, or universality; regularity of one comparison language does not rescue C because Σ* is already regular.
