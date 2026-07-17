# Question 12

*UGC NET CS · 2013 June Paper 3 · Performance Analysis and Recurrences · Square-Root Argument Recurrences*

Find the asymptotic solution of T(n)=2T(floor(sqrt(n)))+log n.

- **A.** O(n log log log n)
- **B.** O(n log log n)
- **C.** O(log log n)
- **D.** O(log n log log n)

> [!TIP]
> **Correct answer: D. O(log n log log n)**

## Solution

The unusual square-root subproblem becomes ordinary after a logarithmic substitution. Let m=log n and define S(m)=T(e^m). Since sqrt(n)=e^(m/2), the recurrence becomes S(m)=2S(m/2)+m. The Master theorem has a=2, b=2 and f(m)=m=Theta(m^(log_2 2)), so S(m)=Theta(m log m). Substituting m=log n gives T(n)=Theta(log n·log log n).

## Key Points

- For recurrences on sqrt(n), set m=log n; square root becomes halving and Master-theorem analysis applies.

## Why the other options are incorrect

A and B incorrectly retain a factor n even though repeatedly taking square roots makes the recursion depth only log log n. C counts roughly the depth but ignores the work across levels. D contains both the per-level/logarithmic work and the log-log number of balanced levels.
