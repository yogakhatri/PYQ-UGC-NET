# Question 14

*UGC NET CS · 2012 June Paper 2 · OSI and TCP/IP Layer Functions · RARP*

Which TCP/IP protocol was historically used by a diskless machine to obtain its IP address from a server?

- **A.** RARP
- **B.** RIP
- **C.** ARP
- **D.** X.25

> [!TIP]
> **Correct answer: A. RARP**

## Solution

A diskless host could know its hardware/MAC address but have no local storage containing an IP configuration. Reverse Address Resolution Protocol (RARP) lets it broadcast that MAC address and receive its assigned IP address from a RARP server. The source's 'RAP' is a printing/OCR omission of the second R.

## Key Points

- RARP historically mapped MAC-to-IP for booting hosts; ARP maps IP-to-MAC.

## Why the other options are incorrect

RIP exchanges routing information. ARP maps a known IPv4 address to a MAC address—the opposite direction. X.25 is a packet-switched network protocol suite. BOOTP and later DHCP replaced RARP in practice but are not listed.
