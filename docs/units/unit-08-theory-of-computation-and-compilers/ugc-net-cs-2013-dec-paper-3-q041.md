# Question 41

*UGC NET CS · 2013 Dec Paper 3 · Context-Free Grammars · Greibach Normal Form*

The Greibach normal form grammar for the language L = {an bn + 1 | n ≥ 0} is

- **A.** S → a SB, B → bB | λ
- **B.** S → a SB, B → bB | b
- **C.** S → a SB | b, B → b
- **D.** S → a Sb | b

> [!TIP]
> **Correct answer: C. S → a SB | b, B → b**

## Solution

The grammar S→aSB | b and B→b generates exactly a^n b^(n+1). The base rule S→b gives n=0. Each application of S→aSB adds one a at the front and one B at the end; converting every B to b adds one matching trailing b, while the base b supplies the one extra b. It is in Greibach normal form because every production begins with a terminal followed only by zero or more variables.

## Key Points

- In GNF every rule has the form A→aA1...Ak: one leading terminal, then variables only.

## Why the other options are incorrect

A allows B→lambda and therefore does not force one trailing b per recursive a. B has no terminating production for S, so it cannot derive a terminal string. D describes the language but is not in GNF because its right side contains terminal b after variable S.
