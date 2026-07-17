# Question 115

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Artificial Neural Networks · Linear separability of Boolean functions*

Which Boolean operation on two variables can be represented by a single perception layer? A. XI AND X2 XI OR X2 C. XI NOR X2 D. XI XOR X2 Choose the most appropriate answer from the options given below:

- **1.** A and B Only
- **2.** B and COnly
- **3.** A, B and C Only
- **4.** A, B, C and D Only

> [!TIP]
> **Correct answer: 3. A, B and C Only**

## Solution

AND, OR, and NOR have linearly separable truth-table classes, so a single perceptron layer can implement them. XOR is not linearly separable and requires a hidden layer or transformed features.

## Key Points

- A single perceptron represents a linear decision boundary.

## Why the other options are incorrect

Options 1 and 2 omit a separable operation; option 4 incorrectly includes XOR.
