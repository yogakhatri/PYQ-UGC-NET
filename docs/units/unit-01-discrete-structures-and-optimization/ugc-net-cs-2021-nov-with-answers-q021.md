# Question 21

*UGC NET CS · 2021 Nov With Answers · Mathematical Logic · Propositional Equivalence by Implication Elimination*

Which of the following pairs are logically equivalent? A. not p -> (q -> r) and q -> (p or r). B. (p -> q) -> r and p -> (q -> r). C. (p -> q) -> (r -> s) and (p -> r) -> (q -> s).

- **1.** A only
- **2.** A and B only
- **3.** B and C only
- **4.** A and C only

> [!TIP]
> **Correct answer: 1. A only**

## Solution

Eliminate implications in pair A: ¬p→(q→r) becomes p∨¬q∨r, and q→(p∨r) also becomes ¬q∨p∨r, so A is equivalent. Pair B becomes (p∧¬q)∨r versus ¬p∨¬q∨r, which are not identical. Pair C becomes (p∧¬q)∨¬r∨s versus (p∧¬r)∨¬q∨s, also not identical. Therefore A only, option 1.

## Key Points

- Replace P→Q by ¬P∨Q, simplify, and use one counterexample when two forms differ.

## Why the other options are incorrect

For B, p=false, q=true, r=false makes the first formula false and the second true. For C, p=false, q=true, r=false, s=false makes the first true and the second false. These counterexamples eliminate every option containing B or C.
