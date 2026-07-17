# Question 63

*UGC NET CS · 2018 July Paper 2 · Database Models · Hierarchical Database Root Access*

In a hierarchical database, a hashing function is used to locate the ________.

- **1.** Collision
- **2.** Root
- **3.** Foreign Key
- **4.** Records

> [!TIP]
> **Correct answer: 2. Root**

## Solution

A hierarchical database is navigated as a tree. Its root segment is the entry point; once the appropriate root is found, parent-child links guide access to descendants. A hashing or randomizing function can map a root key directly to the root's storage location. Therefore option 2 is correct.

## Key Points

- Hierarchical access starts at a root; hashing provides direct access to that root, followed by pointer traversal.

## Why the other options are incorrect

A collision is a side effect to be resolved, not the target being located. Foreign keys are a relational-model mechanism. Hashing can locate records in general file organizations, but in this hierarchical-database question its special role is to locate the root from which navigation begins.
