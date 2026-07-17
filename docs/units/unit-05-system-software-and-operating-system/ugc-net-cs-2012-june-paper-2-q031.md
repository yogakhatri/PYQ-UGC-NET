# Question 31

*UGC NET CS · 2012 June Paper 2 · Deadlocks · Coffman Conditions*

Resources are allocated to the process on non-sharable basis is

- **A.** mutual exclusion
- **B.** hold and wait
- **C.** no pre-emption
- **D.** circular wait

> [!TIP]
> **Correct answer: A. mutual exclusion**

## Solution

Mutual exclusion means at least one resource is non-shareable: only one process may use an instance at a time. Another process requesting that occupied resource must wait. This is the Coffman condition described by the question.

## Key Points

- Non-shareable allocation is the mutual-exclusion condition for deadlock.

## Why the other options are incorrect

Hold and wait concerns retaining resources while requesting more. No pre-emption means resources cannot be forcibly taken. Circular wait describes a cycle of processes waiting on one another.
