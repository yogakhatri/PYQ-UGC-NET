# Question 35

*UGC NET CS · 2014 Dec Paper 2 · Context-Free Grammars · Equal-Count Grammar Invariants*

The context-free grammar S→aB|bA, A→a|aS|bAA, B→b|bS|aBB generates strings with

- **A.** odd numbers of a’s and odd numbers of b’s
- **B.** even numbers of a’s and even numbers of b’s
- **C.** equal numbers of a’s and b’s
- **D.** different numbers of a’s and b’s

> [!TIP]
> **Correct answer: C. equal numbers of a’s and b’s**

## Solution

Track Δ=#a−#b. Nonterminal A always derives strings with Δ=+1: A→a gives +1, A→aS adds +1 to a balanced S string, and A→bAA gives −1+1+1=+1. Symmetrically, B always has Δ=−1. Then S→aB has +1−1=0 and S→bA has −1+1=0. Hence every S-string contains equal numbers of a's and b's.

## Key Points

- Assign each nonterminal a count invariant: S balances to 0, A to +1 and B to −1.

## Why the other options are incorrect

Equal counts can be even or odd, so A and B are too restrictive. D is the opposite of the invariant established by every production.
