# Question 148

*UGC NET CS · 2018 Dec Paper 1 And 2 · Knowledge Representation · Model Counting in Propositional Logic*

With only four propositions A, B, C and D, how many models satisfy the sentence NOT A OR NOT B OR NOT C OR NOT D?

- **1.** 7
- **2.** 8
- **3.** 15
- **4.** 16

> [!TIP]
> **Correct answer: 3. 15**

## Solution

Four independent propositions have 2^4=16 truth assignments. The disjunction ¬A∨¬B∨¬C∨¬D is false only when every disjunct is false, which requires A=B=C=D=true. Exactly one assignment is therefore excluded, leaving 16−1=15 satisfying models. Hence option 3.

## Key Points

- For a disjunction, count its complement: all literals must be false simultaneously for the disjunction to fail.

## Why the other options are incorrect

Seven and eight would correspond to different constraints that eliminate roughly half the assignments. Sixteen would mean the formula is a tautology, but the all-true assignment falsifies every negated literal. Only 15 accounts for that single countermodel.
