# Question 110

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Regular Language Models · Grammars and Expressions*

Which of the following identities for regular expressions/languages are correct? A. ∅ + L = L + ∅ = L. B. εL = Lε = L. C. ∅L = L∅ = ∅. D. ∅*L = L∅* = L.

- **1.** A, B and D only
- **2.** A. B and C only
- **3.** B and D only
- **4.** A and D only

> [!TIP]
> **Correct answer: No listed option — A, B, C, and D are all correct**

## Solution

For any language L: ∅+L=L; εL=L; ∅L=∅; and ∅*={ε}, so ∅*L=L. Thus all four printed identities are correct, but no option lists A,B,C,D.

## Key Points

- Distinguish ∅ from ε: ∅ annihilates concatenation, whereas {ε} is its identity.

## Why the other options are incorrect

Every offered choice omits at least one valid identity.
