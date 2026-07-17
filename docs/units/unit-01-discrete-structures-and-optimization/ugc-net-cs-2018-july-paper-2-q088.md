# Question 88

*UGC NET CS · 2018 July Paper 2 · Sets and Relations · Testing Equivalence Relations on Finite Sets*

Which of the relations on {0, 1, 2, 3} is an equivalence relation ?

- **1.** { (0, 0) (0, 2) (2, 0) (2, 2) (2, 3) (3, 2) (3, 3) }
- **2.** { (0, 0) (1, 1) (2, 2) (3, 3) }
- **3.** { (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) }
- **4.** { (0, 0) (0, 2) (2, 3) (1, 1) (2, 2) }

> [!TIP]
> **Correct answer: 2. { (0, 0) (1, 1) (2, 2) (3, 3) }**

## Solution

Option 2 is the identity relation {(0,0),(1,1),(2,2),(3,3)}. It is reflexive because every element is related to itself, symmetric because reversing any listed pair changes nothing, and transitive because composing identity pairs yields identity pairs. Hence it is an equivalence relation.

## Key Points

- An equivalence relation must be reflexive, symmetric, and transitive; test reflexivity first because it is often the quickest filter.

## Why the other options are incorrect

Option 1 omits (1,1), so it is not reflexive. Option 3 omits (2,2) and (3,3) and is also not fully symmetric/transitive. Option 4 omits (3,3) and lacks reverses such as (2,0), so it fails immediately.
