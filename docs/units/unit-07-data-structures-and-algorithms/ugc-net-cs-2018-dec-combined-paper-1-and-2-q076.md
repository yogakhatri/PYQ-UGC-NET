# Question 76

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Structures · Leaf Count from Node Degrees*

In a ternary tree, the numbers of internal nodes of degree 1, 2 and 3 are 4, 3 and 3 respectively. How many leaf nodes are there?

- **1.** 9
- **2.** 10
- **3.** 11
- **4.** 12

> [!TIP]
> **Correct answer: 2. 10**

## Solution

There are I=4+3+3=10 internal nodes. Counting child edges from the internal nodes gives E=4·1+3·2+3·3=19. Any finite rooted tree with I internal nodes and L leaves has E=(I+L)−1. Thus 19=(10+L)−1, so L=10. Therefore option 2.

## Key Points

- Equate the sum of child counts with total vertices minus one; every non-root vertex has exactly one incoming parent edge.

## Why the other options are incorrect

The other values violate the tree edge identity. A useful equivalent shortcut is L=1+Σ internal(degree−1)=1+4(0)+3(1)+3(2)=10.
