# Question 137

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · Protocol Data Units*

Which of the following statements is/are true with regard to various layers in the Internet stack? P : At the link layer, a packet of transmitted information is called a frame. Q: At the network layer, a packet of transmitted information is called a segment.

- **1.** P only
- **2.** Qonly
- **3.** Pand Q
- **4.** Neither P nor Q Options :

> [!TIP]
> **Correct answer: 1. P only**

## Solution

P is true: the link-layer protocol data unit is a frame. Q is false: at the network layer it is normally called a packet or IP datagram. The term segment belongs to the transport layer, especially TCP. Thus only P is correct.

## Key Points

- Application message -> transport segment/datagram -> network packet/datagram -> link frame.

## Why the other options are incorrect

Options 2 and 3 accept the incorrect network-layer term 'segment'. Option 4 rejects the correct link-layer term 'frame'.
