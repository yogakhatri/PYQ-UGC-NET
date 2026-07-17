# Question 11

*UGC NET CS · 2015 Dec Paper 3 · Data Communication · Throughput Calculation*

A network with bandwidth of 10 Mbps can pass only an average of 15,000 frames per minute with each frame carrying an average of 8,000 bits. What is the throughput of this network ?

- **1.** 2 Mbps
- **2.** 60 Mbps
- **3.** 120 Mbps
- **4.** 10 Mbps

> [!TIP]
> **Correct answer: 1. 2 Mbps**

## Solution

Throughput is successfully delivered bits per unit time. The network carries 15,000×8,000=120,000,000 bits per minute. Divide by 60 seconds: 2,000,000 bits/s=2 Mbps. This is below the nominal 10 Mbps bandwidth, as throughput commonly is.

## Key Points

- Throughput = frames/time × bits/frame, with consistent time units.

## Why the other options are incorrect

120 Mbps forgets the per-minute to per-second conversion. 60 Mbps uses an incorrect conversion, while 10 Mbps merely repeats link bandwidth rather than calculating actual throughput.
