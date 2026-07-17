# Question 106

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Structures · AVL*

Which of the following rotations are correctly explained in the context of an AVL tree. A. LL rotation: The new node is inserted in the left sub-tree of the left sub-tree of the critical node. B. RR rotation: The new node is inserted in the right sub-tree of the right sub-tree of the critical node. C. LR rotation: The new node is inserted in the right sub-tree of the left sub-tree of the critical node. D. RL rotation: The new node is inserted in the left sub-tree of the right sub-tree of the critical node Choose the correct answer from the options given below:

- **1.** A, D only
- **2.** A, C Only
- **3.** A, B Only
- **4.** B, C Only

> [!TIP]
> **Correct answer: No listed option — A, B, C, and D all correctly describe the four AVL imbalance cases**

## Solution

LL is insertion in left-of-left; RR right-of-right; LR right-of-left; RL left-of-right. These are precisely the four standard positional cases. Every statement is correct, but each option lists only two.

## Key Points

- Outer cases LL/RR need one rotation; inner cases LR/RL need two.

## Why the other options are incorrect

All offered subsets omit two correct case descriptions.
