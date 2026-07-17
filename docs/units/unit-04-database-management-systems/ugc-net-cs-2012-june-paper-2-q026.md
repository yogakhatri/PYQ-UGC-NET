# Question 26

*UGC NET CS · 2012 June Paper 2 · Database Indexing · B+ Tree Degree from Block Size*

A / B + tree index is to be built on the name attribute of the relation STUDENT. Assume that all students names are of length 8 bytes, disk block are of size 512 bytes and index pointers are of size 4 bytes. Given this scenario what would be the best choice of the degree (i.e. the number of pointers per node) of the B + tree ?

- **A.** 16
- **B.** 42
- **C.** 43
- **D.** 44 www.solutionsadda.in

> [!TIP]
> **Correct answer: C. 43**

## Solution

If an internal B+ tree node has p child pointers, it has p-1 search keys. Each pointer uses 4 bytes and each name key uses 8 bytes, so node size is 4p+8(p-1)=12p-8. It must fit in 512 bytes: 12p-8<=512, hence 12p<=520 and p<=43.33. The largest integer degree is therefore 43.

## Key Points

- For p pointers and p-1 keys, solve p(pointer size)+(p-1)(key size)<=block size.

## Why the other options are incorrect

16 and 42 fit but waste usable fan-out and produce a taller index than necessary. Degree 44 needs 4(44)+8(43)=520 bytes and does not fit in a 512-byte block.
