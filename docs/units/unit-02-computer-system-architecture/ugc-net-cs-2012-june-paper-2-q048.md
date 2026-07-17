# Question 48

*UGC NET CS · 2012 June Paper 2 · Pipeline and Vector Processing · Instruction Prefetch*

The pipelining strategy is used to implement:

- **A.** instruction execution
- **B.** instruction prefetch
- **C.** instruction decoding
- **D.** instruction manipulation

> [!TIP]
> **Correct answer: B. instruction prefetch**

## Solution

Instruction prefetch overlaps fetching later instructions with decoding or executing earlier ones, forming the first/simple stages of an instruction pipeline. While one instruction proceeds downstream, the fetch unit keeps the pipeline supplied. This overlap increases throughput, so 'instruction prefetch' is the intended named strategy among the choices.

## Key Points

- Pipelining overlaps stages of successive instructions; prefetch keeps later instructions ready before current execution finishes.

## Why the other options are incorrect

Execution, decoding and manipulation are individual activities, not the specific overlapping fetch strategy named by the item. A full instruction pipeline includes them, but the option that captures the cited strategy is prefetch.
