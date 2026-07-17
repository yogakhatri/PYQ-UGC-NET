# Question 7

*UGC NET CS · 2021 Nov With Answers · Computer Graphics · Bresenham versus DDA Line Rasterization*

Which of the statements given below are correct? The midpoint (or Bresenham) algorithm for rasterizing lines is optimized relative to DDA algorithm in that A. it avoids round‐off operations. B. it is incremental. C. it uses only integer arithmetic. D. all straight lines can be displayed as straight (exact). Choose the correct answer from the options given below:

- **1.** A and B only
- **2.** A and C only
- **3.** A, B, C, and D
- **4.** A, B, and C only

> [!TIP]
> **Correct answer: 4. A, B, and C only**

## Solution

Bresenham maintains an incrementally updated decision/error variable, so B is true. Its update can be expressed entirely with integer additions and comparisons, avoiding the floating-point slope accumulation and per-pixel rounding associated with basic DDA; hence A and C are true. A raster has a discrete pixel grid, so most geometric lines appear as a staircase approximation rather than an exact continuous straight line; D is false. Thus A, B, and C only: option 4.

## Key Points

- Bresenham replaces floating-point rounding with an incremental integer decision variable; rasterization still approximates the ideal line.

## Why the other options are incorrect

Options 1 and 2 omit a real algorithm property. Option 3 incorrectly claims that finite square pixels can represent every continuous line exactly. DDA is also incremental, but Bresenham's integer incremental error update is the key optimization.
