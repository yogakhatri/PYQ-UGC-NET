# Question 122

*UGC NET CS · 2020 Nov With Answers · Network Layering · Protocols and TCP/IP Layers*

Match the protocols to their TCP/IP/OSI layer: (A) Serial Line IP (SLIP), (B) Border Gateway Protocol (BGP), (C) User Datagram Protocol (UDP), (D) Simple Network Management Protocol (SNMP) with (I) application, (II) transport, (III) data link, (IV) network.

- **1.** A-I, B-II, C-III, D-IV
- **2.** A-III, B-IV, C-II, D-I
- **3.** A-II, B-III, C-IV, D-I
- **4.** A-III, B-I, C-IV, D-II

> [!TIP]
> **Correct answer: 2. A-III, B-IV, C-II, D-I**

## Solution

SLIP frames IP datagrams over a serial line and is placed at the data-link access layer, so A→III. BGP exchanges routing information and is classified here with the network/routing layer, so B→IV. UDP is a transport protocol, so C→II. SNMP is an application-layer network-management protocol, so D→I. The mapping is option 2.

## Key Points

- SLIP links, BGP routes, UDP transports, and SNMP provides an application service.

## Why the other options are incorrect

The distractors place UDP outside transport or SNMP outside application. BGP runs over TCP in implementation, but its functional role in this exam classification is inter-domain network-layer routing.
