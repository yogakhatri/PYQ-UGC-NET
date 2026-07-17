# Question 29

*UGC NET CS · 2016 July Paper 2 · Network Security · Pairwise Symmetric-Key Count*

If there are N people in the world and are using secret key encryption/decryption for privacy purpose, then number of secret keys required will be :

- **1.** N
- **2.** N − 1
- **3.** N(N − 1)/2
- **4.** N(N + 1)/2

> [!TIP]
> **Correct answer: 3. N(N − 1)/2**

## Solution

In pairwise secret-key encryption, every unordered pair of people needs one key known only to that pair. The number of pairs among N people is C(N,2)=N(N−1)/2, so option 3 is correct.

## Key Points

- Symmetric pairwise keys scale quadratically: one shared key per unordered user pair.

## Why the other options are incorrect

N or N−1 keys cannot give a different private shared secret to every pair in a general population. N(N+1)/2 incorrectly includes N self-pairs; a person does not require a pairwise communication key with themself.
