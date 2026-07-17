# Question 121

*UGC NET CS · 2020 Nov With Answers · Language Hierarchy and Closure · Closure-Based Language Classification*

Let L_R be a regular language, L_CF a context-free language, L_REC a recursive language, and L_RE a recursively enumerable language. Match the resulting class: (A) recursively enumerable language, (B) recursive language, (C) context-free language with (I) complement(L_REC) ∪ L_RE, (II) complement(L_CF) ∪ L_REC, (III) L_R* ∩ L_CF.

- **1.** A-II, B-III, C-I
- **2.** A-III, B-I, C-II
- **3.** A-I, B-II, C-III
- **4.** A-II, B-I, C-III

> [!TIP]
> **Correct answer: 3. A-I, B-II, C-III**

## Solution

Recursive languages are closed under complement and are recursively enumerable. Therefore complement(L_REC)∪L_RE is recursively enumerable, giving I→A. Every CFL is recursive; its complement is also recursive, and recursive languages are closed under union, so complement(L_CF)∪L_REC is recursive, giving II→B. L_R* remains regular, and CFLs are closed under intersection with regular languages, so L_R*∩L_CF is context-free, giving III→C. Thus A-I, B-II, C-III, option 3.

## Key Points

- Use the hierarchy Regular⊂CFL⊂Recursive⊂RE plus closure of CFL under intersection with a regular language.

## Why the other options are incorrect

The other mappings ignore one of the containment or closure facts. CFLs are not closed under complement as CFLs, but their complements are still recursive because CFL membership is decidable.
