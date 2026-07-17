# Question 92

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Structures · Trees and Forests*

S. ND82042 Consider the following statements: A. The number of labelled binary trees possible with 'n' nodes is (2n)!/(n+1)! B. The number of binary search trees possible with 'n' nodes is (2n)!/((n+1)!n!) C. The number of unlabeled binary trees possible with 'n' nodes is C(2n,n)/(n+ 1)! D. The number of simple, undirected and labelled graphs possible with 'n' vertices is 2n(n-1)/2 Choose the correct answer from the options given below:

- **1.** A, B and Care only correct
- **2.** A, B and Dare only correct
- **3.** B, C and Dare only correct
- **4.** A, C and Dare only correct

> [!TIP]
> **Correct answer: 2. A, B and Dare only correct**

## Solution

Ordered binary-tree shapes and BSTs are counted by Catalan C_n=(2n)!/((n+1)!n!). Labeling every node multiplies by n!, giving (2n)!/(n+1)! for A. Thus A and B are true. C's extra factorial is wrong. A simple labeled graph independently chooses any of C(n,2) edges, giving 2^[n(n−1)/2], so D is true.

## Key Points

- Catalan counts binary-tree shapes/BSTs; arbitrary simple graphs count edge subsets.

## Why the other options are incorrect

Choices containing C use an incorrect unlabeled-tree formula or omit one of A,B,D.
