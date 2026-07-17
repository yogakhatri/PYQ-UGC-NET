# Question 26

*UGC NET CS · 2017 Jan Paper 2 · OSI and TCP/IP Layer Functions · Protocol-to-Layer Mapping*

Match the layers and protocols for a user browsing with SSL: a. Application layer; b. Transport layer; c. Network layer; d. Data-link layer. i. TCP; ii. IP; iii. PPP; iv. HTTP. Choose the code in the order a,b,c,d.

- **1.** iv i ii iii
- **2.** iii ii i iv
- **3.** ii iii iv i
- **4.** iii i iv ii

> [!TIP]
> **Correct answer: 1. iv i ii iii**

## Solution

HTTP is an application-layer protocol, so a→iv. TCP provides transport, so b→i. IP provides network-layer addressing and routing, so c→ii. PPP frames data over a point-to-point link and belongs to the data-link layer, so d→iii. The mapping iv,i,ii,iii is option 1.

## Key Points

- HTTP/application → TCP/transport → IP/network → PPP/data link.

## Why the other options are incorrect

The other codes move TCP, IP, PPP, or HTTP to layers whose functions they do not perform. SSL/TLS protects the application exchange above TCP, but it does not change the four listed protocol-to-layer identities.
