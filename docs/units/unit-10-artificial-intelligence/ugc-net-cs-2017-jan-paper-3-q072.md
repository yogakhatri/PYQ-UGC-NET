# Question 72

*UGC NET CS · 2017 Jan Paper 3 · Artificial Neural Networks · Weighted Input and Bias*

A neuron with 3 inputs has the weight vector [0.2 –0.1 0.1]T and a bias θ = 0. If the input vector is X = [0.2 0.4 0.2]T then the total input to the neuron is :

- **1.** 0.20
- **2.** 1.0
- **3.** 0.02
- **4.** –1.0

> [!TIP]
> **Correct answer: 3. 0.02**

## Solution

Total input is the dot product plus bias: w^T X+θ = (0.2)(0.2)+(−0.1)(0.4)+(0.1)(0.2)+0 = 0.04−0.04+0.02 = 0.02. Therefore option 3 is correct.

## Key Points

- Neuron pre-activation = weighted sum Σw_i x_i + bias, before applying any activation function.

## Why the other options are incorrect

The positive and negative middle contributions cancel; ignoring the negative sign or summing weights and inputs separately produces the larger distractors. The bias contributes nothing because θ=0.
