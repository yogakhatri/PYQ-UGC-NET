# Question 9

*UGC NET CS · 2012 Dec Paper 2 · OSI and TCP/IP Layer Functions · IPv4 Fragmentation*

If a packet arrives with its M-bit equal to 1 and its fragmentation-offset value equal to 0, it is which fragment?

- **1.** First
- **2.** Middle
- **3.** Last
- **4.** All of the above

> [!TIP]
> **Correct answer: 1. First**

## Solution

In IPv4 fragmentation, a fragmentation offset of 0 means the fragment begins with the first byte of the original datagram's payload. An M/MF bit of 1 means more fragments follow. Together, offset=0 and MF=1 identify the first fragment of a fragmented datagram.

## Key Points

- IPv4 fragment test: offset 0 means first position; MF 1 means not last.
- Both together mean first fragment with more to come.

## Why the other options are incorrect

A middle fragment has a nonzero offset and MF=1. The last fragment has MF=0 and normally a nonzero offset. The same header combination therefore cannot describe all fragment positions.
