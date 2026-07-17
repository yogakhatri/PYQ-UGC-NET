# Question 11

*UGC NET CS · 2014 Dec Paper 3 · Distributed Databases · Mixed and Vertical Fragment Reconstruction*

Consider the following statements : I. Re-construction operation used in mixed fragmentation satisfies commuta tive rule. II. Re-construction operation used in vertical fragmentation satisfies c ommutative rule Which of the following is correct ?

- **A.** I
- **B.** II
- **C.** Both are correct
- **D.** None of the statements are correct.

> [!TIP]
> **Correct answer: C. Both are correct**

## Solution

Vertical fragments are reconstructed by joining them on the replicated key, and natural/equijoin is commutative with respect to operand order, so II holds. Mixed fragmentation is reconstructed through an appropriate combination of joins for vertical pieces and unions for horizontal pieces. Within a valid fragmentation layout, the corresponding same-kind fragment combinations may be reordered because join and union are commutative, so I is also true in the intended reconstruction-rule sense.

## Key Points

- Vertical reconstruction uses join; mixed reconstruction combines join and union, whose compatible operands can be reordered.

## Why the other options are incorrect

A and B each omit one valid reconstruction property. D rejects both even though the standard reconstruction operators are order-independent within their compatible fragment groups.
