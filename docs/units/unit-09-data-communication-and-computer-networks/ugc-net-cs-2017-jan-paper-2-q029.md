# Question 29

*UGC NET CS · 2017 Jan Paper 2 · Routing Algorithms · Distance-Vector Neighbor Exchanges*

Distance vector routing algorithm is a dynamic routing algorithm. The routing tables in distance vector routing algorithm are updated _____.

- **1.** automatically
- **2.** by server
- **3.** by exchanging information with neighbour nodes
- **4.** with back up database

> [!TIP]
> **Correct answer: 3. by exchanging information with neighbour nodes**

## Solution

In distance-vector routing, each router periodically or reactively sends its current distance vector to directly connected neighbors. A router combines the received neighbor costs with its link cost to that neighbor, applying the Bellman-Ford recurrence to update its own table. Hence the tables are updated by exchanging information with neighbor nodes, option 3.

## Key Points

- Distance vector shares route costs with neighbors; link state floods topology information to all routers.

## Why the other options are incorrect

'Automatically' is too vague and omits the mechanism. A central server and a backup database are not required by the distributed distance-vector algorithm.
