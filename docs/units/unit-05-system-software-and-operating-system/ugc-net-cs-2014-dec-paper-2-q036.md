# Question 36

*UGC NET CS · 2014 Dec Paper 2 · CPU Scheduling · Two-Level Scheduling and Swapping*

Consider these justifications for two-level CPU scheduling: I. It is used when memory is too small to hold all ready processes. II. Its performance is the same as FIFO. III. It facilitates putting a set of processes into memory and choosing among that set. IV. It does not allow adjustment of the in-core process set. Which are true?

- **A.** I, III and IV
- **B.** I and II
- **C.** III and IV
- **D.** I and III

> [!TIP]
> **Correct answer: D. I and III**

## Solution

Two-level scheduling is useful when not all ready processes fit in memory: a long/medium-term level selects which processes remain in core, and the CPU scheduler chooses among that resident set. Therefore I and III are true. It need not behave like FIFO, so II is false. Its purpose includes changing the in-core set by swapping or admission decisions, making IV false.

## Key Points

- Two levels separate admission/residency decisions from short-term CPU selection.

## Why the other options are incorrect

A and C include false IV. B includes false II and omits true III. D alone contains exactly the two valid justifications.
