# Question 26

*UGC NET CS · 2013 Dec Paper 2 · Syntax Analysis · SLR, LALR and Canonical LR Power*

Given the following statements : S 1 : SLR uses follow information to guide reductions. In case of LR and LALR parsers, the look- aheads are associated with the items and they make use of the left context available to the parser. S 2 : LR grammar is a larger sub- class of context free grammar as compared to that SLR and LALR grammars. Which of the following is true ?

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S 2 is correct.
- **C.** S 1 is correct and S 2 is not correct.
- **D.** S 1 is correct and S2 is correct.

> [!TIP]
> **Correct answer: D. S 1 is correct and S2 is correct.**

## Solution

S1 is correct: SLR places a reduction using the FOLLOW set of the production's left-hand nonterminal, while LR(1) items carry explicit lookahead symbols and LALR retains merged LR(1) lookahead information. S2 is also correct: canonical LR(1) recognizes a strictly larger grammar class than LALR(1), which in turn contains SLR(1).

## Key Points

- Parser power hierarchy: SLR(1) is contained in LALR(1), which is contained in canonical LR(1).

## Why the other options are incorrect

Options A-C declare at least one true statement false. The practical trade-off is that canonical LR tables are more powerful but larger; LALR merges states for compact tables, and SLR uses coarser FOLLOW information.
