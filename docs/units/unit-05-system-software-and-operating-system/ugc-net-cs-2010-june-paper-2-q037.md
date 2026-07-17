# Question 37

*UGC NET CS · 2010 June Paper 2 · Memory Management · Swapping*

_____ synchronizes critical resources to prevent deadlock.

- **1.** P-operator
- **2.** V-operator
- **3.** Semaphore
- **4.** Swapping

> [!TIP]
> **Correct answer: 3. Semaphore**

## Solution

A semaphore is the synchronization object that controls concurrent access to critical resources. Its atomic wait/P and signal/V operations coordinate processes and can enforce mutual exclusion and resource-count limits.

## Key Points

- Semaphore state plus atomic P/V operations regulate access to shared resources.

## Why the other options are incorrect

P and V are operations on the semaphore, not the complete synchronization object. Swapping is memory/process management and does not protect a critical resource. Also, semaphores prevent races; avoiding deadlock still requires correct acquisition design.
