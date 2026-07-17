# Question 112

*UGC NET CS · 2019 June Paper 1 And 2 · Data Structures · Comparison Sorting and Auxiliary Space*

There are many comparison-based sorting algorithms. The running time of heapsort is O(n log n). Like P, but unlike Q, heapsort sorts in place. Here (P,Q) equals:

- **1.** Merge sort, Quick sort
- **2.** Quick sort, Insertion sort
- **3.** Insertion sort, Quick sort
- **4.** Insertion sort, Merge sort

> [!TIP]
> **Correct answer: 4. Insertion sort, Merge sort**

## Solution

An in-place sorting algorithm needs only O(1) auxiliary storage apart from the input array. Heapsort rearranges elements inside the array, as does insertion sort, so P is insertion sort. Standard merge sort needs a temporary array of O(n) elements and is not in-place, so Q is merge sort. Hence (P,Q) is (Insertion sort, Merge sort).

## Key Points

- Heapsort and insertion sort use constant auxiliary array space; standard merge sort uses O(n) extra space.

## Why the other options are incorrect

- **Option 1:** merge sort is not the required in-place example, while quicksort is usually in-place apart from recursion.
- **Option 2:** insertion sort is also in-place, so it cannot be Q.
- **Option 3:** quicksort is normally classified as in-place, so it cannot be Q.
