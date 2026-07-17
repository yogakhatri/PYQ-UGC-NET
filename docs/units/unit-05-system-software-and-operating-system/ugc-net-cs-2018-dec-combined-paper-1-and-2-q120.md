# Question 120

*UGC NET CS · 2018 Dec Paper 1 And 2 · Deadlocks · Single-Resource Deadlock-Free Bound*

Suppose a system has 12 instances of some resource with n processes competing for that resource. Each process may require 4 instances of the resource. The maximum value of n for which the system never enters into deadlock is

- **1.** 3
- **2.** 4
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 1. 3**

## Solution

For n processes that can each need at most k identical resource instances, a sufficient worst-case deadlock-free condition is R≥n(k-1)+1. In the worst allocation before anyone finishes, each process may hold k-1 instances; one extra instance must remain so some process can obtain its kth instance, finish, and release everything. Here R=12 and k=4, so 12≥3n+1, giving n≤11/3. The greatest integer n is 3, option 1.

## Key Points

- Single resource type safety bound: R must exceed the total worst-case partial holdings n(k-1).

## Why the other options are incorrect

With four processes, each could hold three instances, consuming all 12 while every process waits for one more; deadlock is then possible. The same danger remains for 5 or 6 processes, so options 2–4 cannot guarantee that the system never deadlocks.
