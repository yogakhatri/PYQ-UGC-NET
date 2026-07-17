# Question 73

*UGC NET CS · 2017 Jan Paper 3 · Artificial Neural Networks · Supervised and Unsupervised Network Types*

Which of the following neural networks uses supervised learning ? (A) Multilayer perceptron (B) Self organizing feature map (C) Hopfield network

- **1.** (A) only
- **2.** (B) only
- **3.** (A) and (B) only
- **4.** (A) and (C) only

> [!TIP]
> **Correct answer: 1. (A) only**

## Solution

A multilayer perceptron is conventionally trained with labeled input-target pairs using backpropagation, so A is supervised. A self-organizing feature map uses competitive self-organization without target labels, so B is unsupervised. A classical Hopfield network stores patterns through an associative/Hebbian rule rather than learning labeled input-output mappings, so it is not classified as supervised in this taxonomy. Thus A only is correct, giving option 1.

## Key Points

- MLP/backpropagation uses targets; SOM self-organizes clusters; Hopfield is recurrent associative memory.

## Why the other options are incorrect

Option 2 selects the explicitly unsupervised SOM. Options 3 and 4 incorrectly add SOM or Hopfield to the supervised category used by the question.
