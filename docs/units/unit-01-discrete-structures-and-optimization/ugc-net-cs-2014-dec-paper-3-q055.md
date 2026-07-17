# Question 55

*UGC NET CS · 2014 Dec Paper 3 · Mathematical Logic · Negating Quantifiers*

Which expression is logically equivalent to the well-formed formula ¬(∀x)F(x)?

- **A.** ∀x ¬F(x)
- **B.** ¬(∃x)F(x)
- **C.** ∃x ¬F(x)
- **D.** ∀x F(x)

> [!TIP]
> **Correct answer: C. ∃x ¬F(x)**

## Solution

Negating a universal statement means that at least one counterexample exists. Formally, ¬∀x F(x) ≡ ∃x ¬F(x). So the quantifier changes from universal to existential and the negation moves inside to the predicate.

## Key Points

- Push negation across a quantifier by swapping ∀ and ∃ and negating the predicate.

## Why the other options are incorrect

A says every x fails F, which is stronger than saying not every x satisfies F. B is equivalent to ∀x¬F(x), again too strong. D simply removes the negation. C alone applies the quantifier-negation law correctly.
