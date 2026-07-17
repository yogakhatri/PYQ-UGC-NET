# Question 90

*UGC NET CS · 2019 June Paper 1 And 2 · Data Warehousing and Data Mining · K-means and Manhattan distance*

After the first iteration, K-means has clustered eight observations into C1={(3,3),(5,5),(7,7)}, C2={(0,6),(6,0),(3,0)}, and C3={(8,8),(4,4)}. What is the Manhattan distance of observation (4,4) from centroid C1 in the second iteration?

- **1.** 2
- **2.** sqrt(2)
- **3.** 0
- **4.** 18

> [!TIP]
> **Correct answer: 1. 2**

## Solution

The centroid of C1={(3,3),(5,5),(7,7)} is ((3+5+7)/3,(3+5+7)/3)=(5,5). The Manhattan distance from observation (4,4) to (5,5) is |4-5|+|4-5|=1+1=2.

## Key Points

- Manhattan distance in two dimensions is |x1-x2|+|y1-y2|.

## Why the other options are incorrect

- **Option 2:** √2 is the Euclidean distance, not Manhattan distance.
- **Option 3:** would apply only if the point equalled the centroid.
- **Option 4:** does not result from either common distance measure here.
