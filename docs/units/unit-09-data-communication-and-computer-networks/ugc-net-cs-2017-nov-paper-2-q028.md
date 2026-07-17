# Question 28

*UGC NET CS · 2017 Nov Paper 2 · Ethernet · 48-bit MAC Addressing*

The number of bits used for addressing in Gigabit Ethernet is __________.

- **1.** 32 bits
- **2.** 48 bits
- **3.** 64 bits
- **4.** 128 bits

> [!TIP]
> **Correct answer: 2. 48 bits**

## Solution

Gigabit Ethernet changes Ethernet's data rate and physical-layer implementation, but it retains the standard Ethernet frame addressing format. Both destination and source MAC address fields are 6 bytes long, and 6×8=48 bits. Therefore option 2 is correct.

## Key Points

- Ethernet speed does not change its MAC-address width: 6 bytes = 48 bits.

## Why the other options are incorrect

32 and 128 bits are familiar IPv4 and IPv6 address lengths, not Ethernet MAC lengths. 64-bit identifiers appear in other link technologies and in EUI-64 contexts, but ordinary Ethernet MAC addressing uses 48 bits.
