# Question 64

*UGC NET CS · 2015 Dec Paper 3 · Artificial Neural Networks · Perceptron Decision Boundaries*

A two-class task has C₁={(-1,-1),(-1,1),(1,-1)} and C₂={(1,1)}. Which line can be the decision boundary of a single perceptron separating C₁ from C₂?

- **1.** x₁ − x₂ − 0.5 = 0
- **2.** −x₁ + x₂ − 0.5 = 0
- **3.** 0.5(x₁ + x₂) − 1.5 = 0
- **4.** x₁ + x₂ − 0.5 = 0

> [!TIP]
> **Correct answer: 4. x₁ + x₂ − 0.5 = 0**

## Solution

Test the discriminant f(x₁,x₂)=x₁+x₂−0.5. At the only C₂ point (1,1), f=1.5>0. At the three C₁ points, the values are −2.5, −0.5, and −0.5, all negative. The line f=0 therefore places C₂ on one side and every C₁ point on the other, so it is a valid single-perceptron decision boundary.

## Key Points

- Verify a proposed linear boundary by evaluating its discriminant at every labeled point and checking opposite class signs.

## Why the other options are incorrect

The x₁−x₂ and −x₁+x₂ boundaries give different signs to members of C₁ and do not isolate (1,1). For option 3, 0.5(x₁+x₂)−1.5 is negative even at (1,1), so all four training points lie on the same side.
