# Question 27

*UGC NET CS · 2013 June Paper 3 · Computer Graphics · Bresenham Line Drawing*

Bresenham line drawing algorithm is attractive because it uses

- **A.** Real arithmetic only
- **B.** Integer arithmetic only
- **C.** Floating point arithmetic
- **D.** Real and integer arithmetic

> [!TIP]
> **Correct answer: B. Integer arithmetic only**

## Solution

Bresenham's line algorithm maintains an integer decision/error variable. At each pixel step it updates that variable using additions and subtractions to choose between the two candidate pixels. It avoids slopes, multiplication by fractions and floating-point rounding, which made it fast and predictable on raster hardware.

## Key Points

- Bresenham rasterizes lines using an integer error accumulator and incremental updates.

## Why the other options are incorrect

Real arithmetic and floating-point arithmetic are precisely what Bresenham avoids. It does not require a mixture of real and integer calculations because the recurrence can be expressed entirely with integers.
