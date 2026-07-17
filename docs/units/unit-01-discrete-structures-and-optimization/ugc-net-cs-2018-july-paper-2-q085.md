# Question 85

*UGC NET CS · 2018 July Paper 2 · Mathematical Logic · Negation of Quantifiers*

Which formula is equivalent to ¬∃x Q(x)?

- **1.** ∃x ¬Q(x)
- **2.** ∀x ¬Q(x)
- **3.** ¬∃x ¬Q(x)
- **4.** ∀x Q(x)

> [!TIP]
> **Correct answer: 2. ∀x ¬Q(x)**

## Solution

Negating an existential statement changes the quantifier to universal and negates its predicate: ¬∃x Q(x)≡∀x ¬Q(x). In words, `there is no x for which Q holds` means `for every x, Q does not hold`. Hence option 2 is correct.

## Key Points

- Quantifier De Morgan laws: ¬∃x P≡∀x¬P and ¬∀x P≡∃x¬P.

## Why the other options are incorrect

∃x¬Q(x) merely says at least one object lacks Q. ¬∃x¬Q(x) is equivalent to ∀xQ(x), the opposite claim. Option 4 also states ∀xQ(x).
