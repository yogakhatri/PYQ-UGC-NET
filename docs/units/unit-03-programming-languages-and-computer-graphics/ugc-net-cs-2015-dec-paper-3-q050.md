# Question 50

*UGC NET CS · 2015 Dec Paper 3 · Computer Graphics · Lossy and Lossless Compression*

Which of the following is not a lossy compression technique ?

- **1.** JPEG
- **2.** MPEG
- **3.** FFT
- **4.** Arithmetic coding

> [!TIP]
> **Correct answer: 4. Arithmetic coding**

## Solution

Arithmetic coding is an entropy-coding method: it represents a symbol sequence by a subinterval whose width reflects the symbols' probabilities. Decoding can recover the original symbol sequence exactly, so arithmetic coding is lossless. It is therefore the intended answer to 'not a lossy compression technique.'

## Key Points

- The transform does not create loss; quantization/discarding coefficients does.
- Arithmetic coding itself is lossless entropy coding.

## Why the other options are incorrect

Ordinary JPEG discards image information during quantization, and MPEG commonly uses lossy spatial and temporal coding. FFT is mathematically a reversible transform and is not, by itself, a complete compression method; it can be used inside transform-coding systems that become lossy when coefficients are quantized or discarded. Thus the wording makes option 3 technically debatable, but option 4 is the unambiguous lossless compression method and the expected exam answer.
