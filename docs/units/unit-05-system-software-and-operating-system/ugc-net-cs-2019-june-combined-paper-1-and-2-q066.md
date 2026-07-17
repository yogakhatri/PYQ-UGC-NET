# Question 66

*UGC NET CS · 2019 June Paper 1 And 2 · Storage Management · Disk seek time*

For a magnetic disk with concentric circular tracks, the seek latency is not linearly proportional to the seek distance due to

- **1.** non-uniform distribution of requests
- **2.** arm starting or stopping inertia
- **3.** higher capacity of tracks on the periphery of the platter
- **4.** use of unfair arm scheduling policies

> [!TIP]
> **Correct answer: 2. arm starting or stopping inertia**

## Solution

A disk arm must accelerate from rest, travel and then decelerate so that the head settles on the target track. These starting, stopping and settling components do not grow in direct proportion to the number of tracks crossed. Consequently seek latency is not a linear function of seek distance.

## Key Points

- Seek time is nonlinear because mechanical acceleration, deceleration and settling add distance-dependent overhead.

## Why the other options are incorrect

- **Option 1:** request distribution affects workload averages, not the mechanical time for a particular seek distance.
- **Option 3:** outer-track capacity does not create the seek-time nonlinearity.
- **Option 4:** scheduling changes request order, not the mechanics of one seek.
