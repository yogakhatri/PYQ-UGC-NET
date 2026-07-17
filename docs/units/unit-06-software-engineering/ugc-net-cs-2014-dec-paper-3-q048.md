# Question 48

*UGC NET CS · 2014 Dec Paper 3 · Software Design · Temporal Cohesion*

Temporal cohesion means

- **A.** Coincidental cohesion
- **B.** Cohesion between temporary variables
- **C.** Cohesion between local variables
- **D.** Cohesion with respect to time

> [!TIP]
> **Correct answer: D. Cohesion with respect to time**

## Solution

A module has temporal cohesion when its elements are grouped because they must execute at approximately the same time, such as several initialization operations or several shutdown operations. Their common bond is execution time, even if they perform different functions. Thus it is cohesion with respect to time.

## Key Points

- Temporal cohesion groups tasks by when they execute—typically initialization, cleanup, or another common phase.

## Why the other options are incorrect

Coincidental cohesion groups unrelated tasks and is weaker than temporal cohesion. 'Temporary variables' and 'local variables' concern variable lifetime or scope, not the reason module operations are grouped. D states the defining criterion.
