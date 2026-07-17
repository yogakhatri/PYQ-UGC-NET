# Question 57

*UGC NET CS · 2015 June Paper 3 · Mathematical Logic · Biconditional Equivalence*

In propositional logic, P ↔ Q is equivalent to which expression? Here ~ denotes NOT.

- **1.** ~(P ∨ Q) ∧ ~(Q ∨ P)
- **2.** (~P ∨ Q) ∧ (~Q ∨ P)
- **3.** (P ∨ Q) ∧ (Q ∨ P)
- **4.** ~(P ∨ Q) → ~(Q ∨ P)

> [!TIP]
> **Correct answer: 2. (~P ∨ Q) ∧ (~Q ∨ P)**

## Solution

A biconditional is true exactly when both implications hold: `P ↔ Q ≡ (P → Q) ∧ (Q → P)`. Replacing each implication with a disjunction gives `(~P ∨ Q) ∧ (~Q ∨ P)`, which is option 2.

## Key Points

- Biconditional = two directions of implication = `(¬P∨Q)∧(¬Q∨P)`.

## Why the other options are incorrect

Option 3 simplifies to `P∨Q` and accepts cases where only one proposition is true. Option 1 says neither is true in a redundant form and misses the both-true case. Option 4 is an implication between two identical expressions because `P∨Q = Q∨P`, so it is a tautology rather than a biconditional.
