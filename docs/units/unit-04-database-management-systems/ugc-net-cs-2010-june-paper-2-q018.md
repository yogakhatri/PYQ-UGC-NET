# Question 18

*UGC NET CS · 2010 June Paper 2 · Normalization for Relational Databases · Second normal form*

Match the following : I. 2 NF

- **A.** transitive dependencies eliminated II. 3 NF
- **B.** multivalued attribute removed III. 4 NF
- **C.** contain no partial functional dependencies IV. 5 NF
- **D.** contains no join dependency Codes : I II III IV (A) (a) (c) (b) (d) (B) (d) (a) (b) (c) (C) (c) (d) (a) (b) (D) (d) (b) (a) (c)

> [!TIP]
> **Correct answer: A. transitive dependencies eliminated II. 3 NF**

## Solution

2NF contains no partial dependency (I-c); 3NF eliminates transitive dependencies of non-key attributes (II-a); 4NF removes problematic nontrivial multivalued dependencies (III-b); and 5NF removes nontrivial join dependencies not implied by keys (IV-d). Thus c,a,b,d, printed as option A.

## Key Points

- 2NF partial, 3NF transitive, 4NF multivalued, 5NF join dependencies.

## Why the other options are incorrect

The other orders attach multivalued/join dependencies or partial/transitive dependencies to the wrong normalization levels.
