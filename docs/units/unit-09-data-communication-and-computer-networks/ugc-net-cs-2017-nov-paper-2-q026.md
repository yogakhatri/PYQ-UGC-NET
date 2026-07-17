# Question 26

*UGC NET CS · 2017 Nov Paper 2 · Data Communication · Ethernet Switching and MAC Forwarding*

Which of the following devices takes data sent from one network device and forwards it to the destination node based on MAC address ?

- **1.** Hub
- **2.** Modem
- **3.** Switch
- **4.** Gateway

> [!TIP]
> **Correct answer: 3. Switch**

## Solution

An Ethernet switch learns which source MAC addresses are reachable through each port and stores the associations in its forwarding table. For an incoming frame, it looks up the destination MAC address and forwards the frame toward the corresponding port when known. Therefore option 3 is correct.

## Key Points

- A Layer-2 switch forwards Ethernet frames using destination MAC addresses and learns its table from source MAC addresses.

## Why the other options are incorrect

A hub repeats incoming bits to all other ports without examining the destination MAC. A modem converts signaling for a transmission medium. A gateway translates or connects dissimilar protocols/networks; it is not the ordinary Layer-2 MAC forwarding device described.
