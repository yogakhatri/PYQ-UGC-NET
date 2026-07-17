# Question 19

*UGC NET CS · 2017 Jan Paper 2 · Relational Database Design · Binary Lossless-Join Decomposition Test*

Consider a schema R(MNPQ) and functional dependencies M → N, P → Q. Then the decomposition of R into R1(MN) and R2(PQ) is ________.

- **1.** Dependency preserving but not lossless join
- **2.** Dependency preserving and lossless join
- **3.** Lossless join but not dependency preserving
- **4.** Neither dependency preserving nor lossless join.

> [!TIP]
> **Correct answer: 1. Dependency preserving but not lossless join**

## Solution

The decomposition preserves dependencies because M→N can be enforced entirely in R₁(MN), while P→Q can be enforced entirely in R₂(PQ). For a binary decomposition to be lossless, the common attributes must functionally determine all attributes of at least one component. Here R₁∩R₂=∅, so that condition fails. Joining arbitrary R₁ and R₂ instances forms a Cartesian product and can create combinations of MN with PQ that were not together in the original R. Hence the decomposition is dependency preserving but not lossless, option 1.

## Key Points

- Binary lossless test: (R₁∩R₂)→R₁ or (R₁∩R₂)→R₂ must follow from F⁺.

## Why the other options are incorrect

Options 2 and 3 incorrectly claim losslessness despite the empty intersection. Option 4 incorrectly denies dependency preservation even though each given functional dependency is contained in one projected schema.
