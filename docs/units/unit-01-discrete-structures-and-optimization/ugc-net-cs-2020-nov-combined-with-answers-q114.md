# Question 114

*UGC NET CS · 2020 Nov With Answers · Relations and Set Operations · Union, Intersection and Difference of Relations*

Let R₁={(1,1),(2,2),(3,3)} and R₂={(1,1),(1,2),(1,3),(1,4)}. Match: (A) R₁∪R₂, (B) R₁−R₂, (C) R₁∩R₂, (D) R₂−R₁ with (I) {(1,1),(1,2),(1,3),(1,4),(2,2),(3,3)}, (II) {(1,1)}, (III) {(1,2),(1,3),(1,4)}, (IV) {(2,2),(3,3)}.

- **1.** A-I, B-II, C-IV, D-III
- **2.** A-I, B-IV, C-III, D-II
- **3.** A-I, B-III, C-II, D-IV
- **4.** A-I, B-IV, C-II, D-III

> [!TIP]
> **Correct answer: 4. A-I, B-IV, C-II, D-III**

## Solution

The union contains every pair appearing in either relation, so A→I. Removing the common pair (1,1) from R₁ leaves {(2,2),(3,3)}, hence B→IV. The only common pair is (1,1), so C→II. Removing (1,1) from R₂ leaves {(1,2),(1,3),(1,4)}, hence D→III. The mapping A-I, B-IV, C-II, D-III is option 4.

## Key Points

- Treat a relation as a set of ordered pairs and apply ordinary union, intersection, and directional difference.

## Why the other options are incorrect

The distractors exchange intersection and one or both directional differences. Set difference is directional: R₁−R₂ and R₂−R₁ need not be the same.
