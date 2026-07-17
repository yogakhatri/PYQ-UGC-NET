# Question 5

*UGC NET CS · 2012 June Paper 2 · Network Models · Interconnecting Heterogeneous Networks*

Networks that use different technologies can be connected by using

- **A.** Packets
- **B.** Switches
- **C.** Bridges
- **D.** Routers

> [!TIP]
> **Correct answer: D. Routers**

## Solution

A router interconnects different IP networks and forwards packets using network-layer addresses. Because each interface can use a different link technology—such as Ethernet on one side and a wireless or serial link on another—the router removes the incoming link-layer frame and creates the appropriate outgoing frame while preserving the IP forwarding function.

## Key Points

- Routers join heterogeneous networks at the Internet/network layer and adapt packets to each outgoing link.

## Why the other options are incorrect

Packets are data units, not connecting devices. A basic switch or bridge connects segments at the data-link layer and normally assumes compatible link-layer framing/addressing; it does not perform the network-layer interconnection described.
