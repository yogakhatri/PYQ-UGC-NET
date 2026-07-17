# Question 2

*UGC NET CS · 2012 Dec Paper 2 · Data Structures · AVL Worst-Case Complexity*

The worst-case time complexity of an AVL tree is better in comparison to a binary search tree for:

- **1.** Search and insert operations
- **2.** Search and delete operations
- **3.** Insert and delete operations
- **4.** Search, insert and delete operations

> [!TIP]
> **Correct answer: 4. Search, insert and delete operations**

## Solution

An AVL tree maintains a balance factor of -1, 0 or +1 at every node, so its height is O(log n). Search follows a root-to-leaf path, while insertion and deletion first follow such a path and then perform only a bounded amount of rebalancing work per visited level. Their worst-case times are therefore O(log n). An ordinary binary search tree can become a chain of height n, making all three operations O(n) in the worst case.

## Key Points

- AVL height is O(log n); an unbalanced BST can have height O(n).
- Since the three basic operations depend on tree height, AVL improves all three worst-case bounds.

## Why the other options are incorrect

Options 1, 2 and 3 each omit one operation that also receives the same worst-case improvement. AVL balancing benefits search, insertion and deletion, so the complete choice is option 4.
