# Question 66

*UGC NET CS · 2016 July Paper 3 · Artificial Neural Networks · Perceptron Activation and Threshold*

A perceptron has input weights W1 = – 3.9 and W2 = 1.1 with threshold value T = 0.3. What output does it give for the input x1 = 1.3 and x2 = 2.2 ?

- **1.** – 2.65
- **2.** – 2.30
- **3.** 0
- **4.** 1

> [!TIP]
> **Correct answer: 3. 0**

## Solution

First compute the weighted input: W₁x₁+W₂x₂=(−3.9)(1.3)+(1.1)(2.2)=−5.07+2.42=−2.65. A binary perceptron with threshold T=0.3 outputs 1 only when the weighted input reaches or exceeds 0.3; otherwise it outputs 0. Since −2.65<0.3, the output is 0, option 3.

## Key Points

- Separate the two stages: calculate the weighted sum, then apply the threshold activation.

## Why the other options are incorrect

−2.65 is the net input before the activation function, not the perceptron's binary output. −2.30 results from incorrectly adding the threshold to the net value. Output 1 would require the threshold test to succeed.
