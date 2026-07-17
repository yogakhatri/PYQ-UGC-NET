# Question 74

*UGC NET CS · 2013 June Paper 3 · Fuzzy Sets · Complement of a Fuzzy Union*

If A and B are fuzzy sets with μ_A(x)={0.6,0.5,0.1,0.7,0.8} and μ_B(x)={0.9,0.2,0.6,0.8,0.5}, then the value of μ_complement(A∪B)(x) is

- **A.** {0.9, 0.5, 0.6, 0.8, 0.8}
- **B.** {0.6, 0.2, 0.1, 0.7, 0.5}
- **C.** {0.1, 0.5, 0.4, 0.2, 0.2}
- **D.** {0.1, 0.5, 0.4, 0.2, 0.3}

> [!TIP]
> **Correct answer: C. {0.1, 0.5, 0.4, 0.2, 0.2}**

## Solution

For a fuzzy union, take the componentwise maximum: μ_(A∪B)={0.9,0.5,0.6,0.8,0.8}. The question asks for the complement of that union, whose standard membership is 1−μ. Subtracting each entry from 1 gives {0.1,0.5,0.4,0.2,0.2}, option C.

## Key Points

- Fuzzy union=max; standard complement=1−membership.
- Apply them in the order indicated by the bar.

## Why the other options are incorrect

A is the union itself before complementation. B is the componentwise minimum, namely the intersection A∩B. D matches the first four complement values but incorrectly computes 1−0.8 as 0.3 instead of 0.2.
