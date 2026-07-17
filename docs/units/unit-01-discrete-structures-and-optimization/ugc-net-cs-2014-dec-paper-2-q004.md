# Question 4

*UGC NET CS · 2014 Dec Paper 2 · Counting, Mathematical Induction and Discrete Probability · Probability of at least one occurrence*

A computer program selects an integer in the set {k : 1 ≤ k ≤ 10,00,000} at random and prints out the result. This process is repeated 1 million times. What is the probability that the value k = 1 appears in the printout atleast once ?

- **A.** 0.5
- **B.** 0.704
- **C.** 0.632121
- **D.** 0.68

> [!TIP]
> **Correct answer: C. 0.632121**

## Solution

On each independent draw, P(k≠1)=1−1/1,000,000. The probability that 1 never appears in one million draws is (1−10^−6)^1,000,000. Therefore P(at least one 1)=1−(1−10^−6)^1,000,000≈1−e^−1=0.63212056, which rounds to 0.632121.

## Key Points

- At least once = 1 − never; (1−1/n)^n approaches e^−1.

## Why the other options are incorrect

The expected number of occurrences is 1, but that does not make the occurrence probability 1 or 0.5. The other decimals do not match the complement of the zero-occurrence probability.
