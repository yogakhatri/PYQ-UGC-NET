# Question 59

*UGC NET CS · 2017 Jan Paper 3 · Knowledge Representation and Reasoning · Logical Consequence, Validity, and Consistency*

Which of the following statements is true ?

- **1.** The sentence S is a logical consequence of S1,…, Sn if and only if S1 ∧ S2 ∧........ ∧ Sn → S is satisfiable.
- **2.** The sentence S is a logical consequence of S1,…, Sn if and only if S1 ∧ S2 ∧........ ∧ Sn → S is valid.
- **3.** The sentence S is a logical consequence of S1,…,Sn iff S1∧S2∧…∧Sn∧¬S is consistent.
- **4.** The sentence S is a logical consequence of S1,…,Sn iff S1∧S2∧…∧Sn∧S is inconsistent.

> [!TIP]
> **Correct answer: 2. The sentence S is a logical consequence of S1,…, Sn if and only if S1 ∧ S2 ∧........ ∧ Sn → S is valid.**

## Solution

S is a logical consequence of premises S1,…,Sn exactly when every interpretation satisfying all premises also satisfies S. That condition says the implication (S1∧S2∧…∧Sn)→S is true under every interpretation—that is, valid. Hence option 2 is correct. Equivalently, S1∧…∧Sn∧¬S is unsatisfiable, but that equivalent statement is not offered correctly.

## Key Points

- Entailment Γ⊨S iff the implication (∧Γ)→S is valid iff Γ∧¬S is unsatisfiable.

## Why the other options are incorrect

Mere satisfiability of the implication in option 1 is too weak. Option 3 says the counterexample formula is consistent, the opposite of entailment. Option 4 conjoins S rather than ¬S; premises may consistently entail S, so that conjunction need not be inconsistent.
