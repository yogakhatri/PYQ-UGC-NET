# Question 2

*UGC NET CS · 2012 June Paper 2 · Data Structures · Binary-Tree Traversal Reconstruction*

The post order traversal of a binary tree is DEBFCA. Find out the pre- order traversal.

- **A.** ABFCDE
- **B.** ADBFEC
- **C.** ABDECF
- **D.** None of the above

> [!TIP]
> **Correct answer: D. None of the above**

## Solution

Postorder gives left subtree, right subtree, then root, so DEBFCA tells us only that A is the root. It does not reveal where the left subtree ends or whether a one-child node uses its left or right link. Many different trees share this postorder and have different preorders. For example, a left-skewed chain A-C-F-B-E-D has postorder DEBFCA but preorder ACFBED. Therefore the preorder is not uniquely determined from the supplied information, and none of A-C can be asserted as the answer.

## Key Points

- One traversal alone generally does not determine a binary tree; postorder identifies the root but not the subtree split.

## Why the other options are incorrect

Option C, ABDECF, is one possible preorder for a full tree whose left subtree is B(D,E) and right subtree is C(F), but fullness or that shape is not stated. Options A and B are also unsupported. A unique reconstruction normally needs inorder plus preorder/postorder, or an explicit full-tree assumption.

## Additional Information

This item is under-specified. If an unstated assumption of a particular full binary-tree shape is imposed, option C is possible; without it, D is the logically valid choice.
