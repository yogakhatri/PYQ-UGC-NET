# Question 53

*UGC NET CS · 2018 Dec Paper 1 And 2 · Counting, Mathematical Induction and Discrete Probability · Hypergeometric Probability*

A box contains six red balls and four green balls. Four balls are selected at random from the box. What is the probability that two of the selected balls will be red and two will be green?

- **1.** 1/14
- **2.** 3/7
- **3.** 1/35
- **4.** 1/9

> [!TIP]
> **Correct answer: 2. 3/7**

## Solution

Choose 4 engineers from 10, where 6 are men and 4 are women. The total number of equally likely groups is C(10,4)=210. A group with exactly two men and two women can be chosen in C(6,2)C(4,2)=15×6=90 ways. Thus P(exactly two men)=90/210=3/7, so option 2 is correct.

## Key Points

- Sampling without replacement with category counts uses the hypergeometric ratio C(M,m)C(N−M,n−m)/C(N,n).

## Why the other options are incorrect

The remaining fractions do not equal the required favourable-to-total ratio. Multiplying C(6,2) by C(4,2) is necessary because both selections occur; dividing by C(10,4) avoids treating different orders of the same committee as different outcomes.
