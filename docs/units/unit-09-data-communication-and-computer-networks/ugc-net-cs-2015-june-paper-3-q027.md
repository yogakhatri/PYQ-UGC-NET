# Question 27

*UGC NET CS · 2015 June Paper 3 · Network Security · IPsec Transport and Tunnel Modes*

Which are the two modes of IP security ?

- **1.** Transport and certificate
- **2.** Transport and tunnel
- **3.** Certificate and tunnel
- **4.** Preshared and transport

> [!TIP]
> **Correct answer: 2. Transport and tunnel**

## Solution

IPsec defines transport mode and tunnel mode. Transport mode protects the IP payload while retaining the original outer IP header, making it suitable for host-to-host protection. Tunnel mode protects the entire original IP packet and wraps it in a new outer IP header, which is common for VPN gateways.

## Key Points

- IPsec transport mode protects payload; tunnel mode encapsulates and protects the original packet.

## Why the other options are incorrect

Certificates and preshared keys are authentication or key-establishment choices, not IPsec packet-processing modes. Any option pairing one of them with transport or tunnel therefore mixes different concepts.
