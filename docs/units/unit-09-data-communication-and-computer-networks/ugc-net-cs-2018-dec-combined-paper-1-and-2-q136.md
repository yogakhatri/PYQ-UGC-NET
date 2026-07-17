# Question 136

*UGC NET CS · 2018 Dec Paper 1 And 2 · Ethernet · Global Uniqueness of MAC Addresses*

A host is connected to a department network which is part of a university network. The university network, in turn, is part of the Internet. The largest network in which the Ethernet address of the host is unique is:

- **1.** the Internet
- **2.** the university network
- **3.** the department network
- **4.** the subnet to which the host belongs

> [!TIP]
> **Correct answer: 1. the Internet**

## Solution

A universally administered Ethernet MAC address is assigned from a globally unique IEEE identifier space, so the same address is intended not to be assigned to another interface anywhere. On that addressing assumption, its uniqueness extends across the largest listed network—the Internet—so option 1 is correct. The frame-level address is still used only on a local link; routers do not forward the original Ethernet header end to end.

## Key Points

- MAC delivery is local-link scoped, but a universally administered MAC identifier is designed to be globally unique.

## Why the other options are incorrect

The university, department, and local subnet are all smaller scopes than the global uniqueness intended for factory-assigned MAC addresses. Choosing the subnet confuses the scope in which a MAC address is used for delivery with the larger scope in which the identifier is designed to be unique.
