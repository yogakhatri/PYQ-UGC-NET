# Question 89

*UGC NET CS · 2019 Dec Paper 1 And 2 · Performance Analysis and Recurrences · Square-Root Recurrences*

Give the asymptotic upper and lower bound for T(n), where T(n) is constant for n<=2 and T(n)=4T(sqrt(n))+(log n)^2.

- **1.** Theta(log((log n)^2) log n)
- **2.** Theta((log n)^2 log n)
- **3.** Theta((log n)^2 log log n)
- **4.** Theta(log(log n) log n)

> [!TIP]
> **Correct answer: 3. Theta((log n)^2 log log n)**

## Solution

Substitute m=log n and define S(m)=T(2^m). Because sqrt(2^m)=2^(m/2), the recurrence becomes S(m)=4S(m/2)+m². The Master Theorem has a=4, b=2, so m^(log_b a)=m², exactly matching the nonrecursive term. Therefore S(m)=Theta(m² log m). Replacing m by log n gives T(n)=Theta((log n)² log log n), option 3.

## Key Points

- For square-root recurrences, transform the input with m=log n; the recurrence then becomes an ordinary divide-by-two Master-Theorem form.

## Why the other options are incorrect

Option 2 adds a full extra log n factor instead of the one log log n factor produced by the recursion depth in m. Options 1 and 4 are only about Theta(log n log log n), missing the squared log n factor contributed at every balanced recurrence level.
