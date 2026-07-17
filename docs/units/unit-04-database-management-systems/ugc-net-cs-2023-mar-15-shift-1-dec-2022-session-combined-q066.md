# Question 66

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Warehousing and Data Mining · Decision-tree rule conversion*

Stoption 1D=457631 I. No.1 BID:8701 If we convert a decision tree to a set of logical rules, then:

- **1.** The internal nodes in a branch are connected by AND and branches by AND
- **2.** The internal nodes in a branch are connected by OR and branches by OR
- **3.** The internal nodes in a branch are connected by AND and branches by OR
- **4.** The internal nodes in a branch are connected by OR and branches by AND

> [!TIP]
> **Correct answer: 3. The internal nodes in a branch are connected by AND and branches by OR**

## Solution

All tests along one root-to-leaf branch must hold together, so they are joined by AND. Different branches offer alternative sufficient paths to a class, so branch rules are joined by OR.

## Key Points

- Decision-tree path = conjunction; set of paths to a class = disjunction.

## Why the other options are incorrect

The other choices reverse conjunction within a path or disjunction among alternative paths.
