# Question 18

*UGC NET CS · 2015 Dec Paper 3 · Sorting Algorithms · Radix Sort Complexity*

If there are n integers to sort, each integer has d digits and each digit is in the set {1, 2, ..., k}, radix sort can sort the numbers in :

- **1.** O(d n k)
- **2.** O(d·n^k)
- **3.** O((d+n)k)
- **4.** O(d(n+k))

> [!TIP]
> **Correct answer: 4. O(d(n+k))**

## Solution

LSD radix sort performs one stable digit sort for each of the d digit positions. Counting sort on one digit scans n records and a digit alphabet of size k, costing O(n+k). Repeating that pass d times gives O(d(n+k)).

## Key Points

- Radix sort cost = number of digits × cost of one stable digit sort.

## Why the other options are incorrect

O(dnk) multiplies costs that counting sort adds; O(d·n^k) is exponential in digit alphabet size; O((d+n)k) does not represent d stable passes over all n items.
