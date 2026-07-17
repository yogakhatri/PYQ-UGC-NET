# Question 26

*UGC NET CS · 2017 Jan Paper 3 · Data-Link Layer · Sliding-Window Size and Bandwidth-Delay Product*

Station A uses 32 byte packets to transmit messages to station B using sliding window protocol. The round trip delay between A and B is 40 milliseconds and the bottleneck bandwidth on the path between A and B is 64 kbps. The optimal window size of A is ________.

- **1.** 20
- **2.** 10
- **3.** 30
- **4.** 40

> [!TIP]
> **Correct answer: 2. 10**

## Solution

The amount of data that can be in flight over one 40 ms round trip is bandwidth×RTT = 64,000 bit/s × 0.040 s = 2,560 bits. Each 32-byte packet carries 32×8=256 bits. The window needed to cover that bandwidth-delay product is 2,560/256=10 packets, so option 2 is correct under the question's stated RTT convention.

## Key Points

- Optimal pipeline window in packets ≈ bandwidth-delay product ÷ packet size.

## Why the other options are incorrect

Windows 20, 30, and 40 packets represent two, three, and four times the calculated bandwidth-delay product. They are larger than needed merely to keep this bottleneck busy.
