# Question 109

*UGC NET CS · 2019 Dec Paper 1 And 2 · Mathematical Logic · Predicates and Quantifiers*

Consider: S1: (∀x P(x)) ∨ (∀x Q(x)) and ∀x(P(x) ∨ Q(x)) are not logically equivalent. S2: (∃x P(x)) ∧ (∃x Q(x)) and ∃x(P(x) ∧ Q(x)) are not logically equivalent. Which statement(s) are correct?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 3. Both S1 and S2**

## Solution

S1 is true: (∀xP(x))∨(∀xQ(x)) implies ∀x(P(x)∨Q(x)), but the converse fails. With two objects, let P hold only for the first and Q only for the second; every object satisfies P∨Q, yet neither predicate is universally true. S2 is also true: ∃x(P∧Q) implies (∃xP)∧(∃xQ), but the converse can use different witnesses—one object satisfying only P and another only Q. Thus both pairs are not equivalent, giving option 3.

## Key Points

- Test a claimed quantified equivalence with a two-element domain and let different elements witness different predicates.

## Why the other options are incorrect

Options 1 and 2 miss one valid countermodel, and option 4 incorrectly assumes quantifiers distribute over both connectives. Universal quantification distributes over conjunction, and existential quantification over disjunction; the displayed mixed cases do not distribute as equivalences.
