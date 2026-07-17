# Question 35

*UGC NET CS · 2013 Dec Paper 2 · Performance Analysis and Recurrences · Dominant Asymptotic Terms*

Big – O estimate for f( x) = ( x + 1) log( x2 + 1) + 3 x2 is given as

- **A.** O( x log x)
- **B.** O( x2)
- **C.** O( x3)
- **D.** O( x2 log x)

> [!TIP]
> **Correct answer: B. O( x2)**

## Solution

For large x, log(x²+1)=Θ(log x), so (x+1)log(x²+1)=Θ(x log x). The remaining term is 3x²=Θ(x²), which grows faster than x log x. The whole sum is therefore Θ(x²), and hence O(x²).

## Key Points

- For sums, keep the asymptotically dominant term.
- Polynomial x² dominates x log x.

## Why the other options are incorrect

O(x log x) is too small because of the quadratic term. O(x³) and O(x² log x) are valid loose upper bounds in a purely formal sense, but the question asks for the standard tight Big-O estimate among the choices; O(x²) is the tightest listed.
