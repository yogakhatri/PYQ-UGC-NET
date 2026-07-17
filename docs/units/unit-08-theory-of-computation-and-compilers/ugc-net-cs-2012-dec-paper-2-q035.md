# Question 35

*UGC NET CS · 2012 Dec Paper 2 · Syntax Analysis · Relative Power of Parsing Methods*

Which is the most powerful parsing method?

- **1.** LL(1)
- **2.** Canonical LR
- **3.** SLR
- **4.** LALR

> [!TIP]
> **Correct answer: 2. Canonical LR**

## Solution

Canonical LR(1) constructs items with individual lookahead symbols and recognizes the largest grammar class among the listed deterministic parsing methods. Its detailed states avoid reductions that would conflict in coarser LR tables, so it is more powerful than SLR and LALR and far more powerful than LL(1).

## Key Points

- Power order for these choices: LL(1) is weakest; SLR and LALR cover more grammars; canonical LR(1) is the most powerful.

## Why the other options are incorrect

LL(1) is a restricted top-down method. SLR uses FOLLOW sets for reductions and can introduce conflicts. LALR merges LR(1) states with identical LR(0) cores, producing smaller tables but sometimes creating conflicts that canonical LR(1) avoids.
