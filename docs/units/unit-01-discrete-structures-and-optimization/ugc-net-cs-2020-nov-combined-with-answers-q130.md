# Question 130

*UGC NET CS · 2020 Nov With Answers · Number Theory · Divisibility and Modular Arithmetic*

Statement I: 5 divides n^5-n whenever n is a nonnegative integer. Statement II: 6 divides n^3-n whenever n is a nonnegative integer. Choose the correct evaluation.

- **1.** Both Statement I and Statement II are correct
- **2.** Both Statement I and Statement Il are incorrect
- **3.** Statement I is correct but Statement Il is incorrect
- **4.** Statement I is incorrect but Statement II is correct

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement II are correct**

## Solution

For Statement I, Fermat's congruence gives n^5≡n (mod 5) for every integer n, including multiples of 5; hence 5 divides n^5−n. For Statement II, factor n^3−n=n(n−1)(n+1), the product of three consecutive integers. One factor is divisible by 3 and at least one is even, so the product is divisible by 2×3=6. Both statements are correct, giving option 1.

## Key Points

- Use modular residues for n^5−n and the three-consecutive-integers factorization for n^3−n.

## Why the other options are incorrect

Options 2–4 declare at least one true divisibility statement false. The factorization of n^3−n proves Statement II directly, and residues modulo 5—or Fermat's theorem—prove Statement I.
