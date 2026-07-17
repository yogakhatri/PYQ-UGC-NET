# Question 16

*UGC NET CS · 2013 June Paper 3 · Network Topologies · Full-Mesh Link Count*

In a fully connected mesh network with n devices, there are ________ physical channels to link all devices.

- **A.** n(n–1)/2
- **B.** n(n+1)/2
- **C.** 2n
- **D.** 2n+1

> [!TIP]
> **Correct answer: A. n(n–1)/2**

## Solution

In a full mesh, every unordered pair of distinct devices needs one direct physical channel. Device 1 can be paired with n-1 others, device 2 with n-2 new others, and so on, giving (n-1)+(n-2)+...+1=n(n-1)/2 links. Division by two avoids counting the same link once from each endpoint.

## Key Points

- Full-mesh links equal the number of 2-device combinations: C(n,2)=n(n-1)/2.

## Why the other options are incorrect

n(n+1)/2 includes n extra self-pairs that are not links between different devices. 2n and 2n+1 grow only linearly, but a full mesh needs a link for every pair and therefore grows quadratically.
