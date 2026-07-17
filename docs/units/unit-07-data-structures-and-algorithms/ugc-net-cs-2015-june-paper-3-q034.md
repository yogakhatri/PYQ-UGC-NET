# Question 34

*UGC NET CS · 2015 June Paper 3 · Hashing · Multiplication-Method Hashing*

Consider a hash table of size m=100 and the multiplication-method hash h(k)=floor(m(kA mod 1)), where A=(√5−1)/2=0.618033. Compute the location for key k=123456.

- **1.** 77
- **2.** 82
- **3.** 88
- **4.** 89

> [!TIP]
> **Correct answer: Using the explicitly supplied rounded value A=0.618033 gives option 3 (location 88). Using the exact radical A=(√5−1)/2 gives location 0, which is absent; the question is numerically inconsistent.**

## Solution

With the printed decimal, `123456 × 0.618033 = 76299.882048`. The fractional part is `0.882048`; multiplying by m=100 gives `88.2048`, and flooring yields `h=88`. However, the exact golden-ratio conjugate is approximately `0.618033988749895`, giving `123456A ≈ 76300.004115107`, fractional part about `0.004115107`, and hash 0. The equality sign between the exact radical and the truncated decimal is therefore unsafe for this large key.

## Key Points

- Multiplication hashing uses the fractional part of kA; early rounding of A can radically change a bucket for large k.

## Why the other options are incorrect

Under the six-decimal value stated for calculation, 77, 82, and 89 do not equal the floored result. Yet option 88 should be treated as the exam-intended rounded calculation, not as the result of the exact radical.
