# Question 53

*UGC NET CS · 2016 July Paper 3 · Multiprocessors and Multicomputers · Mesh Interconnection Networks*

A multicomputer with 256 CPUs is organized as 16 × 16 grid. What is the worst case delay (in hops) that a message might have to take ?

- **1.** 16
- **2.** 15
- **3.** 32
- **4.** 30

> [!TIP]
> **Correct answer: 4. 30**

## Solution

In a 16 × 16 two-dimensional mesh, the longest shortest path is between opposite corner processors. Moving from row 0 to row 15 takes 15 vertical hops, and moving from column 0 to column 15 takes 15 horizontal hops. The worst-case distance is therefore 15 + 15 = 30 hops, which is option 4.

## Key Points

- The diameter of an r × c mesh is (r − 1) + (c − 1).

## Why the other options are incorrect

Sixteen counts processors along one dimension, not links between the two extreme processors; 16 processors have only 15 intervening links. Values 15 and 16 account for at most one dimension, while 32 incorrectly uses 16 hops in each dimension.
