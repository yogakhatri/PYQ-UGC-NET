# Question 69

*UGC NET CS · 2013 June Paper 3 · Knowledge Representation and Reasoning · Skolemization*

If we convert ∃u ∀v ∀x ∃y (P(f(u),v, x, y) → Q(u,v,y)) to ∀v ∀x (P(f(a),v, x, g(v,x)) → Q(a,v,g(v,x))) This process is known as

- **A.** Simplification
- **B.** Unification
- **C.** Skolemization
- **D.** Resolution

> [!TIP]
> **Correct answer: C. Skolemization**

## Solution

Skolemization removes existential quantifiers by replacing each existential variable with a new Skolem term based on the universal variables in whose scope it occurs. The outer ∃u has no preceding universal variables, so u becomes a new constant a. The later ∃y is inside ∀v∀x, so y becomes a new function g(v,x). The remaining formula is universally quantified, exactly as shown.

## Key Points

- Existential with no preceding universals→Skolem constant; with preceding universals→Skolem function of them.

## Why the other options are incorrect

Simplification is a general rewriting term and does not describe the systematic introduction of Skolem symbols. Unification finds substitutions that make terms equal. Resolution derives clauses by cancelling complementary literals. Neither performs these existential replacements.
