# Question 65

*UGC NET CS · 2015 June Paper 3 · Digital Image Processing · Interpixel Redundancy and Correlation*

The redundancy in images stems from :

- **1.** pixel decorrelation
- **2.** pixel correlation
- **3.** pixel quantization
- **4.** image size

> [!TIP]
> **Correct answer: 2. pixel correlation**

## Solution

Neighboring pixels in natural images tend to have similar intensity or color, so one pixel is statistically predictable from nearby pixels. This interpixel correlation means the raw representation repeats information and therefore contains redundancy that predictive and transform compression can remove.

## Key Points

- Correlation creates predictable repetition; compression seeks to decorrelate or encode only the prediction error.

## Why the other options are incorrect

Decorrelation is a compression objective: it removes redundancy rather than causing it. Quantization reduces the number of represented levels and introduces loss; image dimensions determine data volume but not statistical redundancy by themselves.
