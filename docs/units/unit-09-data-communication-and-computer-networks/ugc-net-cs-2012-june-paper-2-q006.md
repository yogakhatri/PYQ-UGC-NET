# Question 6

*UGC NET CS · 2012 June Paper 2 · OSI and TCP/IP Layer Functions · Router Protocol Stack*

Both hosts and routers are TCP/IP protocol software. However, routers do not use protocol from all layers. The layer for which protocol software is not needed by a router is

- **A.** Layer – 5 (Application)
- **B.** Layer – 1 (Physical)
- **C.** Layer – 3 (Internet)
- **D.** Layer – 2 (Network Interface)

> [!TIP]
> **Correct answer: A. Layer – 5 (Application)**

## Solution

A router must receive and transmit bits and frames on its interfaces, so it needs physical and network-interface protocols. It must inspect and forward IP datagrams, so it needs the Internet layer. Ordinary packet forwarding does not run end-user application protocols, so application-layer protocol software is not required for the routing function.

## Key Points

- An IP router forwards through the lower layers up to Internet/IP; end hosts consume application data.

## Why the other options are incorrect

Without Physical and Network Interface layers the router could not communicate on attached links; without the Internet layer it could not route IP packets. A managed router may host applications for configuration, but those are not required by its forwarding role.
