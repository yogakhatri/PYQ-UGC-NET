# Question 25

*UGC NET CS · 2014 Dec Paper 3 · Data Communication · Full-Mesh Link Count*

For n devices in a network, how many duplex-mode links are required for a full-mesh topology?

- **A.** n(n + 1)
- **B.** n (n – 1)
- **C.** n(n + 1)/2
- **D.** n(n – 1)/2

> [!TIP]
> **Correct answer: D. n(n – 1)/2**

## Solution

In a full mesh, every unordered pair of distinct devices needs one duplex link. There are n choices for the first endpoint and n−1 for the second, but this counts each pair twice: once as (u,v) and once as (v,u). Dividing by two gives C(n,2)=n(n−1)/2 links.

## Key Points

- One duplex link serves both directions, so count unordered device pairs with the binomial coefficient C(n,2).

## Why the other options are incorrect

n(n−1) double-counts every duplex link. Formulas containing n(n+1) act as though self-links or an extra endpoint were present. A full mesh has no device-to-itself link, so option D is the only correct count.
