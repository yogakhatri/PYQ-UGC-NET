# Question 38

*UGC NET CS · 2014 Dec Paper 2 · Process Synchronization · Critical-Section Requirements*

Which of the following conditions does not hold good for a solution to a cri tical section problem ?

- **A.** No assumptions may be made about speeds or the number of CPUs.
- **B.** No two processes may be simultaneously inside their critical secti ons.
- **C.** Processes running outside its critical section may block other process es.
- **D.** Processes do not wait forever to enter its critical section.

> [!TIP]
> **Correct answer: C. Processes running outside its critical section may block other process es.**

## Solution

A correct critical-section solution requires mutual exclusion, progress and bounded waiting without relying on relative process speeds or CPU count. A process executing outside its critical section must not prevent eligible contenders from deciding who enters. Statement C says it may block them, directly violating progress, so it is the condition that should not hold.

## Key Points

- Critical-section requirements: mutual exclusion, progress, bounded waiting and no timing assumptions.

## Why the other options are incorrect

A is the standard no-timing-assumption requirement. B states mutual exclusion. D states freedom from indefinite waiting/bounded waiting. All three are desired properties.
