# Question 99

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Grammars · Chomsky Normal Form Production Count*

Let G = (V, T, S, P) be a context-free grammar without λ-productions or unit productions. Let K be the maximum number of symbols on the right-hand side of a production in P. What is the maximum number of production rules needed for an equivalent grammar in Chomsky normal form?

- **1.** (K − 1)|P| + |T| − 1
- **2.** (K − 1)|P| + |T|
- **3.** K|P| + |T| − 1
- **4.** K|P| + |T|

> [!TIP]
> **Correct answer: 2. (K − 1)|P| + |T|**

## Solution

A production with r symbols on its right side is binarized into r−1 CNF productions, so each original rule contributes at most K−1 rules and all original rules contribute at most (K−1)|P|. Terminals occurring in longer right sides are replaced by variables such as X_a, with one added rule X_a→a for each distinct terminal; at most |T| such rules are needed. The maximum is therefore (K−1)|P|+|T|, option 2.

## Key Points

- CNF conversion cost = binary-chain rules for long productions plus at most one terminal-isolation rule per terminal.

## Why the other options are incorrect

The −1 variants have no general justification: for G with the sole rule S→ab, K=2, |P|=1, and |T|=2, CNF needs S→AB, A→a, and B→b—three rules, attaining (K−1)|P|+|T|. The K|P| variants overcount binarization because an r-symbol right side needs r−1, not r, binary productions.
