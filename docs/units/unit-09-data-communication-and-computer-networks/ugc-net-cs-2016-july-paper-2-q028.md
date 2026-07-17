# Question 28

*UGC NET CS · 2016 July Paper 2 · OSI and TCP/IP Layer Functions · Internet Layer versus Host-to-Network Layer*

In TCP/IP Reference model, the job of _______ layer is to permit hosts to inject packets into any network and travel them independently to the destination.

- **1.** Physical
- **2.** Transport
- **3.** Application
- **4.** Host-to-network

> [!TIP]
> **Correct answer: No listed option — the described function belongs to the TCP/IP Internet layer**

## Solution

No listed option is correct. The quoted function belongs to the TCP/IP Internet layer: it accepts datagrams from hosts, routes them across interconnected networks, and treats different datagrams independently. That layer contains IP. The question omits 'Internet' from its answer choices.

## Key Points

- TCP/IP Internet layer routes independent IP datagrams across networks; host-to-network handles access to the local link.

## Why the other options are incorrect

The physical layer transmits signals, the transport layer provides end-to-end process communication, and the application layer supports network applications. The host-to-network (network-access/link) layer lets a host place an IP datagram onto its directly attached network; it does not perform inter-network routing to the destination. Some unofficial keys select option 4, but that confuses the access layer with the Internet layer named by the textbook definition.
