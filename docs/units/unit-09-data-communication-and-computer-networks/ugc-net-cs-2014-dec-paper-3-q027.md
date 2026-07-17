# Question 27

*UGC NET CS · 2014 Dec Paper 3 · OSI and TCP/IP Layer Functions · TCP versus IPv4 Header Fields*

Which of the following is not a field in TCP header ?

- **A.** Sequence number
- **B.** Fragment offset
- **C.** Checksum
- **D.** Window size

> [!TIP]
> **Correct answer: B. Fragment offset**

## Solution

A TCP header contains a sequence number, checksum, and receive-window field (commonly called window size). Fragment offset belongs to the IPv4 header, where it tells the receiver where an IP fragment belongs in the original datagram. TCP itself provides byte-stream sequencing rather than IP-style packet fragmentation.

## Key Points

- Fragmentation fields are in IPv4; TCP uses sequence numbers and window advertisement for reliable stream delivery.

## Why the other options are incorrect

A is essential for ordering TCP bytes and acknowledgments. C protects the TCP header and data, including an IP pseudo-header in its calculation. D supports flow control by advertising available receive space. Only B names a field from a different layer's header.
