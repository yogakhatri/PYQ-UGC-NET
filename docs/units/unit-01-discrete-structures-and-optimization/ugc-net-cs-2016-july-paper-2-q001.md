# Question 1

*UGC NET CS · 2016 July Paper 2 · Sets and Relations · Equivalence Relations and Stirling Numbers*

How many different equivalence relations with exactly three different equivalence classes are there on a set with five elements ?

- **1.** 10
- **2.** 15
- **3.** 25
- **4.** 30

> [!TIP]
> **Correct answer: 3. 25**

## Solution

Every equivalence relation corresponds uniquely to a partition of the set into its equivalence classes. Partition five labeled elements into exactly three nonempty unlabeled blocks. The possible block-size patterns are 3+1+1 and 2+2+1. For 3+1+1, choose the three-element block in C(5,3)=10 ways. For 2+2+1, choose the singleton in 5 ways and split the remaining four elements into two unordered pairs in 3 ways, giving 15. Total: 10+15=25.

## Key Points

- Equivalence relations on a set are in one-to-one correspondence with set partitions.

## Why the other options are incorrect

Ten counts only partitions of type 3+1+1, and 15 counts only type 2+2+1. Thirty double-counts some unlabeled equivalence classes. The full count is the Stirling number of the second kind S(5,3)=25.
