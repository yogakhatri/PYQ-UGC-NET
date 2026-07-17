# Question 35

*UGC NET CS · 2014 Dec Paper 3 · Advanced Algorithms · Matrix-Chain Multiplication Cost*

A matrix chain ⟨A₁,A₂,A₃⟩ has dimensions 10×100, 100×5, and 5×50, respectively. Comparing (i) ((A₁A₂)A₃) with (ii) (A₁(A₂A₃)), how many times smaller is the scalar-multiplication count for the first parenthesization?

- **A.** 5
- **B.** 10
- **C.** 20
- **D.** 100

> [!TIP]
> **Correct answer: B. 10**

## Solution

For ((A₁A₂)A₃), A₁A₂ costs 10×100×5=5,000 scalar multiplications and produces a 10×5 matrix. Multiplying it by A₃ costs 10×5×50=2,500, for a total of 7,500. For A₁(A₂A₃), the first product costs 100×5×50=25,000 and the second costs 10×100×50=50,000, totaling 75,000. The ratio 75,000/7,500 is 10, so the first ordering uses one-tenth as many multiplications.

## Key Points

- Multiplying a p×q matrix by a q×r matrix costs pqr scalar multiplications; add every stage before comparing parenthesizations.

## Why the other options are incorrect

5, 20, and 100 do not equal the ratio of the two total operation counts. A common error is to compare only the first multiplication in each parenthesization; both multiplication costs must be added before taking the ratio.
