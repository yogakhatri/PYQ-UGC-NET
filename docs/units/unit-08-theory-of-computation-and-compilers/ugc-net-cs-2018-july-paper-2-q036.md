# Question 36

*UGC NET CS · 2018 July Paper 2 · Context-Free Grammars · Ambiguous Grammars and Multiple Parse Trees*

Consider two grammars: G1: S→SbS|a. G2 (as printed): S→aB|ab, A→GAB|a, B→ABb|b. Which statement about ambiguity is correct?

- **1.** Only G1 is ambiguous
- **2.** Only G2 is ambiguous
- **3.** Both G1 and G2 are ambiguous
- **4.** Both G1 and G2 are not ambiguous

> [!TIP]
> **Correct answer: 3. Both G1 and G2 are ambiguous**

## Solution

G1 is ambiguous: the string `ababa` can group as `(a b a) b a` or `a b (a b a)`, producing two parse trees under S→SbS|a. G2 is also ambiguous because `ab` has two parse trees immediately: S→ab directly, or S→aB→ab using B→b. This witness does not depend on the questionable printed A-production. Hence both grammars are ambiguous, option 3.

## Key Points

- One terminal string with two structurally different parse trees proves a grammar ambiguous.

## Why the other options are incorrect

Options 1, 2, and 4 deny one of two explicit ambiguity witnesses. Different leftmost and rightmost derivation orders of the same tree are not enough, but the examples here genuinely change which production/tree is used.
