# Question 131

*UGC NET CS · 2019 Dec Paper 1 And 2 · Artificial Neural Networks · Learning Algorithms for Classification*

Consider the following learning algorithms: (a) logistic regression, (b) backpropagation, and (c) linear regression. Which option represents classification algorithms?

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (b) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 1. (a) and (b) only**

## Solution

Logistic regression is a classification method despite its name: it models a class probability, commonly with the logistic sigmoid, and converts that probability to a class using a threshold. Backpropagation is the learning procedure used to train multilayer neural networks; when the network's output represents class scores or probabilities, the trained network performs classification. Ordinary linear regression instead predicts a continuous numerical response by fitting a linear relationship. It is not, in its standard form, a classification algorithm. Consequently (a) and (b) only are the classification choices, so option 1.

## Key Points

- Logistic regression and classification neural networks predict classes; linear regression predicts continuous values.

## Why the other options are incorrect

Options 2, 3, and 4 include linear regression as a classifier. Thresholding a regression output can be improvised, but that does not make standard linear regression a classification algorithm, and it lacks the probability constraints of logistic regression.
