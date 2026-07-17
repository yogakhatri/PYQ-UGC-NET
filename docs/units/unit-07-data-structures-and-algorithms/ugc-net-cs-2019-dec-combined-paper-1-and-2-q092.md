# Question 92

*UGC NET CS · 2019 Dec Paper 1 And 2 · Algorithm Design Techniques · FFT Polynomial Multiplication*

The time complexity to multiply two polynomials of degree n using Fast Fourier transform method is :

- **1.** Theta(n log n)
- **2.** Theta(n^2)
- **3.** Theta(n)
- **4.** Theta(log n)

> [!TIP]
> **Correct answer: 1. Theta(n log n)**

## Solution

FFT multiplication evaluates both degree-n polynomials at O(n) suitably chosen points using two FFTs, multiplies corresponding values in O(n), and applies an inverse FFT to recover the coefficients. Each FFT takes Theta(n log n), which dominates the pointwise multiplication. Total time is Theta(n log n), option 1.

## Key Points

- Polynomial multiplication via FFT: transform, pointwise multiply, inverse transform—overall Theta(n log n).

## Why the other options are incorrect

Theta(n²) is the straightforward coefficient-by-coefficient method. Theta(n) would not cover the FFT transforms, and Theta(log n) is below even the time needed to read or output n coefficients.
