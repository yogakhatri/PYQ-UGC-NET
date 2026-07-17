# Question 29

*UGC NET CS · 2015 June Paper 2 · Network Layer · IPv4 Total-Length Field*

What is the size of the total length field in IPv 4 datagram ?

- **1.** 4 bits
- **2.** 8 bits
- **3.** 16 bits
- **4.** 32 bits

> [!TIP]
> **Correct answer: 3. 16 bits**

## Solution

The IPv4 header's Total Length field is 16 bits wide and records the size of the entire datagram—header plus payload—in bytes. An unsigned 16-bit field can represent values through `2^16 - 1 = 65,535`, so an IPv4 datagram can have at most 65,535 bytes. The correct option is 16 bits.

## Key Points

- IPv4 Total Length: 16 bits, counting the complete datagram in bytes, maximum 65,535 bytes.

## Why the other options are incorrect

Four or eight bits could not represent the full IPv4 datagram-size range. Thirty-two bits is the width of an IPv4 address, not the Total Length header field.
