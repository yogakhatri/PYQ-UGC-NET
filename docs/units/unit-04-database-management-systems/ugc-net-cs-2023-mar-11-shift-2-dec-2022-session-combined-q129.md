# Question 129

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Data Warehousing and Data Mining · DBSCAN clustering procedure*

OBID:187079 Select the correct order of DBSCAN algorithm. A. Find recursively all its density connected points and assign them to the same cluster as the core point. B. Find all the neighbor points with eps and identify the core points with more than Mints neighbors. C. Iterate through the remaining unvisited pointed in the dataset. D. For each core point if it is not already assigned to a cluster, create a new cluster. Choose the correct answer from the following :

- **1.** B. D, C, A
- **2.** D. B. C.A
- **3.** B, D, A, C
- **4.** D, B, A, C

> [!TIP]
> **Correct answer: 3. B, D, A, C**

## Solution

DBSCAN first finds ε-neighborhoods and identifies core points (B). For an unassigned core it creates a cluster (D), recursively expands all density-connected points (A), then continues through remaining unvisited points (C). Hence B–D–A–C.

## Key Points

- DBSCAN: neighborhood/core test → create cluster → density expansion → continue scan.

## Why the other options are incorrect

Other orders create a cluster before identifying cores or postpone expansion until after unrelated points.
