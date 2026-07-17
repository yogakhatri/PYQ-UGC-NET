# Question 60

*UGC NET CS · 2017 Jan Paper 3 · Knowledge Representation and Reasoning · Resolution and Redundant Clauses*

Which formula is equivalent to (R∨Q)∧(P∨¬Q)?

- **1.** (R∨¬Q)∧(P∨¬Q)∧(R∨P)
- **2.** (R∨Q)∧(P∨¬Q)∧(R∨P)
- **3.** (R∨Q)∧(P∨¬Q)∧(R∨¬P)
- **4.** (R∨Q)∧(P∨¬Q)∧(¬R∨P)

> [!TIP]
> **Correct answer: 2. (R∨Q)∧(P∨¬Q)∧(R∨P)**

## Solution

The clauses R∨Q and P∨¬Q contain complementary literals Q and ¬Q. Resolving them produces the resolvent R∨P. Every assignment satisfying both original clauses must satisfy this resolvent, so adding it as a conjunct removes no models: (R∨Q)∧(P∨¬Q) is equivalent to (R∨Q)∧(P∨¬Q)∧(R∨P). This is option 2.

## Key Points

- Resolution rule: from A∨x and B∨¬x infer A∨B; adding an entailed resolvent preserves equivalence.

## Why the other options are incorrect

Option 1 changes Q to ¬Q in the first original clause. Options 3 and 4 add R∨¬P or ¬R∨P, neither of which follows from resolving the two given clauses and each can eliminate models of the original formula.
