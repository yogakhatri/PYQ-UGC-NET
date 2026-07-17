# Question 16

*UGC NET CS · 2011 Dec Paper 3 · Data Communication · Broadcast and Switched LANs*

Why does LAN tend to use Broadcast Network ? Why not use Netw orks consisting of multiplexer and switches ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: A shared broadcast medium was simple and economical for a small local area; dedicated switching historically added cost and complexity**

## Solution

A LAN covers a limited distance, has relatively few stations and normally offers high bandwidth with low propagation delay and low error rate. A shared cable or radio channel can therefore be heard by every attached station; each frame carries a destination MAC address, and only the addressed station accepts it. Broadcast and multicast are natural, adding a station is simple, and medium-access control such as CSMA/CD or token passing coordinates sharing without a separate circuit for every pair.

A design built from central multiplexers or switches needs additional ports, cabling, buffering and control. Early LAN technology made that equipment relatively expensive and could create a central bottleneck or failure point, while a passive shared medium was economical for a small site.

This is a historical design explanation, not a claim about all modern LANs. Contemporary Ethernet is normally switched: each host has a point-to-point link to a switch, collisions disappear in full duplex and links can operate concurrently. It still provides a broadcast domain at the link layer (bounded by VLANs/routers), and wireless LAN remains inherently shared.

## Key Points

- Shared-medium broadcast matched early LAN scale and economics; modern switched LANs retain MAC broadcast semantics while using point-to-point physical links.

## Common mistakes to avoid

Do not claim broadcast scales without limit; contention and broadcast traffic become problems as a LAN grows. Do not claim LANs never use switches—modern Ethernet overwhelmingly does.
