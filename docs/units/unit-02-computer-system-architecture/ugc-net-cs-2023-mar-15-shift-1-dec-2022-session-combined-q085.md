# Question 85

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Programming the Basic Computer · Input-Output Programming*

2BID:87035 In Go-back-N protocol, the values of S; (Send window, the first outstanding packet) =3, S, (Send window, the next packet to be send) =7, after receiving the packet with AckNo.6, the value of SnisM....

- **1.** 6
- **2.** 7
- **3.** 5
- **4.** 4

> [!TIP]
> **Correct answer: 1. 6**

## Solution

AckNo 6 is cumulative and announces 6 as the next expected sequence number, so packets through 5 are acknowledged. The first outstanding pointer Sf advances from 3 to 6; Sn remains 7 because no new send is described.

## Key Points

- In Go-Back-N, a cumulative ACK moves the send base to its AckNo.

## Why the other options are incorrect

7 is the unchanged next-to-send pointer, while 4 and 5 under-advance the cumulative acknowledgement.
