# Question 28

*UGC NET CS · 2018 July Paper 2 · Sorting Algorithms · Radix Sort and Bucket Processing*

The maximum number of comparisons needed to sort 9 items using radix sort is (assume each item is 5 digit octal number) :

- **1.** 45
- **2.** 72
- **3.** 360
- **4.** 450

> [!TIP]
> **Correct answer: No standards-correct option: ordinary radix sort uses zero key-to-key comparisons; option 3 (360) assumes a nonstandard sequential search through eight buckets.**

## Solution

Radix sort is a non-comparison sorting method. For each of five octal digit positions, it reads each of the nine digits and directly indexes one of eight buckets, so it performs 5×9=45 digit-distribution operations plus bucket bookkeeping—but no comparisons between keys. None of the offered numbers expresses the correct key-comparison count of zero. The commonly intended answer 360 comes from 9×5×8, assuming each digit is compared sequentially against all eight bucket labels, an unnecessary implementation.

## Key Points

- Radix sort escapes comparison-sorting bounds by classifying digits into directly addressed buckets; distinguish item visits from key comparisons.

## Why the other options are incorrect

45 is a plausible count of item-digit visits, not comparisons; 72 is one pass of nine items times eight bucket tests; 360 repeats that naive bucket scan for five digits; 450 has no standard radix-sort basis. Direct bucket indexing avoids all eight-way searching.

## References

- [UC Berkeley CS61B — Beyond Comparisons: Radix Sort](https://www-inst.eecs.berkeley.edu/~cs61b/fa15/demos/radix-sort-demo.html)
