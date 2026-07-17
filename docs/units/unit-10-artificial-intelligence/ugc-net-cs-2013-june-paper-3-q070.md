# Question 70

*UGC NET CS · 2013 June Paper 3 · AI Search and Problem Solving · Water-Jug State Space*

Given two jugs of capacities 5 litres and 3 litres with no measuring markers on them. Assume that there is endless supply of water. Then the minimum number of states to measure 4 litres water will be

- **A.** 3
- **B.** 4
- **C.** 5
- **D.** 7

> [!TIP]
> **Correct answer: D. 7**

## Solution

Represent a state as (water in 5-L jug, water in 3-L jug). A shortest path is (0,0)→(5,0)→(2,3)→(2,0)→(0,2)→(5,2)→(4,3). The final state has exactly 4 litres in the 5-L jug. This path contains seven states, including the initial state, and breadth-first exploration confirms no shorter state path reaches a quantity of 4.

## Key Points

- In state-space problems, count nodes (including the start), not just operator applications along the path.

## Why the other options are incorrect

Three, four and five states do not allow enough fill, pour and empty transitions to isolate 4 litres using unmarked 5-L and 3-L jugs. Be careful that the path has six actions but seven states; the question asks for states.
