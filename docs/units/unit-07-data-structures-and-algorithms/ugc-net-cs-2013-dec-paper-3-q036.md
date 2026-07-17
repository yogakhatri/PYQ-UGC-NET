# Question 36

*UGC NET CS · 2013 Dec Paper 3 · Performance Analysis and Recurrences · Master-Theorem Cases*

The recurrence T(n)=mT(n/2)+an^2 is satisfied by which asymptotic bound?

- **A.** O(n^2)
- **B.** O(n^(log2 m))
- **C.** O(n^2 log n)
- **D.** O(n log n)

> [!TIP]
> **Correct answer: The printed question is under-specified: Theta(n^2) if m<4, Theta(n^2 log n) if m=4, and Theta(n^(log2 m)) if m>4.**

## Solution

Write the recurrence in Master-theorem form T(n)=mT(n/2)+Theta(n^2). The critical exponent is log2 m, so compare n^2 with n^(log2 m). If m<4, then log2 m<2 and the nonrecursive n^2 work dominates, giving Theta(n^2). If m=4, the two terms balance, giving Theta(n^2 log n). If m>4, the recursive leaves dominate, giving Theta(n^(log2 m)). Because the paper supplies no value or range for m, none of A, B or C is the unique answer for all m.

## Key Points

- For T(n)=aT(n/b)+f(n), compare f(n) with n^(log_b a); here the threshold is m=4.

## Why the other options are incorrect

A is valid only when m<4, C only when m=4, and B is the tight bound only when m>4. D does not arise for positive constant m with an n^2 combine term. Choosing one option without a condition on m hides the missing information.
