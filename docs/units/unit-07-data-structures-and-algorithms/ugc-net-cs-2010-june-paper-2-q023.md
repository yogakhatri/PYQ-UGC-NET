# Question 23

*UGC NET CS · 2010 June Paper 2 · Data Structures · Threaded Binary*

In a complete binary tree of n nodes, how far are the two most distant nodes ? Assume each edge in the path counts as !

- **A.** About log 2n
- **B.** About 2 log 2n
- **C.** About n log 2n
- **D.** About 2n

> [!TIP]
> **Correct answer: B. About 2 log 2n**

## Solution

A complete binary tree with n nodes has height h=⌊log₂n⌋. The longest path can run from a deepest leaf through the root to a deepest leaf in the opposite subtree, using about 2h edges. Hence the diameter is about 2log₂n.

## Key Points

- Tree diameter is at most twice its height and is nearly that value for a complete tree.

## Why the other options are incorrect

log₂n estimates root-to-leaf height, only half the possible leaf-to-leaf route. The alternatives involving n are far too large for a logarithmic-height tree.
