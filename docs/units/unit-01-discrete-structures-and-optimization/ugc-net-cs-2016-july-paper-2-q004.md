# Question 4

*UGC NET CS · 2016 July Paper 2 · Discrete Probability · Conditional Probability with Two-Sided Cards*

There are three cards in a box. Both sides of one card are black, both sides of one card are red, and the third card has one black side and one red side. We pick a card at random and observe only one side. What is the probability that the opposite side is the same colour as the one side we observed ?

- **1.** 3/4
- **2.** 2/3
- **3.** 1/2
- **4.** 1/3

> [!TIP]
> **Correct answer: 2. 2/3**

## Solution

Choose a card and the visible side uniformly. There are six equally likely face outcomes: two faces of BB, two of RR, and one black plus one red face of BR. For all four faces belonging to BB or RR, the opposite side has the same color; for the two faces of BR, it differs. Thus P(same opposite)=4/6=2/3.

## Key Points

- Count equally likely observed faces, not merely color labels or informal cases.

## Why the other options are incorrect

Treating the three card types as only two cases—same-color versus mixed—can tempt a 1/2 answer, but the same-color event contains two of the three equally likely cards. The six-face count makes the weighting explicit; 3/4 and 1/3 do not match it.
