# Question 113

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

stoption TD=450521 510 67063 Consider two hosts P and Q are connected through a router R. The maximum transfer unit (MTU) value of the link between Pand Ris 1500 bytes and between R and Q is 820 bytes. A TCP segment of size of 1400 bytes is transferred from P to Q through R with IP identification value of 0x12334. Assume that IP header size is 20 bytes. Further the packet is allowed to be fragmented that is Don't Fragment (DF) flag in the IP Header is not set by P. Which of the following statement is/are not true? A. Two fragments are created at R and IP datagram size carrying the second fragment is 620 bytes B. If the second fragment is lost then R resend the fragment with IP Identification value of 0x1234 C. If the second fragment lost then P required to resend the entire TCP segment D. TCP destination port can be determined by analyzing the second fragment only Choose the correct answer from the options given below:

- **1.** A and B Only
- **2.** A and C Only
- **3.** C and D Only
- **4.** Band D Only

> [!TIP]
> **Correct answer: 4. Band D Only**

## Solution

Fragment payloads are 800 and 600 bytes, so the second datagram is 620 bytes: A true. Routers do not retransmit fragments, so B false. TCP at P retransmits after loss, so C true. Only the first fragment contains the TCP header/port, so D false. The not-true statements are B,D.

## Key Points

- IP routers fragment but do not recover loss; TCP endpoints do.

## Why the other options are incorrect

Other options mark A or C false even though their fragmentation/TCP behavior is correct.
