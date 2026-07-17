# Question 22

*UGC NET CS · 2015 Dec Paper 2 · Internet Protocol · IPv4 Fragmentation Fields*

Which field in an IPv4 datagram is not related to fragmentation?

- **1.** Type of service
- **2.** Fragment offset
- **3.** Flags
- **4.** Identification

> [!TIP]
> **Correct answer: 1. Type of service**

## Solution

IPv4 fragmentation uses Identification to group fragments of one original datagram, the MF/DF bits in Flags to describe fragmentation, and Fragment Offset to place each fragment in the reassembled payload. Type of Service—now interpreted as DSCP/ECN—expresses handling priority/congestion information and is not a fragmentation-control field.

## Key Points

- IPv4 fragmentation trio: Identification, Flags, and Fragment Offset.

## Why the other options are incorrect

Fragment Offset, Flags, and Identification work together during fragmentation and reassembly, so options 2–4 are directly related to the process.
