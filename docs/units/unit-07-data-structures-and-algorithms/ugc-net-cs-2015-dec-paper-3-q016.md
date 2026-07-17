# Question 16

*UGC NET CS · 2015 Dec Paper 3 · Greedy Algorithms · Activity Compatibility and Selection*

In the activity-selection problem, activity i has start time s_i and finish time f_i, with s_i≤f_i. Activities i and j are compatible if:

- **1.** s_i ≥ f_j
- **2.** s_j ≥ f_i
- **3.** s_i ≥ f_j or s_j ≥ f_i
- **4.** s_i ≥ f_j and s_j ≥ f_i

> [!TIP]
> **Correct answer: 3. s_i ≥ f_j or s_j ≥ f_i**

## Solution

Two activities are compatible exactly when their time intervals do not overlap. This happens if i starts after j finishes, s_i≥f_j, or j starts after i finishes, s_j≥f_i. Only one ordering needs to hold, so the connector is OR.

## Key Points

- Intervals are compatible when either one finishes before the other starts.

## Why the other options are incorrect

Options 1 and 2 cover only one of the two possible temporal orders. Option 4 demands both inequalities simultaneously, which is generally impossible for positive-duration activities and is much stronger than non-overlap.
