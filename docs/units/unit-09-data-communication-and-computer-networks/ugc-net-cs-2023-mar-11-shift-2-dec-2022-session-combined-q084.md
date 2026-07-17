# Question 84

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Network Security · Secret-Key and Public-Key Algorithms*

A Computer on a 10 Mbps network is regulated by a token bucket. The token bucket is filled at a rate of 2 Mbps. It is initially filled to capacity with 16 megabits. What is the maximum duration for which the computer can transmit at the full 10 Mops?

- **1.** 1.6 seconds
- **2.** 2 seconds
- **3.** 5 seconds
- **4.** 8 seconds

> [!TIP]
> **Correct answer: 2. 2 seconds**

## Solution

While transmitting at 10 Mbps, tokens are spent at 10 Mbps but replenished at 2 Mbps, so the bucket drains at a net rate of 8 Mbps. An initially full 16-megabit bucket therefore supports the burst for 16/8=2 seconds.

## Key Points

- Maximum token-bucket burst duration = bucket capacity ÷ (peak sending rate − token generation rate).

## Why the other options are incorrect

Using 16/10 gives 1.6 seconds but ignores tokens arriving during transmission. Five or eight seconds would require a much smaller net drain rate than 10−2=8 Mbps.
