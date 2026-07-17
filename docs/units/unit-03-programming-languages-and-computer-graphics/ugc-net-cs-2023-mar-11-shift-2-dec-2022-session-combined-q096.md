# Question 96

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · 2-D Geometrical Transforms and Viewing · Non-uniform scaling*

Given a vector with canesian components (xy), if scaling is dome with matrix Lo 1.5) which of the following are true. A. Decreases the vertical by three halves B. Increases the vertical by three halves C. Doubles the horizontal D. Halves the horizontal Choose the correct answer from the options given below:

- **1.** A and Conly
- **2.** A and Donly
- **3.** B and C only
- **4.** Band Donly

> [!TIP]
> **Correct answer: 4. Band Donly**

## Solution

Multiplying (x,y) by diag(0.5,1.5) gives (0.5x,1.5y). The horizontal component is halved (D) and the vertical component is increased to three halves of its original value (B).

## Key Points

- A diagonal 2-D scaling matrix directly lists the x- and y-scale factors.

## Why the other options are incorrect

A reverses the vertical effect, while C says the horizontal coordinate doubles instead of being multiplied by 0.5.
