# Question 8

*UGC NET CS · 2017 Nov Paper 2 · Mathematical Logic · Biconditional Equivalence*

Let P and Q be two propositions, ¬ (P ↔ Q) is equivalent to :

- **1.** P↔¬Q
- **2.** ¬P↔Q
- **3.** ¬P↔¬Q
- **4.** Q→P

> [!TIP]
> **Correct answer: No unique answer: both options 1 and 2 are logically equivalent to ¬(P↔Q).**

## Solution

P↔Q is true when P and Q have the same truth value, so its negation is true exactly when they differ—this is XOR. In P↔¬Q, the two sides are equal exactly when P and Q differ. The same is true of ¬P↔Q. Algebraically, ¬(P↔Q) ≡ P↔¬Q ≡ ¬P↔Q. Therefore both options 1 and 2 are correct, and the item has no unique valid choice.

## Key Points

- Negating a biconditional produces XOR; equivalently, negate either one—but not both—of its operands.

## Why the other options are incorrect

Option 3, ¬P↔¬Q, is equivalent to P↔Q, not its negation. Option 4, Q→P, is false only in one truth-table row and therefore is not XOR. Selecting only option 1, as an intended key might do, overlooks the symmetry of negating either side of a biconditional.
