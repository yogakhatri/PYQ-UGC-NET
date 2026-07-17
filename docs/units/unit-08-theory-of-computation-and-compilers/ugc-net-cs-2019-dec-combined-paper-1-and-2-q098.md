# Question 98

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Grammars · Inherently Ambiguous Languages*

Consider L1 = {a^n b^n c^m | n,m ≥ 0} ∪ {a^n b^m c^m | n,m ≥ 0} and L2 = {ww^R | w ∈ {a,b}*}, where w^R is the reversal of w. Which language(s) are inherently ambiguous?

- **1.** Only L1
- **2.** Only L2
- **3.** Both L1 and L2
- **4.** Neither L1 nor L2

> [!TIP]
> **Correct answer: 1. Only L1**

## Solution

L1 is the classic inherently ambiguous language formed by the union of strings satisfying i=j and strings satisfying j=k. Their overlap is {a^n b^n c^n | n≥0}; strings in that overlap meet both independent counting conditions. The standard inherent-ambiguity result shows that no context-free grammar for the whole union can make all such overlap strings unambiguous. By contrast, L2 is the language of even-length palindromes and has the unambiguous grammar S→aSa | bSb | ε: the two outer symbols uniquely choose the production at every step. Therefore only L1 is inherently ambiguous, option 1.

## Key Points

- Inherent ambiguity is a property of a language, not just a grammar; one unambiguous grammar is enough to show that a language is not inherently ambiguous.

## Why the other options are incorrect

Options 2 and 3 wrongly classify L2 as inherently ambiguous; an explicit unambiguous grammar disproves that. Option 4 wrongly treats L1 as merely ambiguous under one grammar, whereas this union is the standard example whose ambiguity cannot be removed by choosing another grammar.
