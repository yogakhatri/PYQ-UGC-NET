# Question 28

*UGC NET CS · 2017 Jan Paper 3 · Packet Switching · Payload, Header, and Packet-Size Overhead*

In a packet switching network, if the message size is 48 bytes and each packet contains a header of 3 bytes. If 24 packets are required to transmit the message, the packet size is ________.

- **1.** 2 bytes
- **2.** 1 byte
- **3.** 4 bytes
- **4.** 5 bytes

> [!TIP]
> **Correct answer: 4. 5 bytes**

## Solution

The 48-byte message is divided among 24 packets, so each packet carries 48/24=2 bytes of message payload. Each packet also contains a 3-byte header. Therefore total packet size is 2+3=5 bytes, which is option 4.

## Key Points

- Packet size = payload per packet + header = message size/packet count + header size.

## Why the other options are incorrect

Option 1 gives only the payload size and ignores the header. Options 2 and 3 match neither the per-packet payload nor payload-plus-header total.
