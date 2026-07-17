# Question 90

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Artificial Neural Networks · Linear neuron output*

A 4-input neuron has weights 1.2,3.4. The transfer function is linear with the constant of proportionality being equal to 3. The inputs are 5,7,10,30, respectively Then the output will be.

- **1.** 120
- **2.** 213
- **3.** 410
- **4.** 507

> [!TIP]
> **Correct answer: 4. 507**

## Solution

The net input is 1·5+2·7+3·10+4·30=5+14+30+120=169. The linear transfer function has proportionality constant 3, so the output is 3×169=507.

## Key Points

- A linear neuron computes y=kΣwᵢxᵢ (plus a bias only if one is specified).

## Why the other options are incorrect

The other values result from omitting weights, failing to sum all four products, or not applying the final factor of 3.
