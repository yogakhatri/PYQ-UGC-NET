# Question 35

*UGC NET CS · 2018 July Paper 2 · Context-Free Grammars · Chomsky Normal Form Production Count*

To obtain a string of n Terminals from a given Chomsky normal form grammar, the number of productions to be used is :

- **1.** 2n−1
- **2.** 2n
- **3.** n+1
- **4.** n²

> [!TIP]
> **Correct answer: 1. 2n−1**

## Solution

In Chomsky normal form, a derivation of n terminals has a binary parse tree. It needs n terminal productions of the form A→a, one for each leaf. A full binary tree with n leaves has n−1 internal binary productions A→BC. Total productions used are n+(n−1)=2n−1. Therefore option 1 is correct.

## Key Points

- CNF parse tree with n terminal leaves has n−1 binary internal nodes, so derivation length is 2n−1.

## Why the other options are incorrect

2n has one extra step; n+1 is too small once n grows; n² has no basis in the binary-tree structure. The count assumes n≥1 and ordinary CNF derivation of a nonempty string.
