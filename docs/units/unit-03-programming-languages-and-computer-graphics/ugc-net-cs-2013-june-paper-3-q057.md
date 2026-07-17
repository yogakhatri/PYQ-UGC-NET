# Question 57

*UGC NET CS · 2013 June Paper 3 · Computer Graphics and Image Processing · Digital Image Discretization*

If f( x, y) is a digital image, then x, y and amplitude values of f are

- **A.** Finite
- **B.** Infinite
- **C.** Neither finite nor infinite
- **D.** None of the above

> [!TIP]
> **Correct answer: A. Finite**

## Solution

A digital image is obtained by sampling spatial coordinates and quantizing amplitude. Thus x and y take values on a finite discrete pixel grid, while f(x,y) takes one of a finite number of intensity or color levels. Both the coordinate set and amplitude set are finite for a stored digital image.

## Key Points

- Digital imaging discretizes both space (sampling) and value (quantization).

## Why the other options are incorrect

Infinite or continuous coordinates/amplitudes describe an ideal analog image model. A digital array has a bounded number of samples and a bounded bit depth, so neither B nor C applies, and D is unnecessary.
