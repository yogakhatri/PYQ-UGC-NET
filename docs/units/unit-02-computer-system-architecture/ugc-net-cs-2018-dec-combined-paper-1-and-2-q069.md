# Question 69

*UGC NET CS · 2018 Dec Paper 1 And 2 · Memory Hierarchy · Two-Level Cache Average Access Time*

A two-level cache has L1, L2 and main-memory access times of 0.5 ns, 5 ns and 100 ns, with L1 and L2 hit rates of 0.7 and 0.8. Ignoring search time within the cache, what is the average access time?

- **1.** 35.20 ns
- **2.** 7.55 ns
- **3.** 20.75 ns
- **4.** 24.35 ns

> [!TIP]
> **Correct answer: 2. 7.55 ns**

## Solution

There are three mutually exclusive outcomes. L1 serves 70% of requests: probability 0.7, time 0.5 ns. L1 misses and L2 hits with probability 0.3×0.8=0.24, time 5 ns. Both caches miss with probability 0.3×0.2=0.06, so main memory serves the request in 100 ns. Ignoring cache-search overhead as instructed, EAT=0.7(0.5)+0.24(5)+0.06(100)=0.35+1.20+6=7.55 ns. Therefore option 2.

## Key Points

- In a multilevel cache, multiply conditional hit/miss probabilities along each path, then take a probability-weighted time average.

## Why the other options are incorrect

The other results use unconditional L2 probabilities, fail to multiply successive miss probabilities, or add lookup times even though the question says to ignore cache-search time. The outcome probabilities correctly sum to 0.7+0.24+0.06=1.
