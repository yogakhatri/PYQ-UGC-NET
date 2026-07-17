# Question 74

*UGC NET CS · 2019 Dec Paper 1 And 2 · Process Synchronization · Counting Semaphore Operations*

A counting semaphore is initialized to 8. Three wait() operations and four signal() operations are applied. Find the current value of the semaphore.

- **1.** 9
- **2.** 5
- **3.** 1
- **4.** 4

> [!TIP]
> **Correct answer: 1. 9**

## Solution

For a counting semaphore, wait() decrements the value and signal() increments it. Starting from 8, three waits give 8−3=5; four signals then give 5+4=9. No wait blocks because the value never reaches an unavailable state. Thus option 1.

## Key Points

- Counting semaphore arithmetic: final = initial − successful waits + signals.

## Why the other options are incorrect

Five is only the intermediate value after the waits. One and four result from treating operations as assignments or using the wrong direction. The net change is −3+4=+1, so the final value must be one greater than 8.
