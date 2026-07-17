# Question 51

*UGC NET CS · 2018 July Paper 2 · Process Synchronization · Counting-Semaphore P and V Operations*

At a particular time of computation, the value of a counting semapho re is 10. Then 12 P operations and “ x” V operations were performed on this semaphore. If the final value of semaphore is 7, x will be :

- **1.** 8
- **2.** 9
- **3.** 10
- **4.** 11

> [!TIP]
> **Correct answer: 2. 9**

## Solution

For a counting semaphore, each P (wait) operation decrements the count and each V (signal) operation increments it. Starting from 10, after 12 P operations and x V operations the value is 10−12+x. Equating this to the final value 7 gives x=9. Therefore option 2 is correct.

## Key Points

- Counting-semaphore balance: final=initial−number of P operations+number of V operations.

## Why the other options are incorrect

Substitution makes the alternatives easy to reject: x=8,10,11 would produce final counts 6,8,9 respectively. Do not reverse P and V: P consumes one available unit; V releases one.
