# Question 44

*UGC NET CS · 2014 Dec Paper 3 · Software Metrics · Function-Point Value-Adjustment Factors*

Function points are computed as FP = Count-total × (0.65 + 0.01ΣFᵢ), where the Fᵢ values are degree-of-influence ratings for n value-adjustment questions. What is n?

- **A.** 12
- **B.** 14
- **C.** 16
- **D.** 18

> [!TIP]
> **Correct answer: B. 14**

## Solution

The classic IFPUG-style value adjustment factor uses 14 general system characteristics. Each characteristic receives a degree-of-influence rating, and their sum enters VAF = 0.65 + 0.01ΣFᵢ. Hence the index runs from i=1 through n=14.

## Key Points

- Classic adjusted function points use 14 general system characteristics in the VAF calculation.

## Why the other options are incorrect

12, 16, and 18 are not the number of general system characteristics in this standard function-point adjustment model. With 14 characteristics each rated 0–5, the sum ranges 0–70 and the adjustment factor ranges 0.65–1.35, which is a useful consistency check.
