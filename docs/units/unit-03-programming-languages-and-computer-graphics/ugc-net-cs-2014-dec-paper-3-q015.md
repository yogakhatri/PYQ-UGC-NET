# Question 15

*UGC NET CS · 2014 Dec Paper 3 · Image Processing · Dithering and Halftone Approximation*

A technique used to approximate halftones without reducing spatial resolution i s known as _________.

- **A.** Halftoning
- **B.** Dithering
- **C.** Error diffusion
- **D.** None of the above

> [!TIP]
> **Correct answer: B. Dithering**

## Solution

Dithering approximates intermediate gray levels or colors by arranging available output levels in fine spatial patterns. The viewer integrates the pattern perceptually, so tonal variety increases without grouping pixels into larger halftone cells that would reduce spatial resolution.

## Key Points

- Dithering trades local intensity precision for fine-grained spatial patterns while preserving pixel-grid resolution.

## Why the other options are incorrect

Halftoning is the broader goal and traditional clustered-dot halftones trade spatial resolution for tone levels. Error diffusion is one particular dithering algorithm that propagates quantization error; the general technique named by the question is dithering. Therefore 'none' is false.
