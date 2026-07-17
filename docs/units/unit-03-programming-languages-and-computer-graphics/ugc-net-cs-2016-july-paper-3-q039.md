# Question 39

*UGC NET CS · 2016 July Paper 3 · Object-Oriented Programming · Aggregation versus Composition*

Which of the following statements is correct ?

- **1.** Aggregation is a strong type of association between two classes with full ownership.
- **2.** Aggregation is a strong type of association between two classes with partial ownership.
- **3.** Aggregation is a weak type of association between two classes with partial ownership.
- **4.** Aggregation is a weak type of association between two classes with full ownership.

> [!TIP]
> **Correct answer: 3. Aggregation is a weak type of association between two classes with partial ownership.**

## Solution

Aggregation is a weak whole-part association. The whole has only partial ownership, and the part can normally exist independently of it. Thus option 3 correctly describes aggregation.

## Key Points

- Aggregation=weak/shared whole-part relationship; composition=strong ownership and lifecycle dependence.

## Why the other options are incorrect

Strong association with full ownership describes composition: a composed part's lifecycle is controlled by the whole. Options 1, 2, and 4 combine the wrong association strength or ownership level.
