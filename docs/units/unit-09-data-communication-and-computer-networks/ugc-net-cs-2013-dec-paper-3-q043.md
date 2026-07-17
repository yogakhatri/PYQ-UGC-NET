# Question 43

*UGC NET CS · 2013 Dec Paper 3 · Data Communication · Multimedia Bit-Rate Calculation*

What is the bit rate for transmitting uncompressed 800 × 600 pixel colour frames with 8 bits/pixel at 40 frames/second ?

- **A.** 2.4 Mbps
- **B.** 15.36 Mbps
- **C.** 153.6 Mbps
- **D.** 1536 Mbps

> [!TIP]
> **Correct answer: C. 153.6 Mbps**

## Solution

One frame contains 800×600=480,000 pixels. At 8 bits per pixel, that is 3,840,000 bits per frame. At 40 frames per second, the stream requires 3,840,000×40=153,600,000 bits/s=153.6 megabits/s, using the decimal network-rate unit 1 Mbps=10^6 bits/s.

## Key Points

- Uncompressed video rate = width × height × bits per pixel × frames per second.

## Why the other options are incorrect

15.36 Mbps misses a factor of 10, 2.4 Mbps omits major factors from colour depth or frame rate, and 1536 Mbps adds an extra factor of 10.
