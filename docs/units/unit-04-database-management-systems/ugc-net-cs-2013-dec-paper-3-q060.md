# Question 60

*UGC NET CS · 2013 Dec Paper 3 · Relational Database Concepts · Indexes, Query Languages, Closure and Natural Join*

Match the following : List – I List – II a. Secondary Index i. Functional Dependency b. Non- procedural Query Language ii. B-Tree c. Closure of set of Attributes iii. Relational Algebraic Operation d. Natural JOIN iv. Domain Calculus Codes : a b c d

- **A.** i ii iv iii
- **B.** ii i iv iii
- **C.** i iii iv ii
- **D.** ii iv i iii

> [!TIP]
> **Correct answer: D. ii iv i iii**

## Solution

A secondary index is commonly implemented with a B-tree/B+ tree, so a→ii. Domain relational calculus is a declarative, nonprocedural query language, so b→iv. Attribute closure is computed from a set of functional dependencies, so c→i. Natural join is a relational-algebra operation, so d→iii. The resulting order is ii, iv, i, iii.

## Key Points

- Index→B-tree; declarative query→domain calculus; closure→functional dependencies; natural join→relational algebra.

## Why the other options are incorrect

A, B and C each mismatch one or more basic database concepts: functional dependency governs closure rather than the secondary index, domain calculus is the nonprocedural language, and natural join belongs to relational algebra.
