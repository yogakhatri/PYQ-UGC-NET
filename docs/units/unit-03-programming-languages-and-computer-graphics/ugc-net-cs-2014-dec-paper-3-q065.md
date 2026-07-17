# Question 65

*UGC NET CS · 2014 Dec Paper 3 · Image Processing · Maximum First-Order Entropy*

A 10×10 image histogram has four symbol probabilities p₁=a, p₂=b, p₃=c, and p₄=d. When is the first-order image entropy maximum?

- **A.** a = 0, b = 0, c = 0, d = 1
- **B.** a=1/2, b=1/2, c=0, d=0
- **C.** a=1/3, b=1/3, c=1/3, d=0
- **D.** a=b=c=d=1/4

> [!TIP]
> **Correct answer: D. a=b=c=d=1/4**

## Solution

First-order entropy is H=−Σpᵢlog₂pᵢ. For a fixed alphabet of four symbols, entropy is maximized by the uniform distribution, pᵢ=1/4, giving H=−4(1/4)log₂(1/4)=2 bits per symbol. Thus a=b=c=d=1/4.

## Key Points

- For k possible symbols, maximum entropy is log₂k and occurs when every symbol has probability 1/k.

## Why the other options are incorrect

A has entropy 0 because only one symbol occurs. B has two equally likely symbols and entropy 1 bit. C has three equally likely symbols and entropy log₂3≈1.585 bits. All are below the four-symbol maximum of 2 bits in D.
