# Question 106

*UGC NET CS · 2019 Dec Paper 1 And 2 · Data Communication · Throughput Calculation*

A 10 Mbps network passes an average of 12,000 frames per minute, each carrying 10,000 bits. What is the network throughput?

- **1.** 1,000,000 bps
- **2.** 2,000,000 bps
- **3.** 12,000,000 bps
- **4.** 120,000,000 bps

> [!TIP]
> **Correct answer: 2. 2,000,000 bps**

## Solution

Throughput is successfully carried bits divided by elapsed time. The network carries 12,000 frames/minute × 10,000 bits/frame = 120,000,000 bits/minute. Dividing by 60 seconds/minute gives 2,000,000 bits/second, or 2 Mbps. Therefore option 2 is correct.

## Key Points

- Keep units visible: frames/min × bits/frame ÷ 60 s/min = bits/s.

## Why the other options are incorrect

One Mbps incorrectly divides or halves the traffic again. Twelve Mbps confuses the frame count with a per-second bit rate and even exceeds the stated 10 Mbps capacity. One hundred twenty Mbps is the per-minute bit total mislabeled as a per-second rate.
