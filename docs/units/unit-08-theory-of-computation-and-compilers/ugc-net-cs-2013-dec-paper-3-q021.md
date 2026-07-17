# Question 21

*UGC NET CS · 2013 Dec Paper 3 · Context-Free Grammars · Grammar Equivalence and Redundant Productions*

Given the following statements : S 1 : The grammars S → asb | bsa | ss | a and S → asb | bsa | a are not equivalent. S 2 : The grammars S → ss | sss | asb | bsa | λ and S → ss | asb | bsa | λ are equivalent. Which of the following is true ?

- **A.** S 1 is correct and S 2 is not correct.
- **B.** Both S 1 and S2 are correct.
- **C.** S 1 is not correct and S2 is correct.
- **D.** Both S 1 and S2 are not correct.

> [!TIP]
> **Correct answer: B. Both S 1 and S2 are correct.**

## Solution

S1 is true: adding S→SS to the first grammar permits concatenations, such as strings with multiple central a contributions, that the grammar without SS cannot generate. S2 is also true: S→SS already makes SSS derivable by expanding one of the two S symbols again, so explicitly adding S→SSS does not change the language.

## Key Points

- To compare grammars, test whether an added production generates new terminal strings or is derivable from existing recursive rules.

## Why the other options are incorrect

A and C incorrectly reject one true statement, while D rejects both. A production is redundant when its effect can already be obtained through repeated existing productions.
