# Question 113

*UGC NET CS · 2019 June Paper 1 And 2 · Selected Topics · Euler Phi Function*

Consider Euler's phi function phi(n) = n product over primes p dividing n of (1 - 1/p). What is phi(45)?

- **1.** 3
- **2.** 12
- **3.** 6
- **4.** 24

> [!TIP]
> **Correct answer: 4. 24**

## Solution

Factor 45 as 3^2 x 5. Euler's product formula uses each distinct prime divisor once: phi(45)=45(1-1/3)(1-1/5). Therefore phi(45)=45 x (2/3) x (4/5)=24. Equivalently, 24 integers from 1 through 45 are relatively prime to 45.

## Key Points

- If n has distinct prime divisors p, then phi(n)=n times the product of (1-1/p).

## Why the other options are incorrect

The values 3, 6 and 12 result from misusing the exponents or subtracting prime factors instead of multiplying by the two factors (1-1/p).
