# Question 86

*UGC NET CS · 2018 July Paper 2 · Sets and Relations · Infinite Unions of Nested Sets*

If Ai={−i,…,−2,−1,0,1,2,…,i}, what is ⋃(i=1 to ∞) Ai?

- **1.** Z
- **2.** Q
- **3.** R
- **4.** C

> [!TIP]
> **Correct answer: 1. Z**

## Solution

Each Ai contains every integer from −i through i. Any integer z belongs to A|z| (or to A1 when z=0), so every integer appears in the union. Conversely, every element of every Ai is an integer, so the union contains nothing outside Z. Thus ⋃(i=1 to ∞)Ai=Z, option 1.

## Key Points

- For nested sets A1⊆A2⊆…, identify which stage contains an arbitrary candidate element.

## Why the other options are incorrect

The union includes no non-integer rational, irrational, or complex numbers, so it cannot be Q, R, or C. An infinite union of finite sets need not be uncountable; here it is exactly the countably infinite integers.
