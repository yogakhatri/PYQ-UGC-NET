# Question 111

*UGC NET CS · 2020 Nov With Answers · Mathematical Logic · Conditional and Biconditional Formalization*

A person who is radical (R) is electable (E) if he or she is conservative (C), but otherwise is not electable. Which proposed formalizations correctly express this statement? (A) (R ∧ E) ↔ C. (B) R → (E ↔ C). (C) R → ((C → E) ∨ ¬E). (D) (¬R ∨ ¬E ∨ C) ∧ (¬R ∨ ¬C ∨ E).

- **1.** (B) only
- **2.** (C) only
- **3.** (A) and (C) only
- **4.** (B) and (D) only

> [!TIP]
> **Correct answer: 4. (B) and (D) only**

## Solution

For a radical person, the sentence says electability occurs exactly when conservatism occurs: R→(E↔C), which is B. Expand the biconditional as (E→C)∧(C→E), replace each implication, and distribute R: (¬R∨¬E∨C)∧(¬R∨¬C∨E). This is precisely D. Hence B and D are equivalent formalizations, giving option 4.

## Key Points

- ‘If conservative, electable; otherwise not’ makes E and C equivalent within the radical case: R→(E↔C).

## Why the other options are incorrect

A, (R∧E)↔C, wrongly forces any conservative person to be both radical and electable. In C, (C→E)∨¬E simplifies to (¬C∨E∨¬E), a tautology, so the formula imposes no required relationship between E and C when R holds.
