# Question 98

*UGC NET CS · 2018 Dec Paper 1 And 2 · Java Programming · Recursive Geometric Series and Integer Overflow*

Consider the following recursive Java function f that takes two long arguments and returns a float value: public static float f(long m, long n) { float result = (float) m / (float) n; if (m < 0 || n < 0) return 0.0f; else result += f(m*2, n*3); return result; } Which of the following integers best approximates the value of f(2, 3)?

- **1.** 0
- **2.** 1
- **3.** 2
- **4.** 3

> [!TIP]
> **Correct answer: 3. 2**

## Solution

Ignoring the eventual fixed-width overflow for a moment, successive nonnegative calls contribute 2/3, 4/9, 8/27, ... . This is a geometric series with first term 2/3 and ratio 2/3, so its infinite sum is (2/3)/(1-2/3)=2. Java long multiplication eventually overflows; in the actual execution n becomes negative and the base case returns 0, so the program adds a long finite prefix rather than the mathematical infinite series. By that point the omitted tail is tiny, and single-precision accumulation is about 1.9999999. The nearest listed integer is 2, option 3.

## Key Points

- Recognize the recursive ratio sequence as a geometric series, then account for fixed-width overflow only as the mechanism that terminates a very accurate finite approximation.

## Why the other options are incorrect

0 and 1 are already contradicted by the positive early partial sums: 2/3+4/9≈1.111. The total cannot approach 3 because the complete geometric-series limit is 2, and truncating the positive series before overflow does not increase that limit.
