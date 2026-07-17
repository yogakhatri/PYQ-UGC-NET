# Question 22

*UGC NET CS · 2015 June Paper 2 · Trees · Reconstructing a Binary Tree from Traversals*

The inorder and preorder Traversal of binary Tree are dbeafcg and abdecfg respectively. The post-order Traversal is __________.

- **1.** dbefacg
- **2.** debfagc
- **3.** dbefcga
- **4.** debfgca

> [!TIP]
> **Correct answer: 4. debfgca**

## Solution

Preorder begins with the root, so `a` is the root. In inorder `dbe | a | fcg`, the left subtree contains `dbe` and the right subtree contains `fcg`. The corresponding preorder pieces are `bde` and `cfg`. Thus the left subtree is root `b` with children `d` and `e`, giving postorder `deb`; the right subtree is root `c` with children `f` and `g`, giving `fgc`. Postorder visits left subtree, right subtree, then root: `deb + fgc + a = debfgca`.

## Key Points

- Use preorder's first symbol as root, split inorder around it, reconstruct both subtrees, then output left-right-root.

## Why the other options are incorrect

The other strings do not obey the left-right-root rule after reconstructing the unique tree. In particular, the root `a` must appear last in a postorder traversal, immediately eliminating options 1 and 2; option 3 orders the left subtree incorrectly.
