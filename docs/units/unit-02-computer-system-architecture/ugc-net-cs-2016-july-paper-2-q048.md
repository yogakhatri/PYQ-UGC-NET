# Question 48

*UGC NET CS · 2016 July Paper 2 · Processor Organization · Pipelining and Instruction-Level Parallelism*

Pipelining improves performance by :

- **1.** decreasing instruction latency
- **2.** eliminating data hazards
- **3.** exploiting instruction level parallelism
- **4.** decreasing the cache miss rate

> [!TIP]
> **Correct answer: 3. exploiting instruction level parallelism**

## Solution

A pipeline overlaps different stages of several instructions—for example, one instruction can execute while the next decodes and another fetches. This overlap exploits instruction-level parallelism and improves throughput after the pipeline fills. Therefore option 3 is correct.

## Key Points

- Pipelining improves instruction throughput by overlapping stages; it does not guarantee lower single-instruction latency.

## Why the other options are incorrect

Pipelining does not necessarily reduce the latency of one instruction; pipeline registers can even add overhead. It does not eliminate data hazards—stalling, forwarding, or scheduling must handle them. Cache miss rate is a property of the memory hierarchy and access pattern, not reduced merely by pipelining.
