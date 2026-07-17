# Question 44

*UGC NET CS · 2015 Dec Paper 3 · Mathematical Logic · Modus Ponens*

In propositional logic, given P and P→Q, what can be inferred directly?

- **1.** ¬Q
- **2.** Q
- **3.** P ∧ Q
- **4.** ¬P∧Q

> [!TIP]
> **Correct answer: 2. Q**

## Solution

From P and P→Q, modus ponens immediately derives Q: if the antecedent is known true and the implication holds, its consequent must be true. Therefore option 2 is the direct inference.

## Key Points

- Modus ponens: P, P→Q ⟹ Q.

## Why the other options are incorrect

¬Q contradicts the implication with true P. P∧Q can be derived only after first obtaining Q and then applying conjunction introduction, so it is not the direct modus-ponens conclusion asked for. ¬P∧Q has no support.
