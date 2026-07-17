# Question 12

*UGC NET CS · 2015 Dec Paper 3 · OSI and TCP/IP Layer Functions · Routing*

Consider a subnet with 720 routers. If a three-level hierarchy is choosen with eight clusters, each containing 9 regions of 10 routers, then total number of entries in the routing table is __________.

- **1.** 25
- **2.** 27
- **3.** 53
- **4.** 72

> [!TIP]
> **Correct answer: 1. 25**

## Solution

A router keeps detailed entries for the 10 routers in its own region. The other 8 regions in its 9-region cluster can each be summarized by one entry, and the other 7 clusters can each be summarized by one entry. Thus the routing table needs 10+8+7=25 entries.

## Key Points

- Hierarchical routing keeps detail locally and one summarized entry for each peer group at higher levels.

## Why the other options are incorrect

27 counts all 9 regions and all 8 clusters in addition to the 10 local-router entries, double-counting the current region/cluster levels. 53 and 72 do not exploit the three-level aggregation described.
