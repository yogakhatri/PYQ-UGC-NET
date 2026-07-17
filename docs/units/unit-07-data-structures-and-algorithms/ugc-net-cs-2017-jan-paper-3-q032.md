# Question 32

*UGC NET CS · 2017 Jan Paper 3 · Lower-Bound Theory · Comparison-Sorting Decision Trees*

Any decision tree that sorts n elements has height ________.

- **1.** Ω(lg n)
- **2.** Ω(n)
- **3.** Ω(n lg n)
- **4.** Ω(n²)

> [!TIP]
> **Correct answer: 3. Ω(n lg n)**

## Solution

A comparison sort must distinguish all n! possible input orders of n distinct elements. Its decision tree is binary, so a tree of height h has at most 2^h leaves. Thus 2^h≥n!, giving h≥lg(n!). By Stirling's approximation, lg(n!)=Θ(n lg n). Hence every comparison-sorting decision tree has height Ω(n lg n), which is option 3.

## Key Points

- n!
- possible permutations require at least lg(n!)=Θ(n lg n) binary comparison outcomes.

## Why the other options are incorrect

Ω(lg n) and Ω(n) are weaker statements and do not express the tight comparison lower bound. Ω(n²) is too large because algorithms such as mergesort and heapsort use O(n lg n) comparisons.
