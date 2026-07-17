# Question 143

*UGC NET CS · 2019 June Paper 1 And 2 · Planning · STRIPS Representation*

The STRIPS representation is:

- **1.** a feature-centric representation
- **2.** an action-centric representation
- **3.** a combination of feature-centric and action-centric representations
- **4.** a hierarchical feature-centric representation

> [!TIP]
> **Correct answer: 2. an action-centric representation**

## Solution

STRIPS represents a planning domain mainly through actions or operators. Each action specifies preconditions that must hold, an add list of facts made true, and a delete list of facts made false. Planning searches for a sequence of these actions that transforms the initial state into a goal state, so the representation is action-centric.

## Key Points

- A STRIPS operator is summarized by preconditions, add effects and delete effects.

## Why the other options are incorrect

The other choices describe feature-centred or hierarchical representations. Although STRIPS states are sets of facts, its distinctive planning representation organizes change around action schemas rather than a feature hierarchy.
