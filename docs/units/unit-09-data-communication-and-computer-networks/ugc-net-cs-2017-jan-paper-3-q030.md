# Question 30

*UGC NET CS · 2017 Jan Paper 3 · Congestion Control · Token-Bucket Burst Duration*

A node X on a 10 Mbps network is regulated by a token bucket. The token bucket is filled at a rate of 2 Mbps. Token bucket is initially filled with 16 megabits. The maximum duration taken by X to transmit at full rate of 10 Mbps is _________ secs.

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: 2. 2**

## Solution

At full transmission rate, tokens are consumed at 10 Mb/s while new tokens arrive at 2 Mb/s. The bucket therefore drains at the net rate 10−2=8 Mb/s. Starting with 16 Mb of tokens, the full-rate burst can last 16/8=2 seconds before the bucket empties. Thus option 2 is correct.

## Key Points

- Token-bucket burst duration = initial tokens ÷ (peak sending rate − token refill rate).

## Why the other options are incorrect

Using 16/10 would ignore tokens generated during the burst. Durations 1, 3, or 4 seconds do not satisfy the balance 16 + 2t = 10t.
