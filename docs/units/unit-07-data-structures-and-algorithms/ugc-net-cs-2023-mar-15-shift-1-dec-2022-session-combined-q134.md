# Question 134

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Performance Analysis and Recurrences · Time and Space Complexity*

Arrange the following in the correct order which respect to key generation for RSA algorithm. A. Choose an integer e such that 1 < e < A(n) B. Compute Key length n = p*q C. Find d which is equal to 1/e D. Choose two large prime numbers p and q E. Compute A(n) Choose the correct answer from the options given below:

- **1.** A-B-C-D-E
- **2.** D-C-B-E-A
- **3.** D-B-E-A-C
- **4.** A-B-D-E-C

> [!TIP]
> **Correct answer: 3. D-B-E-A-C**

## Solution

RSA key generation proceeds as follows: choose distinct primes p and q (D); compute n=pq (B); compute φ(n)=(p−1)(q−1) (E); select e relatively prime to φ(n) (A); and compute d such that ed≡1 mod φ(n) (C). Hence D-B-E-A-C.

## Key Points

- RSA builds the modulus and totient before selecting e and finding its modular inverse d.

## Why the other options are incorrect

The alternatives try to compute n, φ(n), or the modular inverse before the values on which those operations depend have been chosen.
