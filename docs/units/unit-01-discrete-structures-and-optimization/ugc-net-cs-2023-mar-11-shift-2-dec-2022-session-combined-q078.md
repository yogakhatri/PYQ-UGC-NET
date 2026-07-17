# Question 78

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Graph Theory · Counting spanning trees*

BID:187021 Consider the Graph below: How many spanning trees can be found?

- **1.** 10
- **2.** 5
- **3.** 9
- **4.** 8

> [!TIP]
> **Correct answer: 4. 8**

## Solution

The pictured graph has four vertices and is K₄ with one edge missing. K₄ has 4^(4−2)=16 spanning trees by Cayley’s formula. By symmetry, each of K₄’s six edges occurs in the same number of spanning trees; because every tree has three edges, the total edge occurrences are 16×3=48, or 48/6=8 per edge. Removing one edge therefore removes 8 trees, leaving 16−8=8.

## Key Points

- Recognize a nearly complete graph and count by deleting the spanning trees that contain the missing edge.

## Why the other options are incorrect

The counts 10, 5, and 9 do not match either direct enumeration or the K₄ symmetry argument. Exactly half of K₄’s spanning trees use the deleted edge.
