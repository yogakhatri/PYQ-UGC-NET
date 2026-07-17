# Question 25

*UGC NET CS · 2015 Dec Paper 2 · Network Security · RSA Encryption*

Using p=3, q=13, d=7, and e=3 in RSA, what is the ciphertext for plaintext 5?

- **1.** 13
- **2.** 21
- **3.** 26
- **4.** 33

> [!TIP]
> **Correct answer: No listed option — the ciphertext computed from p=3, q=13, e=3 is 8**

## Solution

RSA encryption uses n=pq=3×13=39 and c=m^e mod n. For m=5 and e=3, c=5³ mod 39=125 mod 39=8. The private exponent d is not used during encryption. There is a second defect: φ(39)=24, but ed=3×7=21 is not congruent to 1 modulo 24, so the printed e and d do not form a valid RSA exponent pair.

## Key Points

- RSA encryption: c=m^e mod(pq); verify separately that ed≡1 mod φ(n) for a consistent key pair.

## Why the other options are incorrect

13, 21, 26, and 33 are all different from the correctly reduced residue 8. Selecting any listed value would require changing the printed parameters or using a non-RSA calculation.
