# Question 46

*UGC NET CS · 2012 Dec Paper 2 · Artificial Neural Networks · Backpropagation Learning*

Back propagation is a learning technique that adjusts weights in a neural network by propagating weight changes:

- **A.** Forward from source to sink
- **B.** Backward from sink to source
- **C.** Forward from source to hidden nodes
- **D.** Backward from sink to hidden nodes

> [!TIP]
> **Correct answer: B. Backward from sink to source**

## Solution

During the forward pass, activations move from input/source neurons through hidden layers to output/sink neurons. The loss is then differentiated using the chain rule, and error gradients propagate backward from the output layer toward the input layer. Those gradients determine the weight updates. Hence the defining direction of backpropagation is from sink to source.

## Key Points

- Neural-network cycle: activations flow forward; loss gradients flow backward from output/sink toward input/source.

## Why the other options are incorrect

Forward source-to-sink propagation computes predictions rather than backpropagating error. Stopping at hidden nodes describes only part of a pass and does not propagate gradients through the complete dependency chain. 'Backward from sink to hidden nodes' is therefore incomplete.
