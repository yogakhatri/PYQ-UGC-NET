# Question 8

*UGC NET CS · 2011 Dec Paper 3 · Data Structures · B-Tree and B+ Tree Priority Queues*

Show how a B – tree and B + tree can be used to implement a priority queue. Also show that any sequence of n insertion and minimum deletion can be perfor med in o(nlogn) steps. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Store entries by priority; insertion and delete-min take O(log_B n) node accesses, so n operations take O(n log_B n), hence O(n log n)**

## Solution

Use the priority as the search key and attach each item to that key. In a B-tree, items may appear in internal and leaf nodes. Insert follows one root-to-leaf search path, splits full nodes and preserves balance. The minimum is the leftmost key; keep a pointer to its node if O(1) find-min is desired. Delete-min removes that key and repairs underflow by borrowing from a sibling or merging while moving toward the root.

In a B+ tree, internal nodes contain separator keys and all records are at the leaves. Leaves are linked, so the first entry of the leftmost leaf is the minimum. Insert into the proper leaf and split as needed; delete the first leaf entry and borrow/merge on underflow, updating separators and the leftmost-leaf pointer.

With fan-out B, height is O(log_B n). Insert and delete-min each touch O(log_B n) nodes, so any sequence of n such operations costs O(n log_B n) node accesses, which is O(n log n) for fixed B and substantially fewer disk I/Os when B is large. If the paper's lowercase o(n log n) is meant as little-o rather than an OCR/typographic Big-O, that stronger claim is not guaranteed for fixed fan-out; the standard bound is Big-O/Theta in the worst case.

## Key Points

- Balanced multiway search trees implement ordered priority queues; their height controls insertion and delete-min cost.

## Common mistakes to avoid

A B+ tree's minimum is not at the root; it is at the leftmost leaf. Deleting without borrow/merge can violate minimum occupancy. Claiming little-o for fixed fan-out confuses asymptotic notation with the ordinary O(n log n) bound.
