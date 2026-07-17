# Question 75

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Graph Theory · Enumeration of labelled trees*

SEND: 137025 How many different trees are possible with 'n' nodes?

- **1.** 0 1
- **2.** 2º-1
- **3.** 2°
- **4.** 20 - n

> [!TIP]
> **Correct answer: 1. 0 1**

## Solution

Cayley’s formula gives n^(n−2) unrooted labeled trees on n labeled vertices. Choosing a root for each such tree gives n choices, so the number of rooted labeled trees is n·n^(n−2)=n^(n−1). The option set is therefore referring to rooted labeled trees, and option 1 is the matching count.

## Key Points

- Cayley: unrooted labeled trees n^(n−2); rooted labeled trees n^(n−1).

## Why the other options are incorrect

The expressions involving powers of 2 count binary choices of edges without enforcing the connected-and-acyclic conditions required of a tree. They therefore include many non-trees and omit the labeled-tree counting structure.
