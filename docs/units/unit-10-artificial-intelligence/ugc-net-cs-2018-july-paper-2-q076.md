# Question 76

*UGC NET CS · 2018 July Paper 2 · Knowledge Representation and Reasoning · Semantic Entailment*

Consider: (a) False ⊨ True. (b) If α ⊨ (β∧γ), then α ⊨ β and α ⊨ γ. Which choice is correct?

- **1.** Both statement (a) and statement (b) are false.
- **2.** Statement (a) is true but statement (b) is false.
- **3.** Statement (a) is false but statement (b) is true.
- **4.** Both statement (a) and statement (b) are true.

> [!TIP]
> **Correct answer: 4. Both statement (a) and statement (b) are true.**

## Solution

Statement (a) is true by the definition of semantic entailment: α⊨β means every model of α is a model of β. `False` has no models, so there is no countermodel; it vacuously entails `True` (indeed, it entails every formula). Statement (b) is also true: if every model of α satisfies β∧γ, then each such model satisfies β and also γ. Therefore both statements are true, option 4.

## Key Points

- Entailment is universal over premise-models; an unsatisfiable premise entails everything, and a conjunction entails each conjunct.

## Why the other options are incorrect

Options 1–3 reject at least one valid entailment principle. Do not confuse semantic entailment with a material implication evaluated under one assignment; entailment quantifies over every model of the premise.
