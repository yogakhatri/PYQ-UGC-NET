# Question 37

*UGC NET CS · 2015 Dec Paper 3 · Memory Management · Paging, Segmentation and Partitioning*

Match the following with respect to various memory management algorithms : List - I List - II (a) Demand paging (i) degree of multiprogramming (b) Segmentation (ii) working set (c) Dynamic partitions (iii) supports user view of memory (d) Fixed partitions (iv) compaction Codes : (a) (b) (c) (d)

- **1.** (iii) (iv) (ii) (i)
- **2.** (ii) (iii) (i) (iv)
- **3.** (iv) (iii) (ii) (i)
- **4.** (ii) (iii) (iv) (i)

> [!TIP]
> **Correct answer: 4. (ii) (iii) (iv) (i)**

## Solution

Demand paging is analyzed with the working-set concept, so (a)–(ii). Segmentation mirrors the programmer's logical view of memory, so (b)–(iii). Dynamic partitions suffer external fragmentation and may require compaction, so (c)–(iv). Fixed partitions cap the number of resident processes and therefore the degree of multiprogramming, so (d)–(i). The sequence is (ii),(iii),(iv),(i).

## Key Points

- Working set→paging; user view→segmentation; compaction→dynamic partitions; multiprogramming degree→fixed partitions.

## Why the other options are incorrect

The other codes confuse paging locality, logical segmentation, external-fragmentation repair, and the process-count limit imposed by fixed partitions.
