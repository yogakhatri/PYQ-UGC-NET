# Question 40

*UGC NET CS · 2013 June Paper 3 · Language Closure Properties · Context-Sensitive and Context-Free Closure*

The statements s1 and s2 are given as : s1 : Context sensitive languages are closed under intersection, concatenation, substitution and inverse homomorphism. s2 : Context free languages are closed under complementation, substitution and homomorphism. Which of the following is correct statement ?

- **A.** Both s1 and s2 are correct.
- **B.** s1 is correct and s2 is not correct.
- **C.** s1 is not correct and s2 is correct.
- **D.** Both s1 and s2 are not correct.

> [!TIP]
> **Correct answer: B. s1 is correct and s2 is not correct.**

## Solution

Under the standard noncontracting conventions used for context-sensitive languages, they are closed under intersection, concatenation, substitution and inverse homomorphism, so s1 is true. Context-free languages are closed under substitution and homomorphism, but not under complementation. If CFLs were closed under complement, De Morgan's law together with closure under union would also make them closed under intersection, which they are not. Therefore s2 is false.

## Key Points

- CFLs survive homomorphism and substitution, but complement is the decisive nonclosure in s2.

## Why the other options are incorrect

A incorrectly accepts the CFL complementation claim. C and D reject s1 even though the listed context-sensitive closure properties hold under the standard convention. Only B records s1 true and s2 false.
