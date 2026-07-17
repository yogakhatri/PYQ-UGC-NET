# Question 13

*UGC NET CS · 2015 Dec Paper 3 · Internet Protocol · Special Classful Network Numbers*

In a classful addressing, the IP addresses with 0 (zero) as network number :

- **1.** refers to the current network
- **2.** refers to broadcast on the local network
- **3.** refers to broadcast on a distant network
- **4.** refers to loopback testing

> [!TIP]
> **Correct answer: 1. refers to the current network**

## Solution

In historical classful IPv4 notation, a network-number field of all zeros means ‘this network’ or the current network. It was used by a host that did not yet know its own network number. Therefore option 1 is correct.

## Key Points

- Classful special values: network 0=this network; network 127=loopback.

## Why the other options are incorrect

A local broadcast uses all-one host/address forms, a directed broadcast specifies a distant network with an all-one host part, and class A network 127 is reserved for loopback. These are different special-address conventions.
