# Question 32

*UGC NET CS · 2016 July Paper 3 · Performance Analysis · Expected Inversions in a Random Permutation*

Let A[1…n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. What is the expected number of inversions in any permutation on n elements ?

- **1.** Θ(n)
- **2.** Θ(log n)
- **3.** Θ(n log n)
- **4.** Θ(n²)

> [!TIP]
> **Correct answer: 4. Θ(n²)**

## Solution

There are C(n,2)=n(n−1)/2 index pairs i<j. In a uniformly random permutation, either relative order of the two distinct values is equally likely, so each pair is an inversion with probability 1/2. By linearity of expectation, E[inversions]=C(n,2)/2=n(n−1)/4=Θ(n²). Hence option 4.

## Key Points

- Use indicator variables: one per pair, with expectation 1/2; linearity gives n(n−1)/4.

## Why the other options are incorrect

The expectation is quadratic because there are quadratically many possible pairs, each contributing a constant expected amount. Θ(n), Θ(log n), and Θ(n log n) grow too slowly.
