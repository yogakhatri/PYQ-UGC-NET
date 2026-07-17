# Question 82

*UGC NET CS · 2020 Nov With Answers · Network Security · RSA Key and Encryption Calculation*

Using the RSA public-key cryptosystem, if p = 3, q = 11 and d = 7, find the value of e and encrypt the number 19.

- **1.** 20, 19
- **2.** 33, 11
- **3.** 3, 28
- **4.** 77, 28

> [!TIP]
> **Correct answer: 3. 3, 28**

## Solution

RSA uses n=pq=3×11=33 and φ(n)=(p−1)(q−1)=2×10=20. The public exponent e must satisfy ed≡1 (mod 20). With d=7, e=3 works because 3×7=21≡1 (mod 20). Encryption of m=19 is c=m^e mod n=19³ mod 33. Since 19²=361≡31 (mod 33), c≡31×19=589≡28 (mod 33). Thus (e,c)=(3,28), option 3.

## Key Points

- Find e as the modular inverse of d modulo φ(n), then compute c=m^e mod n.

## Why the other options are incorrect

20 is φ(n), not the public exponent; 33 is the modulus n, not e. The value 77 does not satisfy the standard choice 1<e<φ(n) and is merely congruent to 17 modulo 20, whose product with 7 is not 1 modulo 20.
