# Question 2

*UGC NET CS · 2014 Dec Paper 3 · Interrupts and Privilege Modes · Software Interrupts for Supervisor Entry*

For switching from a CPU user mode to the supervisor mode following type of interrupt is most appropriate

- **A.** Internal interrupts
- **B.** External interrupts
- **C.** Software interrupts
- **D.** None of the above

> [!TIP]
> **Correct answer: C. Software interrupts**

## Solution

A user program deliberately enters supervisor mode through a controlled trap or system-call instruction. This is a software interrupt: the CPU saves user state, switches privilege level, vectors to a validated kernel handler and later returns safely to user mode.

## Key Points

- System call/trap is a controlled software interrupt that transfers execution from user mode to kernel mode.

## Why the other options are incorrect

External interrupts originate asynchronously from devices or timers. Internal interrupts/exceptions arise from processor-detected events such as faults, although terminology sometimes groups traps with them. For an intentional user-requested supervisor transition, software interrupt is the most appropriate listed category.
