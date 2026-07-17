# Question 57

*UGC NET CS · 2014 Dec Paper 3 · Knowledge Representation · Propositional Resolution*

The resolvent of the set of clauses (A ∨ B, ~A ∨ D, C ∨ ~B) is

- **A.** A ∨ B
- **B.** C ∨ D
- **C.** A ∨ C
- **D.** A ∨ D

> [!TIP]
> **Correct answer: B. C ∨ D**

## Solution

Resolve (A∨B) with (¬A∨D) on A to obtain B∨D. Then resolve B∨D with (C∨¬B) on B to obtain C∨D. This is the final clause obtained by resolving through the entire three-clause set, so the intended answer is B.

## Key Points

- Resolution deletes one complementary literal pair and unions the remaining literals; repeat to combine the full set when a final resolvent is requested.

## Why the other options are incorrect

A is merely one original clause. D does not follow by eliminating complementary literals. C, A∨C, is a valid one-step resolvent of (A∨B) and (C∨¬B), so the phrase 'the resolvent of the set' is imprecise; the exam clearly intends the chained result using all three clauses, C∨D.
