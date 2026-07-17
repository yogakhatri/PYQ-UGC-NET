# Question 26

*UGC NET CS · 2016 July Paper 2 · Data Link Layer · Synchronous Time-Division Multiplexing*

A multiplexer combines four 100-Kbps channels using a time slot of 2 bits. What is the bit rate ?

- **1.** 100 Kbps
- **2.** 200 Kbps
- **3.** 400 Kbps
- **4.** 1000 Kbps

> [!TIP]
> **Correct answer: 3. 400 Kbps**

## Solution

With synchronous TDM and no stated overhead, the output link carries every input bit, so its rate is the sum of the four input rates: 4·100 Kbps=400 Kbps. Equivalently, a frame contains 4·2=8 bits; each 100-Kbps source produces a 2-bit slot 50,000 times per second, and 8·50,000=400,000 bit/s.

## Key Points

- Synchronous TDM output rate equals the sum of input bit rates when no overhead is specified.

## Why the other options are incorrect

One hundred Kbps is only one input channel, and 200 Kbps combines only two. One thousand Kbps would require unstated framing or excess overhead. The 2-bit slot changes frame size and frame frequency, not the aggregate payload rate.
