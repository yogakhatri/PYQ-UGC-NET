# Question 77

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Selected Topics · FFT polynomial multiplication*

option 1D=39404) I. No.2 3ID:18702 time procedure for multiplying two polynomials A(x) and B(x) of Given the FFT we can have degree bound n where input and output representations are in coefficient form, assuming n is a power of 2.

- **1.** 0(112 )
- **2.** O(n.log2n)
- **3.** 0(2)
- **4.** O(log2n)

> [!TIP]
> **Correct answer: 2. O(n.log2n)**

## Solution

FFT-based multiplication evaluates both degree-bounded polynomials at O(n) suitable points using FFTs, multiplies corresponding values in O(n), and applies an inverse FFT. Each FFT or inverse FFT costs O(n log n), which dominates the pointwise multiplication. The complete procedure is therefore O(n log₂n).

## Key Points

- FFT turns polynomial convolution from quadratic time into O(n log n) time.

## Why the other options are incorrect

O(n²) is the ordinary coefficient-by-coefficient multiplication cost. Exponential time is unnecessary, while O(log n) is too small even to read or write all n coefficients.
