# Question 124

*UGC NET CS · 2018 Dec Paper 1 And 2 · Process Synchronization · Mutual Exclusion and Critical Sections*

Suppose P, Q and R are co-operating processes satisfying Mutual Exclusion condition. Then, if the process Q is executing in its critical section then

- **1.** Both P and R execute in their critical sections.
- **2.** Neither P nor R executes in its critical section.
- **3.** P executes in its critical section.
- **4.** R executes in its critical section.

> [!TIP]
> **Correct answer: 2. Neither P nor R executes in its critical section.**

## Solution

Mutual exclusion means at most one cooperating process may execute the protected critical section at a time. If Q is currently in its critical section, both P and R must remain outside their corresponding critical sections until Q exits. Therefore neither P nor R executes in its critical section, option 2.

## Key Points

- Mutual exclusion is the safety rule: no two cooperating processes occupy the protected critical region simultaneously.

## Why the other options are incorrect

Options 1, 3, and 4 place at least one additional process in a critical section concurrently with Q, directly violating the mutual-exclusion condition stated in the question.
