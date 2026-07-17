# Question 6

*UGC NET CS · 2017 Jan Paper 2 · Mathematical Logic · Constructive Dilemma*

In propositional logic, (P→Q)∧(R→S) and P∨R are two premises. Which proposition Y follows from them?

- **1.** P∨R
- **2.** P∨S
- **3.** Q∨R
- **4.** Q∨S

> [!TIP]
> **Correct answer: 4. Q∨S**

## Solution

Use proof by cases on P∨R. If P is true, P→Q gives Q, hence Q∨S. If R is true, R→S gives S, hence Q∨S. Since at least one of P and R holds, Q∨S follows in every case. This inference is the constructive dilemma, so option 4 is correct.

## Key Points

- Constructive dilemma: (P→Q)∧(R→S), P∨R ⊢ Q∨S.

## Why the other options are incorrect

P∨R is merely the second premise, not the new conclusion. P∨S and Q∨R mix an antecedent from one branch with a consequent from the other and do not follow: the premise permits P true with R false, or conversely.
