# Question 77

*UGC NET CS · 2020 Nov With Answers · Context-Free Language · Intersection and Language Simplification*

Let L=L1∩L2, where L1={0^m1^m2 0^n1^n | m,n≥0} and L2={0^m1^n2^k | m,n,k≥0}. How is L classified?

- **1.** Recursively enumerable but not context free
- **2.** Regular
- **3.** Context free but not regular
- **4.** Not recursive

> [!TIP]
> **Correct answer: 3. Context free but not regular**

## Solution

Every L1 string has form 0^m1^m2 0^n1^n. An L2 string must have all 0s first, then all 1s, then all 2s. After L1's single 2, L2 permits no later 0 or 1, so intersection membership forces n=0. Consequently L={0^m1^m2 | m≥0}. This language is context-free—for example S→T2 and T→0T1|ε—but it is not regular because it must match equal numbers of leading 0s and 1s. Hence option 3.

## Key Points

- First simplify the intersection using symbol order; it collapses to {0^m1^m2}, a CFL with one equality constraint.

## Why the other options are incorrect

The language is decidable and context-free, ruling out options 1 and 4. It is not regular: removing the fixed final 2 by right quotient or a pumping-lemma argument leaves the classic nonregular language {0^m1^m}.
