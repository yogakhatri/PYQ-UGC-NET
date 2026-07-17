# Question 28

*UGC NET CS · 2017 Jan Paper 2 · OSI and TCP/IP Layer Functions · Default Gateway and Off-Subnet Delivery*

A packet whose destination is outside the local TCP/IP network segment is sent to _____.

- **1.** File server
- **2.** DNS server
- **3.** DHCP server
- **4.** Default gateway

> [!TIP]
> **Correct answer: 4. Default gateway**

## Solution

The host applies its subnet mask to determine whether the destination is on the local IP subnet. If it is not, the host sends the frame to the next-hop router configured by the default route—the default gateway—while keeping the remote host as the packet's IP destination. Therefore option 4 is correct.

## Key Points

- On-subnet destination → deliver directly; off-subnet destination → send the frame to a router/default gateway.

## Why the other options are incorrect

A file server supplies files, DNS resolves names to addresses, and DHCP supplies configuration parameters. None of those services forwards ordinary off-subnet traffic. The gateway's link-layer address is obtained locally, commonly through ARP.
