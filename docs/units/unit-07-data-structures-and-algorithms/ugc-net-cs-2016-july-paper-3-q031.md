# Question 31

*UGC NET CS · 2016 July Paper 3 · Data Structures · Counting Binary-Tree Shapes with Catalan Numbers*

The number of different binary trees with 6 nodes is ______.

- **1.** 6
- **2.** 42
- **3.** 132
- **4.** 256

> [!TIP]
> **Correct answer: 3. 132**

## Solution

The number of structurally different ordered binary trees with n nodes is the Catalan number Cₙ=(1/(n+1))·C(2n,n). For n=6, C₆=(1/7)·C(12,6)=924/7=132. Therefore option 3 is correct.

## Key Points

- Ordered binary-tree shapes with n nodes are counted by Catalan Cₙ.

## Why the other options are incorrect

Six is only the node count, 42 is C₅, and 256 is not the sixth Catalan number. The question counts tree shapes, not label permutations; labeling the nodes would produce a different and much larger count.
