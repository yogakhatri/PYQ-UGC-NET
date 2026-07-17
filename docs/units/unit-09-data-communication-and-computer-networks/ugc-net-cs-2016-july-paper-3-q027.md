# Question 27

*UGC NET CS · 2016 July Paper 3 · Data Link Layer · Pure ALOHA Offered Load and Throughput*

A pure ALOHA Network transmits 200 bit frames using a shared channel with 200 Kbps bandwidth. If the system (all stations put together) produces 500 frames per second, then the throughput of the system is ______.

- **1.** 0.384
- **2.** 0.184
- **3.** 0.286
- **4.** 0.586

> [!TIP]
> **Correct answer: 2. 0.184**

## Solution

A 200-bit frame on a 200-Kbps channel takes T=200/200,000=0.001 s. The normalized offered load is G=500 frames/s×0.001 s=0.5. Pure ALOHA throughput is S=G·e^(−2G)=0.5e^(−1)≈0.18394, which rounds to 0.184. Therefore option 2 is correct.

## Key Points

- Pure ALOHA: G=arrival rate×frame time and normalized throughput S=Ge^(−2G).

## Why the other options are incorrect

Pure ALOHA has a two-frame vulnerable period, which creates the exponent −2G. Using slotted ALOHA's Ge^(−G), confusing offered load with throughput, or making an arithmetic error leads to the other values.
