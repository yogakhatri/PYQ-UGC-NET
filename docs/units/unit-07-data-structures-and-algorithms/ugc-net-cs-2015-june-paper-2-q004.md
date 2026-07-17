# Question 4

*UGC NET CS · 2015 June Paper 2 · Data Structures and Algorithms · Tree Traversals, Huffman Coding and Topological Order*

Which statements are true? (a) Depth-first search can traverse a rooted tree. (b) Preorder, postorder, and inorder list vertices of an ordered rooted tree. (c) Huffman's algorithm finds an optimal binary tree for given weights. (d) A conventional topological ordering labels parents larger than their children.

- **1.** (a) and (b)
- **2.** (c) and (d)
- **3.** (a), (b), and (c)
- **4.** (a), (b), (c), and (d)

> [!TIP]
> **Correct answer: 3. (a), (b), and (c)**

## Solution

Depth-first search is a standard rooted-tree traversal, so (a) is true. Preorder, postorder, and—in the intended ordered/binary-tree setting—inorder are traversal listings, so (b) is true. Huffman's greedy merging constructs a minimum-weighted-path-length binary code tree, making (c) true. In a conventional topological order, an edge parent→child places the parent earlier and therefore gives it a smaller position label, not a larger one; (d) is false. Thus (a),(b),(c) are true.

## Key Points

- Topological order respects edge direction: a predecessor/parent appears before its successor/child.

## Why the other options are incorrect

Option 1 omits the true Huffman statement. Option 2 includes the false topological-label claim and omits true traversal facts. Option 4 includes all four and therefore accepts (d). Option 3 contains exactly the true set.
