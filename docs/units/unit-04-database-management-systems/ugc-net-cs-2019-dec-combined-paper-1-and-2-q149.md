# Question 149

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Database Design · Functional Dependencies, Keys and Normalization*

Identify the redundant functional dependency in F.

- **1.** BC→D
- **2.** D→E
- **3.** A → D
- **4.** A → BC

> [!TIP]
> **Correct answer: 3. A → D**

## Solution

Test A→D after temporarily removing it. Starting with A, dependency A→BC supplies B and C; then BC→D supplies D. Therefore D is already in A+ under the other dependencies, which proves that A→D is implied by them and is redundant. The remaining dependencies are needed to obtain B and C from A, D from BC, and E from D. Hence option 3.

## Key Points

- An FD X→Y is redundant exactly when Y⊆X+ computed using all the other dependencies.

## Why the other options are incorrect

Without BC→D, the remaining set cannot derive D from BC. Without D→E, no dependency supplies E. Without A→BC, A cannot derive B or C. Only A→D can be reconstructed transitively as A→BC and BC→D.
