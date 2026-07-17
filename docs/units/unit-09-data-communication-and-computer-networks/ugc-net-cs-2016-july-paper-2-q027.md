# Question 27

*UGC NET CS · 2016 July Paper 2 · Network Models · Fully Connected Mesh Topology*

In a fully-connected mesh network with 10 computers, total ______ number of cables are required and ______ number of ports are required for each device.

- **1.** 40, 9
- **2.** 45, 10
- **3.** 45, 9
- **4.** 50, 10

> [!TIP]
> **Correct answer: 3. 45, 9**

## Solution

In a full mesh, every unordered pair of n devices needs one point-to-point cable, so links=n(n−1)/2. For n=10 this is 10·9/2=45. Each device connects directly to the other n−1=9 devices, so it needs 9 ports. The pair is (45,9), option 3.

## Key Points

- Full mesh: links=C(n,2); ports per device=n−1.

## Why the other options are incorrect

Counting ordered pairs gives 90 and double-counts every cable. Ten ports would include a nonexistent self-connection. The other choices therefore miscount either pairs or per-device neighbors.
