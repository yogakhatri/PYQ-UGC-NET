# Question 25

*UGC NET CS · 2017 Nov Paper 2 · Data Structures · Binary Search Tree Traversal*

Postorder traversal of a given binary search tree T produces following sequence of keys : 3, 5, 7, 9, 4, 17, 16, 20, 18, 15, 14 Which one of the following sequences of keys can be the result of an in-order traversal of the tree T ?

- **1.** 3, 4, 5, 7, 9, 14, 20, 18, 17, 16, 15
- **2.** 20, 18, 17, 16, 15, 14, 3, 4, 5, 7, 9
- **3.** 20, 18, 17, 16, 15, 14, 9, 7, 5, 4, 3
- **4.** 3, 4, 5, 7, 9, 14, 15, 16, 17, 18, 20

> [!TIP]
> **Correct answer: 4. 3, 4, 5, 7, 9, 14, 15, 16, 17, 18, 20**

## Solution

For a binary search tree with distinct keys, an inorder traversal always visits keys in ascending order: all keys in the left subtree, then the root, then all keys in the right subtree. Sorting the keys appearing in the postorder list gives 3,4,5,7,9,14,15,16,17,18,20. This is exactly option 4.

## Key Points

- Inorder traversal of a BST with distinct keys yields the keys in sorted order.

## Why the other options are incorrect

Options 1–3 are not globally increasing, so none can be the inorder traversal of this BST. The supplied postorder is useful for reconstructing shape, but reconstruction is unnecessary when the question asks only for BST inorder order.
