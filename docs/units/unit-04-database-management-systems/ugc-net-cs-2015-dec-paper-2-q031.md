# Question 31

*UGC NET CS · 2015 Dec Paper 2 · Data Warehousing · Maximum Cell Count in a Data Cube*

A data cube C, has n dimensions, and each dimension has exactly p distinct values in the base cuboid. Assume that there are no concept hierarchies associated with the dimensions. What is the maximum number of cells possible in the data cube, C ?

- **1.** p^n
- **2.** p
- **3.** (2^n − 1)p + 1
- **4.** (p + 1)^n

> [!TIP]
> **Correct answer: 4. (p + 1)^n**

## Solution

For each dimension, a cube cell may specify one of its p base values or the aggregate value ALL. Thus each dimension has p+1 possible coordinates in the complete cube. Independent choices across n dimensions give (p+1)^n cells. Equivalently, summing cells over all cuboids gives Σ from k=0 to n of C(n,k)p^k=(p+1)^n by the binomial theorem.

## Key Points

- Add one ALL value per dimension, then apply the product rule: (p+1)^n.

## Why the other options are incorrect

p^n counts only the base cuboid with no aggregation. p ignores all but one dimension. The third expression does not equal the sum of the 2^n cuboids' cell counts.
