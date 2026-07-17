# Question 37

*UGC NET CS · 2015 Dec Paper 2 · Data Structures · B-Tree Search I/O Complexity*

The number of disk pages access in B - tree search, where h is height, n is the number of keys, and t is the minimum degree, is :

- **1.** Θ(log_n(h·t))
- **2.** Θ(h·log_t n)
- **3.** Θ(log_h n)
- **4.** Θ(log_t n)

> [!TIP]
> **Correct answer: 4. Θ(log_t n)**

## Solution

A B-tree search follows one root-to-leaf path and accesses at most one node page per level, so its page-I/O count is Θ(h). With minimum degree t, the height of an n-key B-tree is Θ(log_t n). Substitution gives Θ(log_t n), option 4.

## Key Points

- One B-tree page per level; height grows logarithmically with base determined by fan-out.

## Why the other options are incorrect

Options 1 and 3 use inappropriate logarithm bases or variables. Option 2 multiplies by h even though log_t n already represents the height order, effectively counting the height twice.
