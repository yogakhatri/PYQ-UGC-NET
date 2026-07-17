# Question 65

*UGC NET CS · 2017 Jan Paper 3 · Error Detection and Correction · Hamming Sphere-Packing Bound for q-ary Codes*

A t-error-correcting q-ary linear code satisfies M·Σ_(i=0)^t C(n,i)(q−1)^i ≤ X, where M is the number of codewords. What is X?

- **1.** q^n
- **2.** q^t
- **3.** q^(−n)
- **4.** q^(−t)

> [!TIP]
> **Correct answer: 1. q^n**

## Solution

A q-ary length-n word has q^n possible values. Around one codeword, the number of words within Hamming distance t is Σ from i=0 to t of C(n,i)(q−1)^i: choose i error positions and one of q−1 changed symbols at each. For t-error correction, the M radius-t spheres must be disjoint and fit inside the q^n-word space. Thus M·Σ C(n,i)(q−1)^i≤q^n, so X=q^n and option 1 is correct.

## Key Points

- Hamming bound = number of codewords × volume of one radius-t Hamming ball ≤ total q^n words.

## Why the other options are incorrect

q^t counts neither the whole ambient word space nor a Hamming ball, while negative powers are fractions and cannot represent the number of length-n q-ary words.
