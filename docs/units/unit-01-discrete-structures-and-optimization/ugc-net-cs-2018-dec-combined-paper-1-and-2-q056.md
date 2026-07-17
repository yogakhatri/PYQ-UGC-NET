# Question 56

*UGC NET CS · 2018 Dec Paper 1 And 2 · Boolean Algebra · Order Relations in Boolean Algebras*

On a Boolean algebra, define x <= y iff x OR y = y; x < y iff x <= y but x != y; x >= y iff y <= x; and x > y iff y < x. Which of the following is not true? (i) If x <= y and y <= z, then x <= z. (ii) If x <= y and y <= x, then x = y. (iii) If x < y and y < z, then x <= y. (iv) If x < y and y < z, then x < y.

- **1.** (i) and (ii) only
- **2.** (ii) and (iii) only
- **3.** (iii) only
- **4.** (iv) only

> [!TIP]
> **Correct answer: No valid option: as printed, all four statements are true.**

## Solution

For a partially ordered set, x<y means x≤y and x≠y. Statement (i) is transitivity of the strict order: x<y and y<z imply x<z. Statement (ii) follows from antisymmetry: x≤y and y≤x imply x=y. In (iii), the premise already says x<y, so the conclusion x<y is immediate; (iv) repeats the same implication with x≤y and x≠y written explicitly. Thus none is a false statement, although the question asks for one.

## Key Points

- A strict order is transitive, while the associated non-strict partial order is antisymmetric; x<y is equivalent to x≤y with x≠y.

## Why the other options are incorrect

Options 1–4 each identify a true property as false. This is a defect in the printed question, not a reason to invent a different meaning for < or ≤.
