# Question 145

*UGC NET CS · 2019 June Paper 1 And 2 · Fuzzy Sets · Alpha Cuts*

Let A_alpha0 denote the alpha-cut of a fuzzy set A at alpha0. If alpha1 < alpha2, then:

- **1.** A_alpha1 is a superset of or equal to A_alpha2
- **2.** A_alpha1 is a proper superset of A_alpha2
- **3.** A_alpha1 is a subset of or equal to A_alpha2
- **4.** A_alpha1 is a proper subset of A_alpha2

> [!TIP]
> **Correct answer: 1. A_alpha1 is a superset of or equal to A_alpha2**

## Solution

An alpha-cut is A_alpha={x | mu_A(x)>=alpha}. If alpha1<alpha2, every element meeting the stricter requirement mu_A(x)>=alpha2 automatically meets mu_A(x)>=alpha1. Hence A_alpha2 is contained in A_alpha1, or equivalently A_alpha1 is a superset of or equal to A_alpha2.

## Key Points

- As alpha increases, an alpha-cut can only shrink; it need not shrink strictly.

## Why the other options are incorrect

The containment direction in options 3 and 4 is reversed. Option 2 requires a proper superset, but the cuts can be equal when no membership value lies between alpha1 and alpha2.
