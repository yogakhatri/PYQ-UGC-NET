# Question 41

*UGC NET CS · 2012 June Paper 2 · OSI and TCP/IP Layer Functions · Error Detection and Correction*

Which routing algorithm is used by RIP and IGRP?

- **A.** OSPF
- **B.** Link-state
- **C.** Dynamic routing (too broad)
- **D.** Distance-vector (intended; source prints 'Dijkstra vector')

> [!TIP]
> **Correct answer: D. Distance-vector (intended; source prints 'Dijkstra vector')**

## Solution

RIP and Cisco's historical IGRP are distance-vector routing protocols. Routers periodically advertise a vector of destination metrics to neighbours and update routes using Bellman-Ford-style reasoning. RIP uses hop count; IGRP used a composite metric. The source's 'Dijkstra vector' is a printing error for the intended distance-vector choice.

## Key Points

- RIP and IGRP are distance-vector; OSPF and IS-IS are link-state.

## Why the other options are incorrect

OSPF is a specific link-state protocol. Link-state routing floods topology and runs a shortest-path computation rather than exchanging only neighbour distance vectors. 'Dynamic' is true as a broad classification but does not name the algorithm family asked for.
