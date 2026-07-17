# Question 44

*UGC NET CS · 2013 June Paper 3 · Interrupts and Exceptions · Internal Interrupts*

Interrupt which arises from illegal or erroneous use of an instruction or data is

- **A.** Software interrupt
- **B.** Internal interrupt
- **C.** External interrupt
- **D.** All of the above

> [!TIP]
> **Correct answer: B. Internal interrupt**

## Solution

An illegal opcode, invalid operand use, divide-by-zero or similar execution fault is detected inside the CPU while it executes the current instruction. It therefore raises an internal interrupt, more commonly called an exception or trap. The saved machine state lets an operating-system handler diagnose, terminate or sometimes recover from the fault.

## Key Points

- Execution-detected errors are synchronous internal interrupts (exceptions), not asynchronous external interrupts.

## Why the other options are incorrect

A software interrupt is deliberately requested by executing a designated trap/system-call instruction rather than arising from erroneous use. An external interrupt comes asynchronously from hardware such as a timer or I/O device. Since those causes are distinct, 'all of the above' is incorrect.
