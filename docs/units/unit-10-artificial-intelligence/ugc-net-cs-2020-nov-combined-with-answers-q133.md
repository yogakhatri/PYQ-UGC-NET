# Question 133

*UGC NET CS · 2020 Nov With Answers · Machine Learning · Correlation and K-Means Centroids*

Two variables V1 and V2 are used for k-means clustering with k=3. Statement I: If V1 and V2 have correlation 1, the cluster centroids will lie on a straight line. Statement II: If V1 and V2 have correlation 0, the cluster centroids will lie on a straight line. Choose the correct evaluation.

- **1.** Both Statement I and Statement Il are true
- **2.** Both Statement I and Statement Il are false
- **3.** Statement I is correct but Statement Il is false
- **4.** Statement I is incorrect but Statement II is true

> [!TIP]
> **Correct answer: 3. Statement I is correct but Statement Il is false**

## Solution

Correlation +1 means V1 and V2 have an exact positive affine relationship, V2=aV1+b with a>0, assuming nonzero variances. Every data point therefore lies on one straight line. A k-means centroid is the coordinate-wise mean of its cluster, and the mean of points satisfying that affine equation also satisfies it; all three centroids are consequently collinear. Correlation 0 only means zero linear covariance. The data may have a nonlinear pattern or a two-dimensional spread, so its three centroids need not be collinear. Statement I is true and Statement II false: option 3.

## Key Points

- Perfect correlation gives an exact affine line; zero correlation does not imply either independence or collinearity.

## Why the other options are incorrect

Options 1 and 4 incorrectly treat zero correlation as a geometric straight-line constraint. Option 2 misses that perfect positive correlation does impose an exact line and that averaging preserves the line.
