# Question 33

*UGC NET CS · 2016 July Paper 3 · Data Structures · Array Representation of a Binary Max-Heap*

Which one of the following array represents a binary max-heap ?

- **1.** [26, 13, 17, 14, 11, 9, 15]
- **2.** [26, 15, 14, 17, 11, 9, 13]
- **3.** [26, 15, 17, 14, 11, 9, 13]
- **4.** [26, 15, 13, 14, 11, 9, 17]

> [!TIP]
> **Correct answer: 3. [26, 15, 17, 14, 11, 9, 13]**

## Solution

A max-heap array must satisfy A[parent]≥A[child] at every occupied child index. In option 3, 26≥15,17; 15≥14,11; and 17≥9,13. Every parent dominates its children, so `[26,15,17,14,11,9,13]` is a max-heap.

## Key Points

- For a 1-based heap array, check A[i]≥A[2i] and A[i]≥A[2i+1] for every internal i.

## Why the other options are incorrect

Option 1 has parent 13 below child 14. Option 2 has parent 15 below child 17. Option 4 has parent 13 below child 17. A large root alone is insufficient; the property must hold at every internal node.
