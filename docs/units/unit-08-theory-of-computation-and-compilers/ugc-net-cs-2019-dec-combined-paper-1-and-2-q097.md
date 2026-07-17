# Question 97

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Language · Closure Properties of Context-Free Languages*

For L = {a^n b^n | n ≥ 0}, consider: S1: L^2 is context-free. S2: L^k is context-free for every fixed k ≥ 1. S3: the complement of L and L* are context-free. Which statement set is correct?

- **1.** Only S1 and S2
- **2.** Only S1 and S3
- **3.** Only S2 and S3
- **4.** S1, S2 and S3

> [!TIP]
> **Correct answer: 4. S1, S2 and S3**

## Solution

Context-free languages are closed under concatenation and Kleene star. Therefore L²=LL is context-free, and repeated finite concatenation makes L^k context-free for every fixed k≥1; L* is context-free as well. Although CFLs are not closed under complement in general, this particular complement is context-free: strings outside a*b* form a regular set, while strings a^i b^j with i≠j split into the CFL cases i<j and i>j. Hence S1, S2, and S3 are all true, giving option 4.

## Key Points

- Separate a class-wide closure claim from a claim about one specific language; a particular CFL may have a context-free complement.

## Why the other options are incorrect

Options 1–3 each omit one true statement. The common trap is to use the non-closure of arbitrary CFLs under complement to reject S3; closure facts do not say that the complement of every individual nonregular CFL is non-context-free.
