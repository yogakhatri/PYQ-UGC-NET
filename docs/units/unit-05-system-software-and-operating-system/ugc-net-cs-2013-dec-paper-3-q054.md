# Question 54

*UGC NET CS · 2013 Dec Paper 3 · Operating-System Interrupts · Synchronous Traps and Asynchronous Interrupts*

The essential difference between traps and interrupts is

- **A.** traps are asynchronous and interrupts are synchronous with the program.
- **B.** traps are synchronous and interrupts are asynchronous with the program.
- **C.** traps are synchronous and interrupts are asynchronous with the I/O devices.
- **D.** None of these.

> [!TIP]
> **Correct answer: B. traps are synchronous and interrupts are asynchronous with the program.**

## Solution

A trap is caused by the currently executing instruction or by a deliberately executed system-call instruction, so it occurs at a reproducible point in the program and is synchronous with program execution. A hardware interrupt is raised by an external event such as I/O completion or a timer, whose arrival is independent of the current instruction, so it is asynchronous with the program.

## Key Points

- Trap=internal and synchronous; hardware interrupt=external and asynchronous to the instruction stream.

## Why the other options are incorrect

A reverses the definitions. C compares interrupts with I/O devices rather than with program execution; an I/O device may itself generate an interrupt synchronously with its own event, but that event is asynchronous to the CPU program. Hence D is unnecessary because B states the distinction correctly.
