# Question 96

*UGC NET CS · 2019 June Paper 1 And 2 · Process Management · Counting semaphores*

At a particular time, the value of a counting semaphore is 7. Then 20 P (wait) operations and 15 V (signal) operations are completed on this semaphore. What is the resulting value?

- **1.** 28
- **2.** 12
- **3.** 2
- **4.** 42

> [!TIP]
> **Correct answer: 3. 2**

## Solution

Each completed P (wait) operation decreases the semaphore by one, while each completed V (signal) operation increases it by one. Starting from 7, the final value is 7-20+15=2.

## Key Points

- For completed counting-semaphore operations, final value = initial value - waits + signals.

## Why the other options are incorrect

The other values result from adding waits, ignoring signals or otherwise reversing the definitions of P and V.
