# Question 39

*UGC NET CS · 2017 Nov Paper 2 · CPU Scheduling · Dispatcher and Dispatch Latency*

Which module gives control of the CPU to the process selected by the short-term scheduler?

- **1.** Dispatcher
- **2.** Interrupt
- **3.** Schedular
- **4.** Threading

> [!TIP]
> **Correct answer: 1. Dispatcher**

## Solution

The short-term scheduler chooses a ready process. The dispatcher performs the mechanism needed to run that choice: context switching, changing to user mode, and transferring control to the selected program's next instruction. Therefore option 1 is correct.

## Key Points

- Scheduler decides who runs; dispatcher makes the selected process run.
- The time required is dispatch latency.

## Why the other options are incorrect

An interrupt is an event that may cause control transfer, not the module that hands the CPU to the selected process. The scheduler makes the selection but does not perform the dispatch. Threading is an execution model, not this operating-system component.
