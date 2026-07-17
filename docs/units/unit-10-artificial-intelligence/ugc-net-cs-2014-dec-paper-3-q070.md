# Question 70

*UGC NET CS · 2014 Dec Paper 3 · Artificial Neural Networks · Fixed Feature Detectors and Output-Layer Learning*

Consider these statements about a perceptron (printed as 'perception' in the source). I. A feature detector can be any function of the input parameters. II. The learning procedure adjusts only the connection weights to the output layer. Which option is correct?

- **A.** I is false and II is false.
- **B.** I is true and II is false.
- **C.** I is false and II is true.
- **D.** I is true and II is true.

> [!TIP]
> **Correct answer: D. I is true and II is true.**

## Solution

For the single-layer perceptron model intended here, the first-stage feature detectors gᵢ may be any fixed functions of the input pattern, so I is true. Training does not learn those feature functions; it changes the weights connecting their outputs to the final output unit/layer, so II is also true. Hence both statements hold.

## Key Points

- In the classical perceptron formulation, feature extraction is fixed and learning modifies the final linear decision weights.

## Why the other options are incorrect

A rejects both defining observations. B incorrectly says output-layer weights are not the learned parameters. C incorrectly restricts the fixed feature detector. The result applies to this fixed-feature single-layer perceptron description, not to a general multilayer neural network whose hidden weights may also be trained.
