# Question 78

*UGC NET CS · 2019 Dec Paper 1 And 2 · Deadlocks · Safe Sequences and Banker's Safety Test*

A system has 12 magnetic tape drives. At time t0, three processes have maximum needs and current allocations as follows: P0 maximum 10, current 5; P1 maximum 4, current 2; P2 maximum 9, current 2. Which is a safe sequence?

- **1.** P0, P1, P2
- **2.** P1, P0, P2
- **3.** P2, P1, P0
- **4.** P0, P2, P1

> [!TIP]
> **Correct answer: 2. P1, P0, P2**

## Solution

Initially 5+2+2=9 of the 12 drives are allocated, so Available=3. Remaining needs are P0:5, P1:2, P2:7. Only P1 can finish with 3 available; after it releases its allocation, Available=5. P0 can then finish and release 5, raising Available to 10, after which P2 can finish. The safe sequence is P1,P0,P2—option 2.

## Key Points

- Safety test: Need=Maximum−Allocation; finish an eligible process, add its allocation back to Available, and repeat.

## Why the other options are incorrect

Sequences beginning with P0 fail immediately because P0 still needs 5 while only 3 drives are available. A sequence beginning with P2 also fails because P2 still needs 7. Banker's safety test must find a process whose remaining need is no greater than the current Available value at every step.
