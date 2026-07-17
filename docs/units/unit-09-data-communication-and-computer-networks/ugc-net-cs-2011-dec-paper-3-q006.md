# Question 6

*UGC NET CS · 2011 Dec Paper 3 · OSI and TCP/IP Layer Functions · Centralized and Distributed Routing*

What is the difference between centralized routing and distributed routing ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Centralized routing computes routes at one controller; distributed routing computes them cooperatively at routers**

## Solution

In centralized routing, one controller or routing control centre collects topology and traffic information, computes paths for the network and distributes forwarding rules. It can optimize with a global view and keep policy consistent, and it simplifies individual routers. Its weaknesses are controller failure or attack, stale information during collection, communication overhead and scalability bottlenecks; practical systems use replication to reduce these risks.

In distributed routing, each router runs the algorithm and exchanges information with neighbours or peers. Distance-vector protocols exchange distance estimates; link-state protocols flood local link state and each router computes shortest paths. Distributed control has no single computation point, adapts locally and scales through hierarchy, but convergence may be slower and transient loops or inconsistent views can occur.

The distinction concerns the control plane, not necessarily packet forwarding. Software-defined networking is logically centralized even when the controller is physically replicated; conventional IP routing is distributed.

## Key Points

- Centralized: global computation and policy at a controller.
- Distributed: routers exchange state and converge on routes.

## Common mistakes to avoid

Do not say centralized routing requires every packet to pass through the controller—the controller normally installs forwarding state. Do not say distributed routing has no global result; global routes emerge from exchanged local information.
