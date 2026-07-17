# Question 51

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Mathematical Logic · Negation of quantified statements*

The negation of "Some students like hockey" is:

- **1.** Some students dislike hockey
- **2.** Every student dislike hockey
- **3.** Every student like hockey
- **4.** All students like hockey

> [!TIP]
> **Correct answer: 2. Every student dislike hockey**

## Solution

Write the statement with quantifiers: ‘Some students like hockey’ means ∃x(Student(x) ∧ LikesHockey(x)). Negating an existential quantifier changes it to a universal quantifier and negates its predicate: ¬∃x P(x) ≡ ∀x ¬P(x). Therefore every student does not like hockey, expressed in the options as ‘Every student dislike hockey.’

## Key Points

- Negation rules: ¬∃x P(x) ≡ ∀x ¬P(x), and ¬∀x P(x) ≡ ∃x ¬P(x).

## Why the other options are incorrect

Option 1 still asserts that at least one such student exists, so it can be true at the same time as the original statement. Options 3 and 4 assert that all students like hockey, which is much stronger than the original statement rather than its negation.
