# Question 23

*UGC NET CS · 2015 Dec Paper 2 · Data Communication · Time-Division Multiplexing*

Four channels are multiplexed using TDM. If each channel sends 100 bytes/second and we multiplex 1 byte per channel, then the bit rate for the link is __________.

- **1.** 400 bps
- **2.** 800 bps
- **3.** 1600 bps
- **4.** 3200 bps

> [!TIP]
> **Correct answer: 4. 3200 bps**

## Solution

Each of the four input channels contributes 100 bytes/s, so the aggregate payload rate is 4×100=400 bytes/s. With no synchronization overhead stated, multiply by 8 bits per byte: 400×8=3,200 bits/s. Multiplexing one byte from each channel only describes the four-byte frame; it does not change the aggregate rate.

## Key Points

- Synchronous TDM link rate is the sum of channel rates, converted to common units.

## Why the other options are incorrect

400 is the aggregate in bytes per second, not bits per second. 800 and 1,600 account for only one or two channels after conversion.
