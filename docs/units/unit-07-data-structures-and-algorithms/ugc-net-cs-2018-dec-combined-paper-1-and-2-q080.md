# Question 80

*UGC NET CS · 2018 Dec Paper 1 And 2 · Advanced Algorithms · Tournament Method for Second Minimum*

The second smallest of n elements can be found with _____ comparisons in the worst case.

- **1.** n - 1
- **2.** lg n
- **3.** n + ceil(lg n) - 2
- **4.** 3n/2

> [!TIP]
> **Correct answer: 3. n + ceil(lg n) - 2**

## Solution

Run a balanced knockout tournament to find the minimum. This takes n−1 comparisons. The second-smallest element must be one of the elements that lost directly to the minimum—nobody else can be second because they lost to a smaller nonminimum element. The winner participates in at most ⌈lg n⌉ matches, so at most ⌈lg n⌉ candidates lost directly to it; finding the smallest among them takes ⌈lg n⌉−1 more comparisons. Total=(n−1)+(⌈lg n⌉−1)=n+⌈lg n⌉−2, option 3.

## Key Points

- In a comparison tournament, the runner-up/second minimum must have lost directly to the champion/minimum.

## Why the other options are incorrect

n−1 finds only the minimum. lg n ignores the comparisons needed to establish the minimum. 3n/2 is associated with paired min-and-max bounds, not the optimal second-minimum tournament count.

## References

- [Princeton Algorithms — minimum comparisons for smallest and second smallest](https://algs4.cs.princeton.edu/14analysis/)
