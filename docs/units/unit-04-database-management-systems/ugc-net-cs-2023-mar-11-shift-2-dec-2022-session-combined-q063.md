# Question 63

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Data Warehousing and Data Mining · Training and test error in overfitting*

OBID: 187013 Overfitting is expected when we observe that?

- **1.** With training iterations error on training set as well as test set decreases
- **2.** With training iterations error on training set decreases but test set increases
- **3.** With training iterations error on training set as well as test set increases
- **4.** With training iterations training set as well as test error remains constant

> [!TIP]
> **Correct answer: 2. With training iterations error on training set decreases but test set increases**

## Solution

Overfitting means the model continues to adapt to the training examples—including their noise—without improving generalization. Its training error therefore keeps decreasing while the error measured on unseen test/validation data begins to increase. That divergence is the classic observable warning sign.

## Key Points

- Monitor a validation curve: the point where validation error rises while training error falls marks the onset of overfitting.

## Why the other options are incorrect

If both errors decrease, generalization is still improving. If both increase, optimization itself is failing or the model is deteriorating. Constant errors indicate stalled learning, not specifically overfitting.
