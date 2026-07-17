# Question 57

*UGC NET CS · 2019 June Paper 1 And 2 · Counting, Mathematical Induction and Discrete Probability · Pigeonhole Principle*

How many cards must be selected from a standard deck of 52 cards to guarantee that at least three hearts are present among them?

- **1.** 9
- **2.** 13
- **3.** 17
- **4.** 42

> [!TIP]
> **Correct answer: 4. 42**

## Solution

To delay obtaining three hearts as long as possible, select all 39 non-hearts and then two hearts. That gives 41 cards while still having only two hearts. The next selected card, the 42nd, must be a heart and therefore guarantees at least three hearts.

## Key Points

- For a guarantee problem, construct the largest possible selection that still avoids the required outcome, then add one.

## Why the other options are incorrect

- **Options 1, 2 and 3:** each allows a selection containing too few hearts because many non-heart cards remain available.
