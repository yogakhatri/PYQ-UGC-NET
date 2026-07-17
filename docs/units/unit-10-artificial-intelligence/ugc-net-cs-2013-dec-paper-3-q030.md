# Question 30

*UGC NET CS · 2013 Dec Paper 3 · Artificial Neural Networks · Weighted Sum and Activation Function*

An artificial neuron receives n inputs x1, x2,...., xn with weights w1, w2,...., wn attached to the input links. The weighted sum ________ is computed to be passed on to a non-linear filter φ called activation function to release the output.

- **A.** Σ wi
- **B.** Σ xi
- **C.** Σ wi + Σ xi
- **D.** Σ wi ⋅ xi

> [!TIP]
> **Correct answer: D. Σ wi ⋅ xi**

## Solution

A neuron first forms the weighted input sum net=Σ(wi·xi), usually with an added bias. The activation function φ then maps this net value to the neuron's output.

## Key Points

- Artificial neuron: output=φ(Σwixi+b).

## Why the other options are incorrect

Summing weights alone ignores inputs, summing inputs alone ignores learned importance, and adding the two separate sums is not a dot product. Neural computation multiplies each input by its corresponding weight before summation.
