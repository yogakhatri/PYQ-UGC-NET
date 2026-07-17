# Question 75

*UGC NET CS · 2018 July Paper 2 · Knowledge Representation and Reasoning · Models of Propositional Sentences*

A vocabulary contains only four propositions A, B, C, and D. How many models satisfy the sentence B∨C?

- **1.** 10
- **2.** 12
- **3.** 15
- **4.** 16

> [!TIP]
> **Correct answer: 2. 12**

## Solution

Four propositions have 2⁴=16 total truth assignments. B∨C is false only when B=false and C=false. In that case A and D remain free, giving 2²=4 falsifying assignments. Therefore 16−4=12 assignments satisfy the sentence, so option 2 is correct.

## Key Points

- Count all assignments, then subtract assignments that falsify the formula; variables absent from the formula remain free.

## Why the other options are incorrect

Sixteen counts every model without enforcing B∨C. Fifteen would be correct only if a single assignment falsified the sentence, but A and D create four such assignments. Ten has no corresponding truth-table count.
