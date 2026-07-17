# Question 66

*UGC NET CS · 2014 Dec Paper 3 · Image Processing · Butterworth Low-Pass Filter*

A Butterworth low-pass filter of order n has cutoff distance D₀ from the frequency origin. Which expression is its transfer function H(u,v), where D(u,v) is radial distance?

- **A.** 1 / (1 + [D(u,v)/D₀]²ⁿ)
- **B.** 1 / (1 + [D(u,v)/D₀]ⁿ)
- **C.** 1 / (1 + [D₀/D(u,v)]²ⁿ)
- **D.** 1 / (1 + [D₀/D(u,v)]ⁿ)

> [!TIP]
> **Correct answer: A. 1 / (1 + [D(u,v)/D₀]²ⁿ)**

## Solution

The nth-order Butterworth low-pass response is H(u,v)=1/{1+[D(u,v)/D₀]²ⁿ}. At the origin D=0, H=1, so low frequencies pass. At the cutoff D=D₀, H=1/2 in this image-processing transfer-function convention, and for D≫D₀ the response approaches 0. Option A has exactly this form and behavior.

## Key Points

- Low-pass sanity check: H(0)=1 and H(D→∞)=0; Butterworth order appears as exponent 2n.

## Why the other options are incorrect

B uses exponent n instead of 2n. C and D invert the ratio to D₀/D, producing high-pass-like behavior: their response approaches 0 near the origin and 1 at large distance. A alone is the low-pass formula.
