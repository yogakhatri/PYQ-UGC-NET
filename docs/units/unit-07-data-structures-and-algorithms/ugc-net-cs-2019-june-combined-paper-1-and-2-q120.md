# Question 120

*UGC NET CS · 2019 June Paper 1 And 2 · Selected Topics · Euler and Fermat Theorems*

Consider S1: for every integer n>1, a^phi(n) is congruent to 1 (mod n) for every a relatively prime to n. S2: if p is prime, then a^(p-1) is congruent to 1 (mod p) for every a not divisible by p. Which statements are correct?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 3. Both S1 and S2**

## Solution

S1 is Euler's theorem: when gcd(a,n)=1, a^phi(n) is congruent to 1 modulo n. S2 is Fermat's little theorem: for prime p and p not dividing a, a^(p-1) is congruent to 1 modulo p. Fermat's statement is also the prime-modulus special case of Euler's theorem because phi(p)=p-1. Both statements are therefore correct.

## Key Points

- Euler: a^phi(n) = 1 mod n for gcd(a,n)=1; Fermat: phi(p)=p-1 when p is prime.

## Why the other options are incorrect

Options 1 and 2 omit one valid theorem. Option 4 rejects both. The coprimality conditions are essential: Euler's result is not asserted for arbitrary a sharing a factor with n.
