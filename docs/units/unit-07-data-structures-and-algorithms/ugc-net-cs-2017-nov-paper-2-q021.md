# Question 21

*UGC NET CS · 2017 Nov Paper 2 · Data Structures · Array Representation of a Binary Heap*

Consider an array representation of an n element binary heap where the elements are stored from index 1 to index n of the array. For the element stored at index i of the array (i<=n), the index of the parent is :

- **1.** floor ((i+1)/2)
- **2.** ceiling ((i+1)/2)
- **3.** floor (i/2)
- **4.** ceiling (i/2)

> [!TIP]
> **Correct answer: 3. floor (i/2)**

## Solution

In a 1-indexed binary heap, the children of node i are stored at 2i and 2i+1. Reversing that relationship, both children have parent at floor(i/2): for even i=2p the parent is p, and for odd i=2p+1 the parent is again p. Hence option 3 is correct for every non-root element.

## Key Points

- One-indexed heap: parent(i)=⌊i/2⌋, left(i)=2i, right(i)=2i+1.

## Why the other options are incorrect

The formulas involving i+1 give the wrong parent for even indices. `ceil(i/2)` is wrong for odd right children: for i=5 it gives 3, but index 5 is a child of index 2. The root at i=1 has no parent, so the formula is applied for i>1.
