# Question 27

*UGC NET CS · 2012 Dec Paper 2 · Syntax Analysis · LL(1) Grammar Transformations*

Which is true while converting a CFG to an LL(1) grammar?

- **1.** Remove left recursion alone
- **2.** Factor the grammar alone
- **3.** Both of the above
- **4.** None of the above

> [!TIP]
> **Correct answer: 3. Both of the above**

## Solution

A predictive LL(1) parser must choose a production using one lookahead symbol. Immediate or indirect left recursion prevents such top-down parsing and must be eliminated. Common left prefixes also delay the choice between alternatives, so the grammar is left-factored to expose the decision point. Hence both transformations are used when preparing a suitable grammar.

## Key Points

- LL(1) preparation normally requires both elimination of left recursion and left factoring, followed by FIRST/FOLLOW conflict checks.

## Why the other options are incorrect

Removing only left recursion can leave alternatives with indistinguishable prefixes. Left factoring alone can leave recursive nonterminals that make a top-down parser loop. Also, these transformations are necessary preparation but do not guarantee that every context-free grammar has an equivalent LL(1) grammar.
