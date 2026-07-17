# Question 29

*UGC NET CS · 2015 June Paper 3 · Data Communication · Nyquist Sampling and PCM Bit Rate*

Suppose a digitized voice channel is made by digitizing 8 kHz bandwidth analog voice signal. It is required to sample the signal at twice the highest frequency (two samples per hertz). What is the bit rate required, if it is assumed that each sample requires 8 bits ?

- **1.** 32 kbps
- **2.** 64 kbps
- **3.** 128 kbps
- **4.** 256 kbps

> [!TIP]
> **Correct answer: 3. 128 kbps**

## Solution

Nyquist sampling requires at least twice the highest signal frequency. For an 8 kHz maximum frequency, the sample rate is `2 × 8,000 = 16,000 samples/s`. With 8 bits per sample, bit rate is `16,000 × 8 = 128,000 bits/s = 128 kbps`.

## Key Points

- PCM bit rate = sampling rate × bits per sample; Nyquist sampling rate = 2 × highest frequency.

## Why the other options are incorrect

64 kbps would correspond to 8,000 samples/s at 8 bits and ignores the factor-of-two sampling requirement. The 32 and 256 kbps values undercount or double the stated calculation.
