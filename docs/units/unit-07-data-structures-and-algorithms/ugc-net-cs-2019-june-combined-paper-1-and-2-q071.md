# Question 71

*UGC NET CS · 2019 June Paper 1 And 2 · Selected Topics · Exponentiation by squaring*

Consider the following pseudocode, whose loop invariant is m*x^k=p^n and k>=0, where p and n are initialized integer variables. Preconditions: p>=1 and n>=0; assume no overflow. Initialize x=p, k=n, m=1. While k!=0: if k is odd, set m=m*x; then set x=x*x and k=floor(k/2). Which must be true at the end of the while loop?

- **1.** x=p^n
- **2.** m=p^n
- **3.** p=x^n
- **4.** p=m^n

> [!TIP]
> **Correct answer: 2. m=p^n**

## Solution

The loop invariant is m·x^k=p^n. The loop stops only when k=0. Substituting k=0 into the invariant gives m·x^0=p^n. Since x^0=1, this reduces to m=p^n. The repeated squaring changes x during execution, so no corresponding final equality for x is required.

## Key Points

- Evaluate a loop invariant together with the loop's termination condition to obtain the postcondition.

## Why the other options are incorrect

- **Option 1:** x is repeatedly squared and need not equal p^n at termination.
- **Options 3 and 4:** neither equality follows from the invariant when k becomes zero.

## Additional Information

The algorithm is binary exponentiation. It computes p^n using O(log n) loop iterations rather than n multiplications.
