# Question 31

*UGC NET CS · 2013 June Paper 3 · Computer Graphics and Image Processing · Image Memory Calculation*

Images tend to be very large collection of data. The size of memory required for a 1024 by 1024 image in which the colour of each pixel is represented by a n-bit number, (in an 8 bit machines) is

- **A.** n × 8 MB
- **B.** n / 8 MB
- **C.** (1024 × 1024) / 8 MB
- **D.** 1024 MB

> [!TIP]
> **Correct answer: B. n / 8 MB**

## Solution

The image has 1024×1024 = 2²⁰ pixels. At n bits per pixel, it needs n×2²⁰ bits. An 8-bit machine stores eight bits per byte, so the size is (n×2²⁰)/8 bytes = n/8 megabytes when the question uses 2²⁰ bytes per MB. For example, an 8-bit image occupies 1 MB and a 24-bit image occupies 3 MB.

## Key Points

- Image storage = width × height × bits per pixel ÷ 8 bytes.

## Why the other options are incorrect

A multiplies by eight where conversion from bits to bytes requires division by eight. C omits the n-bit color depth. D gives a fixed size independent of the number of bits per pixel.
