# Question 54

*UGC NET CS · 2016 July Paper 3 · Distributed Systems · Remote Procedure Calls*

Suppose that the time to do a null remote procedure call (RPC) (i.e. 0 data bytes) is 1.0 msec, with an additional 1.5 msec for every 1K of data. How long does it take to read 32 K from the file server as 32 1K RPCs ?

- **1.** 49 msec
- **2.** 80 msec
- **3.** 48 msec
- **4.** 100 msec

> [!TIP]
> **Correct answer: 2. 80 msec**

## Solution

Each 1 K RPC pays both the fixed null-call cost and the data-transfer cost: 1.0 ms + 1.5 ms = 2.5 ms. The file is requested as 32 separate calls, so the total time is 32 × 2.5 ms = 80 ms. Hence option 2 is correct.

## Key Points

- For many small RPCs, total time = number of calls × (fixed cost per call + payload cost per call).

## Why the other options are incorrect

48 ms counts only 32 × 1.5 ms and omits all call overhead. 49 ms adds the fixed overhead only once, which would correspond to one 32 K call under a different cost interpretation. The question explicitly says 32 one-kilobyte RPCs, so the 1 ms setup cost occurs 32 times.
