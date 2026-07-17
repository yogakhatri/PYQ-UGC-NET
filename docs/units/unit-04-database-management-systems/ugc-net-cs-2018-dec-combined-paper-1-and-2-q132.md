# Question 132

*UGC NET CS · 2018 Dec Paper 1 And 2 · Normalization for Relational Databases · Candidate Keys from Functional Dependencies*

For relation R=(A,B,C,D,E,F), the functional dependencies are A->B, BC->D, E->C and D->A. What are the candidate keys?

- **1.** AE and BE
- **2.** AE, BE and DE
- **3.** AEF, BEF and BCF
- **4.** AEF, BEF and DEF

> [!TIP]
> **Correct answer: 4. AEF, BEF and DEF**

## Solution

E and F never appear on the right-hand side of any dependency, so neither can be derived; every candidate key must contain both. Now test minimal additions. (AEF)+ gives B from A→B, C from E→C, and D from BC→D, hence all attributes. (BEF)+ gives C, then D from BC, then A from D→A. (DEF)+ gives A, then B, and C from E. Each is minimal because removing E or F loses an underivable attribute, and removing the third attribute prevents the remaining closure from reaching all of A,B,D. Therefore the candidate keys are AEF, BEF, and DEF, option 4.

## Key Points

- Start candidate-key search with every attribute absent from all FD right-hand sides; those attributes must occur in every key.

## Why the other options are incorrect

Options 1 and 2 omit F, which no dependency can derive, so their sets cannot be superkeys. Option 3 includes BCF, but it omits E; since E never appears on a dependency's right side, BCF cannot determine E and is not a key.
