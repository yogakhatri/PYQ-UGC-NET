# Question 70

*UGC NET CS · 2016 July Paper 3 · Mathematical Logic · Negating Compound Inequalities*

Consider the statement, “Either – 2 ≤ x ≤ – 1 or 1 ≤ x ≤2”. The negation of this statement is

- **1.** x < – 2 or 2 < x or – 1 < x < 1
- **2.** x < – 2 or 2 < x
- **3.** – 1 < x < 1
- **4.** x ≤ −2 or 2 ≤ x or −1 < x < 1

> [!TIP]
> **Correct answer: 1. x < – 2 or 2 < x or – 1 < x < 1**

## Solution

Let P be −2≤x≤−1 and Q be 1≤x≤2. The statement is P∨Q, so De Morgan's law gives ¬P∧¬Q: x must lie outside both closed intervals. On the real line that complement is x<−2, or −1<x<1, or x>2. This is exactly option 1.

## Key Points

- The negation of membership in a union of closed intervals is the complement: the two outer open rays plus every open gap between the intervals.

## Why the other options are incorrect

Option 2 omits the entire gap between −1 and 1. Option 3 omits both exterior rays. Option 4 uses non-strict endpoints and would include −2 and 2 even though both satisfy the original statement and therefore must be excluded from its negation.
