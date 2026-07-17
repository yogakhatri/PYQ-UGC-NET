# Question 19

*UGC NET CS · 2013 June Paper 3 · Data Communication · Image Transmission-Time Calculation*

An image is 1024 ∗800 pixels with 3 bytes/pixel. Assume the image is uncompressed. How long does it take to transmit it over a 10-Mbps Ethernet ?

- **A.** 196.6 seconds
- **B.** 19.66 seconds
- **C.** 1.966 seconds
- **D.** 0.1966 seconds

> [!TIP]
> **Correct answer: C. 1.966 seconds**

## Solution

The image contains 1024×800 pixels. At 3 bytes per pixel and 8 bits per byte, its size is 1024×800×3×8=19,660,800 bits. Using the nominal Ethernet rate 10 Mbps=10,000,000 bits/s, transmission time=19,660,800/10,000,000=1.96608 seconds, approximately 1.966 seconds.

## Key Points

- Transmission time = width × height × bytes/pixel × 8 / link bit rate.

## Why the other options are incorrect

19.66 and 196.6 seconds introduce one or two extra factors of 10. 0.1966 seconds omits a factor of 10. The calculation deliberately ignores headers, contention and interframe overhead as the question requests the raw uncompressed transfer time.
