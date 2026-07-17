# Question 26

*UGC NET CS · 2013 Dec Paper 3 · Planning · Operator Subgoaling*

The mean-end analysis process centers around the detection of differences between the current state and goal state. Once such a difference is isolated, an operator that can reduce the difference must be found. But perhaps that operator can not be applied to the current state. So a sub-problem of getting to a state in which it can be applied is set up. The kind of backward chaining in which operators are selected and then sub goals are set up to establish the precondition of operators is called

- **A.** backward planning
- **B.** goal stack planning
- **C.** operator subgoaling
- **D.** operator overloading

> [!TIP]
> **Correct answer: C. operator subgoaling**

## Solution

Means-ends analysis chooses an operator that would reduce the current-goal difference. If its preconditions are not satisfied, establishing those preconditions becomes a new subgoal. This backward-chaining pattern is called operator subgoaling.

## Key Points

- Operator subgoaling turns an unavailable operator's preconditions into intermediate goals.

## Why the other options are incorrect

Backward planning and goal-stack planning are broader planning approaches. Operator overloading is a programming-language feature and has nothing to do with planning preconditions.
