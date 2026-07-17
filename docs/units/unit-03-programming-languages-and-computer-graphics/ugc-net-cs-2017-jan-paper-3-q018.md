# Question 18

*UGC NET CS · 2017 Jan Paper 3 · Computer Graphics · DDA Line-Drawing Algorithm*

Consider a line AB with A = (0, 0) and B = (8, 4). Apply a simple DDA algorithm and compute the first four plots on this line.

- **1.** [(0, 0), (1, 1), (2, 1), (3, 2)]
- **2.** [(0, 0), (1, 1.5), (2, 2), (3, 3)]
- **3.** [(0, 0), (1, 1), (2, 2.5), (3, 3)]
- **4.** [(0, 0), (1, 2), (2, 2), (3, 2)]

> [!TIP]
> **Correct answer: 1. [(0, 0), (1, 1), (2, 1), (3, 2)]**

## Solution

For A=(0,0) and B=(8,4), Δx=8 and Δy=4. DDA takes steps=max(|8|,|4|)=8, so x increments by 8/8=1 and y by 4/8=0.5. The first four ideal samples are (0,0), (1,0.5), (2,1), and (3,1.5). Rounding each coordinate to the nearest raster pixel gives (0,0), (1,1), (2,1), and (3,2), which is option 1.

## Key Points

- DDA increments by (Δx/steps, Δy/steps) and rounds only for plotting; keep the accumulator fractional.

## Why the other options are incorrect

The other sequences use y increments inconsistent with the line's slope 4/8=0.5. DDA must preserve this fractional accumulator even though the displayed pixel coordinates are rounded.
