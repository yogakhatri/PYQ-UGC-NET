# Question 22

*UGC NET CS · 2015 June Paper 3 · Knowledge Representation and Logic · Clause and Implication Equivalence*

The clausal form of the disjunctive normal form ¬ A ∨ ¬ B ∨ ¬ C ∨ D is :

- **1.** A ∧ B ∧ C ⇒ D
- **2.** A ∨ B ∨ C ∨ D ⇒ true
- **3.** A ∧ B ∧ C ∧ D ⇒ true
- **4.** A ∧ B ∧ C ∧ D ⇒ false

> [!TIP]
> **Correct answer: 1. A ∧ B ∧ C ⇒ D**

## Solution

Use `P ⇒ Q ≡ ¬P ∨ Q`. With `P = A ∧ B ∧ C` and `Q = D`, we get `(A ∧ B ∧ C) ⇒ D ≡ ¬A ∨ ¬B ∨ ¬C ∨ D`. Therefore the given clause is exactly the implication in option 1.

## Key Points

- Move antecedent literals into a clause by negating them: `A∧B∧C ⇒ D` becomes `¬A∨¬B∨¬C∨D`.

## Why the other options are incorrect

Any proposition implying `true` is a tautology, so options 2 and 3 cannot represent the supplied non-tautological clause. Option 4 is `¬(A∧B∧C∧D)`, which contains `¬D`, whereas the original contains positive `D`.
