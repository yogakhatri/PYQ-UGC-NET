# Question 24

*UGC NET CS · 2010 June Paper 2 · Selected Topics · Number-Theoretic Algorithms*

A chained hash table has an array size of 100. What is the maximum number of entries that can be placed in the table ?

- **A.** 100
- **B.** 200
- **C.** 10000
- **D.** There is no upper limit

> [!TIP]
> **Correct answer: D. There is no upper limit**

## Solution

Separate chaining stores colliding entries in an auxiliary chain at each array index. A bucket can therefore hold arbitrarily many entries, limited only by available memory rather than the 100 array slots. There is no fixed upper limit from table size alone.

## Key Points

- Chaining decouples entry count from the number of hash buckets.

## Why the other options are incorrect

100 is the bound for open addressing, not chaining. 200 and 10,000 have no basis without a separate memory/load-factor constraint.
