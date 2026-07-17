# Question 17

*UGC NET CS · 2012 June Paper 2 · OSI and TCP/IP Layer Functions · Link-state routing*

In which Routing Method do all the routers have a common database ?

- **A.** Distance vector
- **B.** Link state
- **C.** Link vector
- **D.** Dijkestra method

> [!TIP]
> **Correct answer: B. Link state**

## Solution

In a link-state routing protocol, each router floods descriptions of its local links. After reliable flooding converges, all routers in the routing area have the same link-state database representing the topology. Each independently runs a shortest-path algorithm, commonly Dijkstra's algorithm, on that common database.

## Key Points

- Link-state routing floods topology information so every router can compute paths from the same database.

## Why the other options are incorrect

Distance-vector routers exchange distance estimates with neighbours and do not maintain a complete common topology database. 'Link vector' is not the standard method here. Dijkstra is the computation performed on the database, not the routing information-distribution method.
