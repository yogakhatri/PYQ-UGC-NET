# Question 52

*UGC NET CS · 2019 June Paper 1 And 2 · Counting, Mathematical Induction and Discrete Probability · Stars-and-bars counting*

How many ways are there to place 8 indistinguishable balls into four distinguishable bins?

- **1.** 70
- **2.** 165
- **3.** 8C4
- **4.** 8P4

> [!TIP]
> **Correct answer: 2. 165**

## Solution

Let xi be the number of balls placed in bin i. We need the number of non-negative integer solutions of x1+x2+x3+x4=8. By the stars-and-bars formula, this is C(8+4-1,4-1)=C(11,3)=165. The balls are indistinguishable, but the four bins are distinguishable, so only the number assigned to each bin matters.

## Key Points

- Distributing n identical objects among r labelled boxes with empty boxes allowed gives C(n+r-1,r-1).

## Why the other options are incorrect

- **Option 1:** 70 is C(8,4), which is not the stars-and-bars count.
- **Option 3:** C(8,4) incorrectly chooses four objects from the balls.
- **Option 4:** permutations apply to distinguishable objects and ordered selections, not identical balls.

## Additional Information

If every bin had to receive at least one ball, substitute yi=xi-1 and count C(7,3)=35 instead.
