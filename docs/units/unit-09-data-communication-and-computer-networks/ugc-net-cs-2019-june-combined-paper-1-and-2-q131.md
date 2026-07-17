# Question 131

*UGC NET CS · 2019 June Paper 1 And 2 · Data Communication · Network Topologies*

A fully connected network topology has a direct link between every pair of nodes. For n nodes, how many direct links are there?

- **1.** n(n+1)/2
- **2.** (n+1)/2
- **3.** n^2
- **4.** n(n-1)/2

> [!TIP]
> **Correct answer: 4. n(n-1)/2**

## Solution

A direct link is needed for every unordered pair of distinct nodes. Choosing the two endpoints of a link from n nodes gives C(n,2)=n!/[2!(n-2)!]=n(n-1)/2. We do not multiply by two because the link between nodes A and B is the same physical link as the link between B and A.

## Key Points

- A full mesh with n nodes has one link per unordered node pair: C(n,2).

## Why the other options are incorrect

n(n+1)/2 counts n extra self-pairs, n^2 counts ordered pairs and self-pairs, and (n+1)/2 is not the number of node pairs.
