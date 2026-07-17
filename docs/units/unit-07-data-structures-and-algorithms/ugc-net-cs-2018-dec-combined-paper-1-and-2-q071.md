# Question 71

*UGC NET CS · 2018 Dec Paper 1 And 2 · Performance Analysis and Recurrences · Recurrences with Square-Root Subproblems*

What is the asymptotic solution of T(n)=2T(√n)+lg n?

- **1.** O(lg n)
- **2.** O(n lg n)
- **3.** O((lg n)²)
- **4.** O(lg n · lg(lg n))

> [!TIP]
> **Correct answer: 4. O(lg n · lg(lg n))**

## Solution

The square-root argument becomes easier after changing variables. Put m=lg n and define S(m)=T(2ᵐ). Since √n=2^(m/2), the recurrence becomes S(m)=2S(m/2)+m. By the Master Theorem, a=2, b=2, and f(m)=Θ(m)=Θ(m^(log₂2)), so S(m)=Θ(m lg m). Substituting m=lg n gives T(n)=Θ(lg n·lg(lg n)), which matches option 4.

## Key Points

- For recurrences involving √n, set m=log n; square roots then become halving and an ordinary Master-Theorem recurrence appears.

## Why the other options are incorrect

O(lg n) misses the extra number of recursion levels in the transformed problem. O((lg n)²) is a looser growth form than the intended tight result, and O(n lg n) is far too large because each recursion step takes a square root of n.
