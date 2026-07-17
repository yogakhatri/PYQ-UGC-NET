# Question 52

*UGC NET CS · 2015 June Paper 3 · Process Management · Dining Philosophers as a Classical IPC Problem*

The Dining Philosophers problem is a:

- **1.** Producer - consumer problem
- **2.** Classical IPC problem
- **3.** Starvation problem
- **4.** Synchronization primitive

> [!TIP]
> **Correct answer: 2. Classical IPC problem**

## Solution

Dining Philosophers is one of the classical interprocess-communication and synchronization problems. Competing processes need multiple shared resources, exposing mutual exclusion, deadlock, and fairness issues. Therefore `classical IPC problem` is the best classification.

## Key Points

- Dining Philosophers models coordination for multiple shared resources and tests deadlock/starvation avoidance.

## Why the other options are incorrect

Producer-consumer is a different classical problem. A poor dining-philosophers solution may cause starvation, but starvation is a possible failure, not the problem's category. A synchronization primitive is a mechanism such as a semaphore, mutex, or monitor, not an illustrative problem.
