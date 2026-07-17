# Question 119

*UGC NET CS · 2020 Nov With Answers · Search Strategies · Branch-and-Bound, Hill Climbing, CSP and Means–Ends Analysis*

Match: (A) branch-and-bound, (B) steepest-ascent hill climbing, (C) constraint satisfaction, (D) means–ends analysis with (I) keeps track of partial paths that remain candidates for exploration, (II) detects differences between current and goal states, (III) finds states satisfying a set of constraints, (IV) considers all moves from the current state and selects the best.

- **1.** A-I, B-IV, C-III, D-II
- **2.** A-I, B-II, C-III, D-IV
- **3.** A-II, B-I, C-III, D-IV
- **4.** A-II, B-IV, C-III, D-I

> [!TIP]
> **Correct answer: 1. A-I, B-IV, C-III, D-II**

## Solution

Branch-and-bound maintains promising partial paths and their bounds for later exploration, so A→I. Steepest-ascent hill climbing evaluates the available successors and chooses the best improvement, so B→IV. Constraint satisfaction seeks assignments or states satisfying all stated constraints, so C→III. Means–ends analysis compares the current and goal states, identifies a difference, and selects an operator to reduce it, so D→II. Therefore option 1.

## Key Points

- Match each strategy to what it stores or compares: partial paths, neighbours, constraints, or current–goal differences.

## Why the other options are incorrect

The other options confuse the goal-difference mechanism of means–ends analysis with the best-neighbour selection of hill climbing, or replace branch-and-bound’s frontier of partial candidates.
