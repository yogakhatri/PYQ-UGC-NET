# Question 24

*UGC NET CS · 2016 July Paper 3 · Regular Language Models · GCD Language and Unary Kleene Closure*

Consider the following two languages : L1 = {0i1j| gcd (i, j) = 1} L2 is any subset of 0*. Which of the following is correct ?

- **1.** L1 is regular and L*2 is not regular
- **2.** L1 is not regular and L*2 is regular
- **3.** Both L1 and L*2 are regular languages
- **4.** Both L1 and L*2 are not regular languages

> [!TIP]
> **Correct answer: 2. L1 is not regular and L*2 is regular**

## Solution

L₁ is not regular. For distinct primes p and q, prefixes 0ᵖ and 0ᑫ are distinguishable by suffix 1ᵖ: gcd(p,p)>1, but gcd(q,p)=1. Infinitely many primes therefore give infinitely many Myhill-Nerode classes. For any L₂⊆0*, the lengths occurring in L₂* form an additive submonoid of the nonnegative integers; such a unary length set is finitely generated/eventually periodic and hence regular. Thus L₁ is nonregular while L₂* is regular.

## Key Points

- Coprimality yields infinitely many distinguishable prime-based prefixes; the Kleene closure of any unary language is regular.

## Why the other options are incorrect

Options 1 and 3 incorrectly classify the gcd language as regular. Option 4 overlooks the special effect of Kleene closure on a unary language: although an arbitrary subset of 0* need not be regular, its star has an eventually periodic set of lengths.
