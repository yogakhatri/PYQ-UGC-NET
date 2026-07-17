# Question 9

*UGC NET CS · 2015 Dec Paper 2 · Mathematical Logic · Tautologies and Logical Equivalence*

Which of the following compound propositions are tautologies? (a) p ∨ ¬(p ∧ q), (b) (p ∧ ¬q) ∨ ¬(p ∧ q), and (c) p ∧ (q ∨ r).

- **1.** (a) and (c)
- **2.** (b) and (c)
- **3.** (a) and (b)
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: No listed option — only proposition (a) is a tautology**

## Solution

For (a), p∨¬(p∧q)=p∨¬p∨¬q=True by De Morgan's law, so it is a tautology. Proposition (b) is false when p=True and q=True: both p∧¬q and ¬(p∧q) are then false. Proposition (c) is false whenever p=False. Hence only (a) is a tautology, but the paper supplies no ‘(a) only’ choice.

## Key Points

- Simplify with logical identities, then use a single counterexample valuation to reject a tautology claim.

## Why the other options are incorrect

Every offered choice includes (b), (c), or both. One false truth assignment is sufficient to show that a formula is not a tautology.
