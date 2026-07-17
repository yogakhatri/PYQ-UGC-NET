# Question 22

*UGC NET CS · 2013 June Paper 3 · Ethernet · Manchester Encoding and Baud Rate*

What is the baud rate of the standard 10 Mbps Ethernet ?

- **A.** 10 megabaud
- **B.** 20 megabaud
- **C.** 30 megabaud
- **D.** 40 megabaud

> [!TIP]
> **Correct answer: B. 20 megabaud**

## Solution

Standard 10-Mbps Ethernet uses Manchester coding. Each data bit is represented by two half-bit signal intervals with a mandatory mid-bit transition, so the signal-element rate is twice the data rate: 2×10 Mbit/s=20 Mbaud.

## Key Points

- Manchester encoding needs two signal elements per bit, so baud rate is twice bit rate.

## Why the other options are incorrect

10 Mbaud would apply to one signal element per bit, not Manchester's two. 30 and 40 Mbaud imply three or four signal elements per bit and do not match standard 10-Mbps Ethernet coding.
