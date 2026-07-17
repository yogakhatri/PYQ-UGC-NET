# Question 35

*UGC NET CS · 2016 July Paper 2 · Parsing Techniques · SLR, LALR, LL(1) and YACC*

Which of the following is FALSE ?

- **1.** The grammar S → a Sb |bSa|SS| ∈, where S is the only non-terminal symbol and ∈ is the null string, is ambiguous.
- **2.** SLR is powerful than LALR.
- **3.** An LL(1) parser is a top-down parser.
- **4.** YACC tool is an LALR (1) parser generator.

> [!TIP]
> **Correct answer: 2. SLR is powerful than LALR.**

## Solution

Statement 2 is false: LALR(1) is more powerful than SLR(1), not the reverse. LALR uses LR(1)-style lookahead information after merging compatible states, so some grammars that produce conflicts in an SLR table can be parsed by LALR. The remaining statements are true.

## Key Points

- Parser power follows SLR(1) ⊂ LALR(1) ⊂ LR(1), while LL(1) is predictive top-down parsing.

## Why the other options are incorrect

Statement 1 is true because the grammar is ambiguous; even ε has distinct derivations such as S⇒ε and S⇒SS⇒εε. Statement 3 is true because LL(1) parsing constructs a leftmost derivation top-down. Statement 4 is true: traditional YACC generates an LALR(1) parser.
