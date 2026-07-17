# Question 67

*UGC NET CS · 2015 June Paper 3 · Optimization · Hungarian Assignment Method Optimality Test*

In the Hungarian method for solving assignment problem, an optimal assignment requires that the maximum number of lines that can be drawn through squares with zero opportunity cost be equal to the number of :

- **1.** rows or columns
- **2.** rows + columns
- **3.** rows + columns − 1
- **4.** rows + columns + 1

> [!TIP]
> **Correct answer: 1. rows or columns**

## Solution

In an n×n assignment matrix, the Hungarian optimality test is satisfied when the minimum number of horizontal and vertical lines needed to cover every zero is n—the order of the matrix, equal to the number of rows or the number of columns. At that point n independent zeros can support a complete assignment. Thus option 1 is intended.

## Key Points

- Hungarian test: minimum zero-covering lines = matrix order n, not rows+columns.

## Why the other options are incorrect

Rows plus columns and its ±1 variants are not the order of the assignment matrix. The printed stem incorrectly says `maximum number of lines`; any zero set could trivially be covered by many extra lines. The algorithm specifically uses the minimum covering-line count.
