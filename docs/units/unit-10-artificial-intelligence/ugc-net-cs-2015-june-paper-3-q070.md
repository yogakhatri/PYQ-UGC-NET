# Question 70

*UGC NET CS · 2015 June Paper 3 · Artificial Neural Networks · Linear Decision Boundary for a Perceptron*

A two-class task has C1={(1,1.5),(1,−1.5)} and C2={(−2,2.5),(−2,−2.5)}. Which listed line is a valid decision boundary for a single perceptron?

- **1.** x1 + x2 + 1.5 = 0
- **2.** x1 + x2 − 1.5 = 0
- **3.** x1 + 1.5 = 0
- **4.** x1 − 1.5 = 0

> [!TIP]
> **Correct answer: 3. x1 + 1.5 = 0**

## Solution

All C1 points have x1=1 and all C2 points have x1=−2, so a vertical line with x-coordinate strictly between −2 and 1 separates them regardless of x2. Option 3 is `x1+1.5=0`, or `x1=−1.5`; C1 lies on its positive side and C2 on its negative side.

## Key Points

- Inspect invariant coordinates first: constant class-wise x1 values make a vertical separator immediate.

## Why the other options are incorrect

The two diagonal choices misclassify at least one extreme x2 point, and `x1−1.5=0` places both classes on the same side. The separating boundary is not mathematically unique—any vertical line between −2 and 1 works—but option 3 is the valid listed one.
