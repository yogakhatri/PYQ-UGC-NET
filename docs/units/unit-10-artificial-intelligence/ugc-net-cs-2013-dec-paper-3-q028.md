# Question 28

*UGC NET CS · 2013 Dec Paper 3 · Fuzzy Sets · Fuzzy-Set Intersection*

If A and B are two fuzzy sets with membership functions μA(x) = {0.2, 0.5, 0.6, 0.1, 0.9} μB(x) = {0.1, 0.5, 0.2, 0.7, 0.8} Then the value of μA ∩ B will be

- **A.** {0.2, 0.5, 0.6, 0.7, 0.9}
- **B.** {0.2, 0.5, 0.2, 0.1, 0.8}
- **C.** {0.1, 0.5, 0.6, 0.1, 0.8}
- **D.** {0.1, 0.5, 0.2, 0.1, 0.8}

> [!TIP]
> **Correct answer: D. {0.1, 0.5, 0.2, 0.1, 0.8}**

## Solution

The standard fuzzy intersection uses the componentwise minimum. Taking min for each pair gives {min(0.2,0.1),min(0.5,0.5),min(0.6,0.2),min(0.1,0.7),min(0.9,0.8)}={0.1,0.5,0.2,0.1,0.8}.

## Key Points

- Standard fuzzy union uses max; standard fuzzy intersection uses min; complement uses 1-μ.

## Why the other options are incorrect

A resembles componentwise maximum (union). B and C use the larger membership in at least one position. Intersection cannot exceed either input membership at the same element.
