# Question 20

*UGC NET CS · 2018 July Paper 2 · Software Maintenance · Behavior-Preserving Refactoring*

Which statements are true? P: Refactoring changes a software system without altering external behavior while improving its internal architecture. Q: Adding a new feature after shipment is an example of refactoring.

- **1.** P only
- **2.** Q only
- **3.** Both P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 1. P only**

## Solution

P is the standard definition of refactoring: improve internal structure without changing observable behavior. Q is false because adding a feature intentionally changes external behavior and requirements coverage; it is an enhancement, not merely a refactor. Thus P only is true, giving option 1.

## Key Points

- Refactoring changes design, not functionality; tests help confirm behavior remains unchanged.

## Why the other options are incorrect

Options 2 and 3 misclassify feature development as refactoring, while option 4 rejects the correct definition in P. A team may refactor before or during feature work, but the refactoring steps themselves should preserve behavior.
