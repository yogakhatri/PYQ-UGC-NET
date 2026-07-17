# Question 126

*UGC NET CS · 2019 June Paper 1 And 2 · Context-Free Language · Closure Properties of Language Classes*

Let L1 be regular, L2 context-free, L3 recursive, and L4 recursively enumerable. Match List I with List II. List I: (a) complement(L3) union L4; (b) complement(L2) union L3; (c) L1* intersection L2. List II: (i) context-free language; (ii) recursively enumerable language; (iii) recursive language.

- **1.** a-ii, b-i, c-iii
- **2.** a-ii, b-iii, c-i
- **3.** a-iii, b-i, c-ii
- **4.** a-i, b-ii, c-iii

> [!TIP]
> **Correct answer: 2. a-ii, b-iii, c-i**

## Solution

For (a), recursive languages are closed under complement, so complement(L3) is recursive and therefore recursively enumerable; union with the recursively enumerable L4 remains recursively enumerable: (a)-(ii). For (b), complement(L2) need not be context-free, but every CFL is recursive, so its complement is recursive; union with recursive L3 is recursive: (b)-(iii). For (c), L1* is regular, and the intersection of a regular language with a CFL is context-free: (c)-(i).

## Key Points

- Use the strongest guaranteed class after each operation: RE union recursive is RE; recursive is complement-closed; CFL intersect regular is CFL.

## Why the other options are incorrect

The alternative matchings violate at least one closure fact. The important trap is assuming CFLs are closed under complement; they are not, but CFLs are recursive, which makes their complements recursive.
