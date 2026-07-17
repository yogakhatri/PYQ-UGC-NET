# Question 53

*UGC NET CS · 2020 Nov With Answers · Mathematical Logic · Propositional Equivalence*

Which of the following pairs of propositions are not logically equivalent?

- **1.** (p→r)∧(q→r) and (p∨q)→r
- **2.** p↔q and ¬p↔¬q
- **3.** (p∧q)∨(¬p∧¬q) and p↔q
- **4.** (p∧q)→r and (p→r)∧(q→r)

> [!TIP]
> **Correct answer: 4. (p∧q)→r and (p→r)∧(q→r)**

## Solution

Pairs 1–3 are equivalences. For pair 1, both expressions simplify to (¬p∨r)∧(¬q∨r). Pair 2 follows because negating both sides preserves a biconditional. Pair 3 is the standard expansion of p↔q: both true or both false. Pair 4 is not equivalent. Let p=true, q=false, r=false. Then (p∧q)→r is true because its antecedent is false, but (p→r)∧(q→r) is false∧true=false. A single counterexample disproves equivalence, so option 4.

## Key Points

- To disprove logical equivalence, find one valuation with different truth values; p=T,q=F,r=F separates pair 4.

## Why the other options are incorrect

Options 1–3 can each be transformed into the same formula on both sides using implication and biconditional laws. The invalid distribution in option 4 confuses implication from a conjunction with a conjunction of two implications.
