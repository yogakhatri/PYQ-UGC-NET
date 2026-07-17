# Question 5

*UGC NET CS · 2013 Dec Paper 2 · Network Security · RSA Exponent Calculation*

Using the RSA public key crypto system, if p = 13, q = 31 and d = 7, then the value of e is

- **A.** 101
- **B.** 103
- **C.** 105
- **D.** 107

> [!TIP]
> **Correct answer: B. 103**

## Solution

RSA uses n=pq and phi(n)=(p-1)(q-1)=12 x 30=360. The public and private exponents satisfy ed congruent to 1 modulo 360. With d=7, test e=103: 7 x 103=721=2 x 360+1. Therefore e=103 is the modular inverse of 7 modulo 360.

## Key Points

- Given RSA private exponent d, find e from ed mod phi(n)=1, with phi(n)=(p-1)(q-1).

## Why the other options are incorrect

Multiplying 7 by 101, 105 or 107 gives remainders 347, 15 and 29 modulo 360, not 1. They therefore cannot be the matching RSA exponent.
