# Question 149

*UGC NET CS · 2019 June Paper 1 And 2 · Artificial Neural Networks · Sigmoid Activation Functions*

For the sigmoid function f(x)=1/(1+e^(-2x)), what is f'(0)?

- **1.** 0
- **2.** 1
- **3.** 1/2
- **4.** infinity

> [!TIP]
> **Correct answer: 3. 1/2**

## Solution

For f(x)=1/(1+e^(-2x)), differentiation gives f'(x)=2e^(-2x)/(1+e^(-2x))^2, equivalently 2f(x)[1-f(x)]. At x=0, f(0)=1/(1+1)=1/2. Hence f'(0)=2(1/2)(1/2)=1/2.

## Key Points

- For logistic f(x)=1/(1+e^(-kx)), f'(x)=k f(x)(1-f(x)); at zero the slope is k/4.

## Why the other options are incorrect

The sigmoid is smooth with a finite, nonzero slope at the origin, ruling out 0 and infinity. The value 1 would result from missing the product f(0)[1-f(0)].
