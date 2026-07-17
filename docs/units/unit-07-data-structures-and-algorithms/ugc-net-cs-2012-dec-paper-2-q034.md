# Question 34

*UGC NET CS · 2012 Dec Paper 2 · Data Structures · Maximum Keys in B-Trees*

The maximum number of keys stored in a B-tree of order m and depth d is:

- **1.** m^(d+1)-1
- **2.** [m^(d+1)-1]/(m-1)
- **3.** (m-1)[m^(d+1)-1]
- **4.** [m^d-1]/(m-1)

> [!TIP]
> **Correct answer: 1. m^(d+1)-1**

## Solution

For a B-tree of order m, each node has at most m children and therefore at most m-1 keys. If the root is at depth 0 and leaves are at depth d, the maximum number of nodes is 1+m+m^2+...+m^d=(m^(d+1)-1)/(m-1). Multiplying by m-1 keys per node gives m^(d+1)-1 maximum keys.

## Key Points

- Maximum B-tree keys equal the maximum node count times (m-1): ((m^(d+1)-1)/(m-1)) times (m-1) = m^(d+1)-1.

## Why the other options are incorrect

Option 2 counts the maximum number of nodes, not keys. Option 3 multiplies by m-1 without first dividing the geometric-series sum and is too large. Option 4 is a truncated geometric expression and does not count all levels through depth d.
