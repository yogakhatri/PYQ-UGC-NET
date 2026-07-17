# Question 61

*UGC NET CS · 2014 Dec Paper 3 · Context-Free Language · Language-Family Inclusion Hierarchy*

Which inclusion chain correctly relates deterministic context-free (L_DCF), context-free (L_CF), context-sensitive (L_CS), recursive (L_REC), and recursively enumerable (L_RE) languages?

- **A.** L CF ⊆ L DCF ⊆ L CS ⊆ L RE ⊆ L REC
- **B.** L CF ⊆ L DCF ⊆ L CS ⊆ L REC ⊆ L RE
- **C.** L DCF ⊆ L CF ⊆ L CS ⊆ L RE ⊆ L REC
- **D.** L DCF ⊆ L CF ⊆ L CS ⊆ L REC ⊆ L RE

> [!TIP]
> **Correct answer: D. L DCF ⊆ L CF ⊆ L CS ⊆ L REC ⊆ L RE**

## Solution

A deterministic pushdown automaton is a restricted PDA, so L_DCF⊆L_CF. Every context-free language is context-sensitive, L_CF⊆L_CS. Context-sensitive languages are decidable and hence recursive, L_CS⊆L_REC. Every decider is also a recognizer, so recursive languages are contained in recursively enumerable languages, L_REC⊆L_RE. The chain is therefore L_DCF⊆L_CF⊆L_CS⊆L_REC⊆L_RE.

## Key Points

- Increasing power: deterministic PDA < PDA < linear-bounded automaton < decider Turing machine < recognizer Turing machine.

## Why the other options are incorrect

A and B incorrectly place all CFLs inside DCFLs; determinism makes DCFL the smaller family. A and C also reverse recursive and recursively enumerable languages. Only D has both endpoints and the middle hierarchy in the right order.
