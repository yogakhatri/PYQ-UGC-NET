# Question 56

*UGC NET CS · 2019 June Paper 1 And 2 · Mathematical Logic · Normal Forms*

Find the principal conjunctive normal form of [(p ∨ q) ∧ ¬p] → ¬q.

- **1.** p OR NOT q
- **2.** p OR q
- **3.** NOT p OR q
- **4.** NOT p OR NOT q

> [!TIP]
> **Correct answer: 1. p OR NOT q**

## Solution

Under ¬p, the conjunction p∨q can be true only through q, so the antecedent (p∨q)∧¬p simplifies to ¬p∧q. Replace implication A→B by ¬A∨B: ¬(¬p∧q)∨¬q. De Morgan's law gives (p∨¬q)∨¬q, which reduces to p∨¬q. This single maxterm is already in conjunctive normal form.

## Key Points

- Eliminate implication first, apply De Morgan's law, and then remove repeated literals.

## Why the other options are incorrect

- **Option 2:** p∨q has q with the wrong polarity.
- **Option 3:** ¬p∨q corresponds to p→q, not the given formula.
- **Option 4:** ¬p∨¬q also has p with the wrong polarity.
