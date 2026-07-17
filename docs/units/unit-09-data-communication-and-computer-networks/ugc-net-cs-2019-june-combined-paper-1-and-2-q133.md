# Question 133

*UGC NET CS · 2019 June Paper 1 And 2 · Data Communication · Propagation Delay*

You are designing a link-layer protocol for a 1 Gbps link over an 800 km fibre, where propagation speed is 200000 km/s. What is the propagation delay?

- **1.** 1 millisecond
- **2.** 2 milliseconds
- **3.** 3 milliseconds
- **4.** 4 milliseconds

> [!TIP]
> **Correct answer: 4. 4 milliseconds**

## Solution

Propagation delay equals distance divided by propagation speed. Thus delay=800 km/(200000 km/s)=0.004 s=4 ms. The 1 Gbps data rate affects transmission delay—the time to put a frame's bits onto the link—but it does not affect how long a signal takes to travel 800 km.

## Key Points

- Propagation delay=d/s; transmission delay=packet bits/link rate.
- Keep the two delays separate.

## Why the other options are incorrect

One, two and three milliseconds result from incorrect distance/speed arithmetic. No frame length is supplied because it is unnecessary for propagation delay.
