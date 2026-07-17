# Question 30

*UGC NET CS · 2017 Jan Paper 2 · Routing Algorithms · Link-State Routing and Dijkstra's Algorithm*

In link state routing algorithm after construction of link state packets, new routes are computed using :

- **1.** DES algorithm
- **2.** Dijkstra’s algorithm
- **3.** RSA algorithm
- **4.** Packets

> [!TIP]
> **Correct answer: 2. Dijkstra’s algorithm**

## Solution

After link-state packets have been flooded, every router has a link-state database representing the network graph and edge costs. Each router runs Dijkstra's shortest-path-first algorithm with itself as the source to construct a shortest-path tree and derive next hops. Thus option 2 is correct.

## Key Points

- Link-state routing = flood link-state information, build a topology map, run Dijkstra locally.

## Why the other options are incorrect

DES and RSA are cryptographic algorithms, not routing algorithms. Packets carry the topology information but are not themselves a computation method.
