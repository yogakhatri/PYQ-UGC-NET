# Question 113

*UGC NET CS · 2019 Dec Paper 1 And 2 · Artificial Neural Networks · Gradient-Descent Weight Updates*

Let W_ij be a weight in a multilayer perceptron, E the output error, and α the learning rate (0≤α≤1). Which update rule performs gradient descent?

- **1.** W_ij(t+1) = W_ij(t) + α ∂E/∂W_ij
- **2.** W_ij(t+1) = W_ij(t) − α ∂E/∂W_ij
- **3.** W_ij(t+1) = α ∂E/∂W_ij
- **4.** W_ij(t+1) = −α ∂E/∂W_ij

> [!TIP]
> **Correct answer: 2. W_ij(t+1) = W_ij(t) − α ∂E/∂W_ij**

## Solution

The gradient ∂E/∂W_ij points in the direction of greatest local increase of error E. Gradient descent must move in the opposite direction by a step of size α. Hence W_ij(t+1)=W_ij(t)−α∂E/∂W_ij, which is option 2.

## Key Points

- Descent update = old parameter minus learning rate times error gradient.

## Why the other options are incorrect

Option 1 adds the gradient and therefore performs gradient ascent. Options 3 and 4 replace the current weight by a gradient term rather than adjusting it, discarding all previously learned weight information. A learning update must retain W_ij(t) and add a signed correction.
