# Question 38

*UGC NET CS · 2013 Dec Paper 2 · Counting, Mathematical Induction and Discrete Probability · Permutation Identities*

If n and r are non-negative integers and n ≥ r, then P(n+1,r) equals:

- **A.** P(n,r)(n+1)/(n+1-r)
- **B.** P(n,r)(n+1)/(n-1+r)
- **C.** P(n,r)(n-1)/(n+1-r)
- **D.** P(n,r)(n+1)/(n+1+r)

> [!TIP]
> **Correct answer: A. P(n,r)(n+1)/(n+1-r)**

## Solution

P(n,r)=n!/(n-r)!. Therefore P(n+1,r)=(n+1)!/(n+1-r)!. Divide by P(n,r): the ratio is (n+1)/(n+1-r). Hence P(n+1,r)=P(n,r)(n+1)/(n+1-r).

## Key Points

- Use P(n,r)=n!/(n-r)!
- and simplify factorial ratios before selecting an identity.

## Why the other options are incorrect

The other denominators or numerator n-1 do not arise when cancelling the two factorial formulas. A quick check with r=1 also works: P(n+1,1)=n+1, which only option A reproduces from P(n,1)=n.
