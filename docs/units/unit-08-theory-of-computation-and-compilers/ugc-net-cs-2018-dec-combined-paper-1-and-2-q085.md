# Question 85

*UGC NET CS · 2018 Dec Paper 1 And 2 · Context-Free Language · PDA Construction and Non-CFL Proofs*

Consider L₁={a^(n+m)b^n a^m | n,m≥0} and L₂={a^(n+m)b^(n+m)a^(n+m) | n,m≥0}. Which statement is correct?

- **1.** Only L1 is context-free
- **2.** Only L2 is context-free
- **3.** Both L1 and L2 are context-free
- **4.** Neither L1 nor L2 is context-free

> [!TIP]
> **Correct answer: 1. Only L1 is context-free**

## Solution

L₁ is context-free. One grammar is S→aSa | T and T→aTb | ε. Applying S→aSa m times creates matching outer a’s, then applying T→aTb n times creates a^n b^n, yielding a^m a^n b^n a^m=a^(n+m)b^n a^m. For L₂, put p=n+m; then L₂={a^p b^p a^p | p≥0}, the standard non-context-free triple-equality language. Thus only L₁ is context-free, option 1.

## Key Points

- Prove CFL membership constructively with a grammar; recognize a^p b^p a^p as a classic non-CFL requiring two independent equality checks.

## Why the other options are incorrect

Options 2 and 3 incorrectly classify L₂ as context-free; one stack cannot enforce equality of all three separated block lengths. Option 4 overlooks the explicit context-free grammar for L₁.
