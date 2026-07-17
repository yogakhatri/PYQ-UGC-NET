# Question 10

*UGC NET CS · 2011 Dec Paper 3 · Data Structures · Binary-Tree Structural Similarity*

Two binary trees are similar if they are either empty or both non-empty and have similar left and right sub trees. Write a function in C++ to dec ide whether two binary trees are similar. What is the running time of your function ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Recursively compare emptiness and corresponding subtree shape; worst-case time O(n) and stack space O(h)**

## Solution

Similarity here concerns shape, not stored values. A direct C++ implementation is:

~~~cpp
bool similar(const Node* a, const Node* b) {
    if (a == nullptr || b == nullptr)
        return a == b;              // both null is true; exactly one null is false
    return similar(a->left, b->left) &&
           similar(a->right, b->right);
}
~~~

The base case handles both empty trees and structural mismatch. If both roots exist, their left subtrees must be similar and their right subtrees must be similar. Structural induction proves correctness: the function implements exactly the recursive definition in the question.

It visits each corresponding pair until a mismatch is found. For two similar n-node trees the time is Theta(n); in the general worst case it is O(min(n1,n2)) before an absent node exposes a mismatch. Recursive auxiliary space is O(h), where h is tree height—O(log n) for a balanced tree and O(n) for a skew tree.

## Key Points

- Mirror the recursive definition in code: both absent, exactly one absent, or recursively compare corresponding children.

## Common mistakes to avoid

Comparing node values answers tree equality, not structural similarity. Comparing only node counts is insufficient because different shapes can have the same count. Omitting the one-null/one-nonnull case can dereference a null pointer or incorrectly accept a mismatch.
