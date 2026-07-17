# Question 130

*UGC NET CS · 2019 Dec Paper 1 And 2 · Heuristic Search · Hill-Climbing Failure Modes*

Consider the following: (a) trapping at a local maximum, (b) reaching a plateau, and (c) traversal along a ridge. Which option represents shortcomings of the hill-climbing algorithm?

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (b) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

All three are standard difficulties of hill climbing. At a local maximum, every immediate neighbour looks worse even though a better state exists elsewhere, so the algorithm stops prematurely. On a plateau, many neighbours have the same evaluation, giving no preferred uphill direction and causing stagnation or an unproductive random walk. Along a ridge, improvement may require a sequence of moves or a diagonal move not represented by the available operators; individual local moves can appear flat or downhill, so progress becomes slow or impossible. Therefore (a), (b), and (c) are all shortcomings, which is option 4.

## Key Points

- Hill climbing sees only local improvement, making it vulnerable to local maxima, plateaus, and ridges.

## Why the other options are incorrect

Options 1–3 each exclude one genuine failure mode. Random restart can help with local maxima, sideways moves can help on plateaus, and richer operators or stochastic search can help traverse ridges, but none removes the fact that the condition is a limitation.
