# Question 21

*UGC NET CS · 2017 Jan Paper 2 · Arrays · Operation Complexity in a Sorted Array*

Which of the following is true for computation time in insertion, deleti on and finding maximum and minimum element in a sorted array ?

- **1.** Insertion – O(1), Deletion – O(1), Maximum – O(1), Minimum – O(1)
- **2.** Insertion – O(1), Deletion – O(1), Maximum – O(n), Minimum – O(n)
- **3.** Insertion – O(n), Deletion – O(n), Maximum – O(1), Minimum – O(1)
- **4.** Insertion – O(n), Deletion – O(n), Maximum – O(n), Minimum – O(n)

> [!TIP]
> **Correct answer: 3. Insertion – O(n), Deletion – O(n), Maximum – O(1), Minimum – O(1)**

## Solution

In a contiguous sorted array, inserting an element may require shifting every larger element one position, so worst-case insertion is O(n). Deleting an element may require shifting all following elements left, so deletion is O(n). Because the array is sorted, the minimum and maximum are stored at the two endpoints and each can be read in O(1). This combination is option 3.

## Key Points

- Sorted arrays trade expensive O(n) updates for O(1) endpoint extrema and O(log n) binary search.

## Why the other options are incorrect

Options 1 and 2 ignore the shifting cost of maintaining sorted order. Option 4 ignores the direct endpoint access that makes extrema constant-time. Searching for an arbitrary value may be logarithmic, but the question asks only for known endpoints and update operations.
