# Question 8

*UGC NET CS · 2018 July Paper 2 · Display Devices · Frame-Buffer Refresh Rate*

A graphic display system has a frame buffer 640 pixels wide, 480 pixels high and 1 bit deep. If the average access time for each pixel is 200 nanoseconds, the refresh rate is approximately:

- **1.** 16 frames per second
- **2.** 19 frames per second
- **3.** 21 frames per second
- **4.** 23 frames per second

> [!TIP]
> **Correct answer: 1. 16 frames per second**

## Solution

One frame contains 640×480=307,200 pixels. At 200 ns per pixel, scanning a frame takes 307,200×200 ns=61,440,000 ns=0.06144 s. Refresh rate is the reciprocal: 1/0.06144≈16.28 frames/s, which is approximately 16 frames/s. Hence option 1 is correct.

## Key Points

- Frame time = number of pixels × access time per pixel; refresh rate = 1/frame time.

## Why the other options are incorrect

The other rates correspond to shorter frame times than the stated per-pixel access permits. Color depth does not add another factor here because the question already gives the access time per pixel and the depth is one bit.
