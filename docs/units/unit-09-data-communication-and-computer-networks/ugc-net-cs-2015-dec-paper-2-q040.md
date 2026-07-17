# Question 40

*UGC NET CS · 2015 Dec Paper 2 · Network Layer · Congestion-Prevention Policies*

Which of the following is not a congestion policy at network layer ?

- **1.** Flow Control Policy
- **2.** Packet Discard Policy
- **3.** Packet Lifetime Management Policy
- **4.** Routing Algorithm

> [!TIP]
> **Correct answer: 1. Flow Control Policy**

## Solution

In the standard layer-by-layer congestion-prevention table, network-layer policies include routing choice, packet-discard policy, and packet-lifetime management. Flow-control policy is associated with link/transport regulation between sender and receiver, not listed as a network-layer congestion policy. Therefore option 1 is the exception.

## Key Points

- Flow control protects a receiver; congestion control protects the network as a whole.

## Why the other options are incorrect

Routing can steer traffic away from overloaded regions; discard policy controls which packets are shed; lifetime management prevents stale packets from consuming resources. Each can affect network-layer congestion.
