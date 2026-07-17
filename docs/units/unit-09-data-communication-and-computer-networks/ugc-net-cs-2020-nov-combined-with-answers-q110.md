# Question 110

*UGC NET CS · 2020 Nov With Answers · Network Security · Packet-Filtering Firewall Fields*

A firewall filters access to a protected network. A packet-filtering firewall can filter packets using which fields? (A) Source IP address, (B) destination IP address, (C) TCP source port, (D) UDP source port, (E) TCP destination port.

- **1.** (A), (B) and (C) only
- **2.** (B) and (E) only
- **3.** (C) and (D) only
- **4.** (A), (B), (C), (D) and (E)

> [!TIP]
> **Correct answer: 4. (A), (B), (C), (D) and (E)**

## Solution

A packet-filtering firewall can examine network-layer source and destination IP addresses and transport-layer protocol/port fields. It may therefore match source IP (A), destination IP (B), TCP source port (C), UDP source port (D), and TCP destination port (E). Rules often combine these fields with direction, protocol, interface, or connection state. All five listed fields are usable, so option 4.

## Key Points

- Basic packet filters match the IP five-tuple: protocol, source/destination addresses, and source/destination ports.

## Why the other options are incorrect

Options 1–3 list valid subsets but omit other equally filterable header fields. UDP ports are just as available for filtering as TCP ports once the IP protocol identifies the transport header.
