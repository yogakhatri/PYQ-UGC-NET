# Question 50

*UGC NET CS · 2012 June Paper 2 · Data Structures · Trees and Hierarchical Relationships*

To represent hierarchical relationship between elements, which data structure is suitable ?

- **A.** Dequeue
- **B.** Priority
- **C.** Tree
- **D.** All of the above www.solutionsadda.in

> [!TIP]
> **Correct answer: C. Tree**

## Solution

A tree represents hierarchy directly: one root has children, those children have descendants, and every non-root node has a parent in the basic tree model. File directories, organization charts and syntax structures are common examples.

## Key Points

- Use a tree when relationships are naturally parent-child and multi-level.

## Why the other options are incorrect

A deque is a linear sequence allowing insertion/removal at both ends. A priority queue orders access by priority but does not represent parent-child hierarchy. Therefore 'all' is false.
