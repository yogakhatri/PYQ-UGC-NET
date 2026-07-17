# Question 132

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · Address Resolution Protocol*

What is the name of the protocol that allows a client to send a broadcast message with its MAC address and receive an IP address in reply?

- **1.** ARP
- **2.** DNS
- **3.** RARP
- **4.** ICMP

> [!TIP]
> **Correct answer: 3. RARP**

## Solution

Reverse Address Resolution Protocol (RARP) was designed for a host that knows its hardware or MAC address but not its IP address. The client broadcasts a RARP request containing the MAC address, and a RARP server replies with the corresponding IP address. Therefore the described protocol is RARP.

## Key Points

- ARP asks IP-to-MAC; RARP historically asked MAC-to-IP.
- DHCP later became the usual address-configuration protocol.

## Why the other options are incorrect

- **ARP:** maps a known IPv4 address to a link-layer address.
- **DNS:** maps domain names to resource records such as IP addresses.
- **ICMP:** carries network-layer control and error messages.
