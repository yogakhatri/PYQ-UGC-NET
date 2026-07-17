# Question 57

*UGC NET CS · 2020 Nov With Answers · Pipeline and Vector Processing · Pipeline Throughput and Speedup*

A non-pipelined system takes 50 ns to process one task. A six-segment pipeline processes the same task with a 10 ns clock cycle. Approximately what speedup does the pipeline achieve for 500 tasks?

- **1.** 6
- **2.** 4.95
- **3.** 5.7
- **4.** 5.5

> [!TIP]
> **Correct answer: 2. 4.95**

## Solution

The non-pipelined time for 500 tasks is 500×50=25,000 ns. A k-stage pipeline completes n tasks in k+n−1 clock cycles, including fill time. Here the time is (6+500−1)×10=5,050 ns. Speedup=25,000/5,050≈4.9505, so the closest option is 4.95, option 2.

## Key Points

- Finite pipeline time is (stages+tasks−1)×cycle time; compare it with tasks×nonpipeline time.

## Why the other options are incorrect

Six is the stage count, not the speedup; the original system takes only 50 ns while the pipeline's steady interval is 10 ns, so the limiting speedup is 5, not 6. Values 5.7 and 5.5 exceed that physical upper limit.
