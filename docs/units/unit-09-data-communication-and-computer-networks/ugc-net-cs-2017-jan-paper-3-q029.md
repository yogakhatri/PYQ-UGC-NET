# Question 29

*UGC NET CS · 2017 Jan Paper 3 · Network Security · RSA Encryption, Decryption, and Key Congruence*

In RSA, let n=pq, φ(n)=(p−1)(q−1), public key (e,n), private key (d,n), and 0<M<n. Which statements are correct? I. C≡M^e (mod n) and M≡C^d (mod n). II. ed≡1 (mod n). III. ed≡1 (mod φ(n)). IV. C≡M^e (mod φ(n)) and M≡C^d (mod φ(n)).

- **1.** I and II
- **2.** I and III
- **3.** II and III
- **4.** I and IV

> [!TIP]
> **Correct answer: 2. I and III**

## Solution

RSA encrypts and decrypts modulo n: C≡M^e (mod n) and M≡C^d (mod n), so statement I is correct. The exponents are chosen as multiplicative inverses modulo φ(n) in the formulation used here, so ed≡1 (mod φ(n)); statement III is correct. There is no general requirement ed≡1 (mod n), and the message operations are not performed modulo φ(n). Hence I and III are correct, giving option 2.

## Key Points

- RSA data arithmetic is modulo n; the textbook key relation is ed≡1 modulo φ(n).

## Why the other options are incorrect

Statement II uses the wrong modulus for the exponent-inverse condition. Statement IV uses φ(n) instead of n for encryption and decryption. Every option other than 2 includes one of those incorrect statements or omits a correct one.
