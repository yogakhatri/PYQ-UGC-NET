# Question 27

*UGC NET CS · 2013 Dec Paper 2 · Context-Free Language · CFG Construction for Count Inequalities*

The context free grammar for the language L = {a n bm | n ≤ m + 3, n ≥ 0, m ≥ 0} is

- **A.** S → aaa A; A → aAb | B, B → Bb | λ
- **B.** S → aaaA| λ, A → aAb | B, B → Bb | λ
- **C.** S → aaaA | aa A | λ, A → aAb | B, B → Bb| λ
- **D.** S → aaaA | aa A | aA | λ, A → aAb | B, B → Bb | λ

> [!TIP]
> **Correct answer: None exactly; option D needs its final λ alternative replaced by A**

## Solution

Write n=m+k-r, where k is the number of extra leading a symbols (0 to 3) and r is the number of extra trailing b symbols. Let A -> aAb | B generate equal a/b pairs followed by B, and B -> Bb | λ generate any extra b symbols. The start rule must be S -> A | aA | aaA | aaaA. This generates every a^n b^m with n-m at most 3, including b^m when n=0.

## Key Points

- For n<=m+3, allow 0, 1, 2 or 3 unpaired leading a symbols, then generate matched a/b pairs and arbitrary extra trailing b symbols.

## Why the other options are incorrect

A permits only surplus 3. B adds only the empty string, and C permits surpluses 2 or 3 plus empty. D is closest but uses λ instead of A; consequently it cannot generate b, bb and other required strings with n=0,m>0. The printed choices therefore omit the correct grammar.
