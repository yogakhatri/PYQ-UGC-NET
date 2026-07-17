# Question 35

*UGC NET CS · 2009 Dec Paper 2 · Semantic Analysis · Inherited and Synthesized Attributes*

Synthesized attribute can be easily simulated by a

- **A.** LL grammar
- **B.** Ambiguous grammar
- **C.** LR grammar
- **D.** None of the above

> [!TIP]
> **Correct answer: C. LR grammar**

## Solution

A synthesized attribute at a parent is computed from attributes of its children. Bottom-up LR parsing completes/reduces the children before reducing their parent, so these values can be stored on the parse stack and combined naturally at reduction time.

## Key Points

- Synthesized values flow upward, matching bottom-up reductions.

## Why the other options are incorrect

Top-down LL parsing reaches a parent before its children are complete and is more naturally associated with inherited information. Ambiguity is unrelated to attribute evaluation.
