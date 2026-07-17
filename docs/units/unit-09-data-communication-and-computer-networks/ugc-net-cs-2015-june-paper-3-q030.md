# Question 30

*UGC NET CS · 2015 June Paper 3 · Transport Layer · Maximum TCP Payload over IPv4*

The maximum payload of a TCP segment is :

- **1.** 65,535
- **2.** 65,515
- **3.** 65,495
- **4.** 65,475

> [!TIP]
> **Correct answer: 3. 65,495**

## Solution

An IPv4 datagram's 16-bit Total Length field permits at most 65,535 bytes including headers. With minimum headers and no options, IPv4 consumes 20 bytes and TCP consumes another 20. Maximum TCP application payload in one IPv4 datagram is therefore `65,535 − 20 − 20 = 65,495 bytes`.

## Key Points

- Maximum TCP data over IPv4 = IP total-length maximum − minimum IP header − minimum TCP header.

## Why the other options are incorrect

65,535 subtracts no headers; 65,515 subtracts only one 20-byte header; and 65,475 subtracts 60 bytes. IP or TCP options would reduce the maximum further, so 65,495 is specifically the no-options theoretical maximum.
