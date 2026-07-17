# Question 77

*UGC NET CS · 2019 June Paper 1 And 2 · Computer Graphics · Frame-buffer storage*

Consider a raster system with resolution 640 by 480. What size is frame buffer (in bytes) for this system to store 12 bits per pixel?

- **1.** 450 kilobytes
- **2.** 500 kilobytes
- **3.** 350 kilobytes
- **4.** 400 kilobytes

> [!TIP]
> **Correct answer: 1. 450 kilobytes**

## Solution

The frame has 640×480=307,200 pixels. At 12 bits per pixel it needs 307,200×12=3,686,400 bits, or 460,800 bytes. Dividing by 1024 gives 450 KiB, reported in the options as 450 kilobytes.

## Key Points

- Frame-buffer bytes = horizontal pixels × vertical pixels × bits per pixel ÷ 8.

## Why the other options are incorrect

The other capacities do not equal resolution × bits per pixel ÷ 8. In particular, treating 12 bits as 12 bytes would overestimate the storage drastically.
