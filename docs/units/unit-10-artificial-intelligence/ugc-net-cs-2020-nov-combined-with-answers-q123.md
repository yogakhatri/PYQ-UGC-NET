# Question 123

*UGC NET CS · 2020 Nov With Answers · Informed Search · Memory-Bounded Heuristic Search*

Match: (A) greedy best-first search, (B) A*, (C) recursive best-first search (RBFS), (D) SMA* with (I) linear space O(d), where d is solution depth, (II) can be incomplete because it may loop even in a finite state space without repeated-state control, (III) is optimal if an optimal solution is reachable within memory and otherwise returns the best reachable solution, (IV) has very high time and space requirements.

- **1.** A-II, B-IV, C-I, D-III
- **2.** A-II, B-III, C-I, D-IV
- **3.** A-III, B-II, C-IV, D-I
- **4.** A-III, B-IV, C-II, D-I

> [!TIP]
> **Correct answer: 1. A-II, B-IV, C-I, D-III**

## Solution

Greedy best-first search follows the smallest heuristic h and, without repeated-state control, may cycle even in a finite state space, so A→II. A* can require exponential memory as well as heavy computation because it retains a large frontier, so B→IV. RBFS emulates best-first search recursively using linear memory—more precisely O(bd), often written O(d) for fixed branching factor—so C→I. SMA* uses all available memory and is optimal when the optimal path fits; otherwise it returns the best solution reachable under the memory limit, so D→III. Hence option 1.

## Key Points

- A* stores the frontier, RBFS trades re-expansion for linear space, and SMA* makes best use of a fixed memory bound.

## Why the other options are incorrect

The alternatives misassign SMA*’s memory-bounded guarantee or RBFS’s linear-space property. A* is optimal under standard conditions, but its main practical weakness is memory consumption, not the SMA* guarantee.
