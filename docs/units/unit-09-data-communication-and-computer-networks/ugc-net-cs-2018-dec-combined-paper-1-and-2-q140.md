# Question 140

*UGC NET CS · 2018 Dec Paper 1 And 2 · Network Security · Pairwise Symmetric-Key Count*

Suppose that everyone in a group of N people wants to communicate secretly with the other (N - 1) people using a symmetric-key cryptographic system. Communication between any two persons should not be decodable by the others in the group. The number of keys required in the system as a whole to satisfy the confidentiality requirement is:

- **1.** N(N - 1)
- **2.** N(N - 1)/2
- **3.** 2N
- **4.** (N - 1)^2

> [!TIP]
> **Correct answer: 2. N(N - 1)/2**

## Solution

Each pair of people needs one symmetric key known only to those two people. A shared key works in both communication directions, so ordered pairs must not be counted separately. The number of unordered pairs among N people is C(N,2)=N(N-1)/2. Therefore option 2 is correct.

## Key Points

- Pairwise symmetric keys correspond to edges of a complete graph on N users: N choose 2.

## Why the other options are incorrect

N(N-1) double-counts each pair as A→B and B→A even though symmetric communication uses the same key. 2N and (N-1)^2 do not count all distinct unordered pairs and fail even on small examples such as N=3, which needs exactly three pairwise keys.
