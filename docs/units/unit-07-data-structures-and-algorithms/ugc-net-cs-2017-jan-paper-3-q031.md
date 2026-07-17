# Question 31

*UGC NET CS · 2017 Jan Paper 3 · Performance Analysis and Recurrences · Recursion Trees with Logarithmic Denominators*

What is the asymptotic upper bound for T(n)=2T(n/2)+n/lg n?

- **1.** O(n²)
- **2.** O(n lg n)
- **3.** O(n lg lg n)
- **4.** O(lg lg n)

> [!TIP]
> **Correct answer: 3. O(n lg lg n)**

## Solution

Let n=2^m and inspect a recursion tree. At level i there are 2^i subproblems of size n/2^i. Their combined nonrecursive cost is 2^i·[(n/2^i)/lg(n/2^i)] = n/(lg n−i). Summing over i=0,…,lg n−1 gives n·(1+1/2+⋯+1/lg n)=Θ(n lg lg n). The leaves contribute Θ(n), which is smaller. Therefore T(n)=Θ(n lg lg n), and option 3 gives the required upper bound.

## Key Points

- For T(n)=2T(n/2)+n/lg n, level costs form n times a harmonic sum over 1,…,lg n.

## Why the other options are incorrect

O(n lg n) and O(n²) are valid loose upper bounds but are not the tight asymptotic solution intended by the choices. O(lg lg n) ignores the Θ(n) leaves and the factor n at every level sum.
