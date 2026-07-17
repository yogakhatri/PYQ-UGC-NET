# Question 59

*UGC NET CS · 2015 June Paper 3 · Approaches to AI · Comparing Heuristic Search Techniques*

Match the following with respect to heuristic search techniques : List - I List - II (a) Steepest - accent Hill Climbing (i) Keeps track of all partial paths which can be candidate for further exploration (b) Branch - and - bound (ii) Discover problem state(s) that satisfy a set of constraints (c) Constraint satisfaction (iii) Detects difference between current state and goal state (d) Means - end - analysis (iv) Considers all moves from current state and selects best move Codes : (a) (b) (c) (d)

- **1.** (i) (iv) (iii) (ii)
- **2.** (iv) (i) (ii) (iii)
- **3.** (i) (iv) (ii) (iii)
- **4.** (iv) (ii) (i) (iii)

> [!TIP]
> **Correct answer: 2. (iv) (i) (ii) (iii)**

## Solution

Steepest-ascent hill climbing evaluates all immediate moves and chooses the best: (a)–(iv). Branch-and-bound retains candidate partial paths for later exploration: (b)–(i). Constraint satisfaction seeks assignments or states satisfying all constraints: (c)–(ii). Means–ends analysis detects differences between the current and goal states and chooses operators to reduce them: (d)–(iii). The sequence is `(iv),(i),(ii),(iii)`.

## Key Points

- Hill climbing picks the best neighbor; B&B maintains candidates; CSP satisfies constraints; means–ends reduces goal differences.

## Why the other options are incorrect

Every other code swaps at least two characteristic behaviors. Matching constraint satisfaction with constraints and means–ends with current/goal differences immediately fixes the last two entries and points to option 2.
