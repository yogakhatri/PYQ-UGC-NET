# Question 35

*UGC NET CS · 2016 July Paper 3 · Data Structures · Valid Search Paths in a Binary Search Tree*

Suppose that we have numbers between 1 and 1,000 in a binary search tree and want to search for the number 364. Which of the following sequences could not be the sequence of nodes examined ?

- **1.** 925, 221, 912, 245, 899, 259, 363, 364
- **2.** 3, 400, 388, 220, 267, 383, 382, 279, 364
- **3.** 926, 203, 912, 241, 913, 246, 364
- **4.** 3, 253, 402, 399, 331, 345, 398, 364

> [!TIP]
> **Correct answer: 3. 926, 203, 912, 241, 913, 246, 364**

## Solution

Track the allowable interval for target 364. In option 3: 926 makes the upper bound 926; 203 makes the lower bound 203; 912 lowers the upper bound to 912; 241 raises the lower bound to 241. The next examined node is 913, but every node in that current subtree must be below 912. Thus 913 cannot occur, and sequence 3 is impossible.

## Key Points

- Validate a BST search path by maintaining an open (lower,upper) interval and tightening it after every comparison.

## Why the other options are incorrect

Each of sequences 1, 2, and 4 keeps every next key within the lower and upper bounds imposed by previous comparisons. Alternating left and right turns is valid as long as the accumulated interval is respected.
