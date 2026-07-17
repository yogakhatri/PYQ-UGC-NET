# Question 59

*UGC NET CS · 2013 Dec Paper 3 · Normalization for Relational Databases · Derived Functional-Dependency Rules*

Armstrong (1974) proposed systematic approach to derive functional dependencies. Match the following w.r.t. functional dependencies : List – I List – II a. Decom- position rule i. If X → Y and Z → W then {X, Z} → {Y, W} b. Union rule ii. If X → Y and {Y, W}→ Z then {X, W} → Z c. Com- position rule iii. If X → Y and X → Z then X → {Y, Z} d. Pseudo transitivity rule iv. If X → {Y, Z} then X → Y and X → Z Codes : a b c d

- **A.** iii ii iv i
- **B.** i iii iv ii
- **C.** ii i iii iv
- **D.** iv iii i ii

> [!TIP]
> **Correct answer: D. iv iii i ii**

## Solution

Decomposition splits a combined right side: X→YZ implies X→Y and X→Z, so a→iv. Union combines dependencies with the same determinant: X→Y and X→Z imply X→YZ, so b→iii. Composition combines two dependencies: X→Y and Z→W imply XZ→YW, so c→i. Pseudo-transitivity says X→Y and YW→Z imply XW→Z, so d→ii. The order is iv, iii, i, ii.

## Key Points

- Recognize FD rules by shape: union joins right sides, decomposition splits them, composition joins two dependencies, and pseudo-transitivity carries an added W.

## Why the other options are incorrect

A, B and C attach at least one rule name to the wrong symbolic pattern. In particular, union and decomposition are converse-looking operations, while composition and pseudo-transitivity have different left-side constructions.
