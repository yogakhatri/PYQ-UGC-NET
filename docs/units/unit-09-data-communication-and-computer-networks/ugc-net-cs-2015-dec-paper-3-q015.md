# Question 15

*UGC NET CS · 2015 Dec Paper 3 · Data Communication · Transmission Rate and Transfer Time*

A device sends data at 2,000 bps. How many seconds does it take to send a file of 100,000 eight-bit characters?

- **1.** 50
- **2.** 200
- **3.** 400
- **4.** 800

> [!TIP]
> **Correct answer: 3. 400**

## Solution

At eight bits per character, 100,000 characters contain 800,000 bits. Transmission time is data size/rate=800,000 bits÷2,000 bits/s=400 seconds. No protocol overhead is specified, so none is added.

## Key Points

- Transfer time = total bits ÷ bits per second.

## Why the other options are incorrect

50 treats characters as bits; 200 effectively assumes four bits per character; 800 doubles the correct result. Convert the file to bits before dividing by bps.
