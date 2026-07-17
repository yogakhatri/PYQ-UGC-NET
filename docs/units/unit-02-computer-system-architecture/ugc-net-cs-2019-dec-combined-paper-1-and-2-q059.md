# Question 59

*UGC NET CS · 2019 Dec Paper 1 And 2 · Pipeline and Vector Processing · Instruction Pipeline*

A non-pipelined system takes 30ns to process a task. The same task can be processed in a four-segment pipeline with a clock cycle of 10ns. Determine the speed up of the pipeline for 100 tasks.

- **1.** 3
- **2.** 4
- **3.** 3.91
- **4.** 2.91

> [!TIP]
> **Correct answer: 4. 2.91**

## Solution

Without pipelining, 100 tasks take 100×30=3000 ns. A k-stage pipeline needs k cycles for the first result and one additional cycle per later result, so n tasks take (k+n−1)T. Here that is (4+100−1)×10=1030 ns. Speedup=3000/1030≈2.91, giving option 4.

## Key Points

- Finite pipeline time is (stages + tasks − 1) × clock period; include fill latency before taking the speedup ratio.

## Why the other options are incorrect

A speedup of 3 is only the large-n limit 30/10; it ignores pipeline fill time. Four is the number of stages, not the speedup, because the non-pipelined task time is only three clock cycles. The value 3.91 cannot arise from the given execution times.
