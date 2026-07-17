# Question 104

*UGC NET CS · 2019 Dec Paper 1 And 2 · Routing Algorithms · Hierarchical Routing Tables*

A subnet has 720 routers arranged in a three-level hierarchy: 8 clusters, each containing 9 regions of 10 routers. How many entries are in the hierarchical routing table of each router?

- **1.** 25
- **2.** 27
- **3.** 53
- **4.** 72

> [!TIP]
> **Correct answer: 1. 25**

## Solution

A router keeps detailed entries for the 10 routers in its own region. For the other regions of its cluster it needs one summarized entry per region, adding 9−1=8 entries. For the other clusters it needs one summarized entry per cluster, adding 8−1=7. The total is 10+8+7=25 entries, so option 1 is correct.

## Key Points

- At each hierarchy level, store detailed routes locally and one aggregate route for every other group: 10+(9−1)+(8−1).

## Why the other options are incorrect

Twenty-seven counts hierarchy groups without excluding the router's own region or cluster after their detailed entries are already represented. Fifty-three and seventy-two discard too much aggregation and approach flatter routing tables. Hierarchical routing saves space precisely by replacing remote-router entries with region or cluster summaries.
