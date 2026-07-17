# Question 1

*UGC NET CS · 2017 Jan Paper 3 · Input-Output Organization · Synchronous and Asynchronous Interrupts*

Which of the following is an interrupt according to temporal relationship with system clock ?

- **1.** Maskable interrupt
- **2.** Periodic interrupt
- **3.** Division by zero
- **4.** Synchronous interrupt

> [!TIP]
> **Correct answer: 4. Synchronous interrupt**

## Solution

When interrupts are classified by their temporal relationship to the processor clock and instruction execution, the two broad classes are synchronous and asynchronous. A synchronous interrupt is caused by, and occurs at a defined point in, the execution of an instruction; division by zero is one example. The question asks for the interrupt class, not an example, so option 4 is correct.

## Key Points

- Classify interrupts along the dimension named in the stem: timing gives synchronous versus asynchronous; masking gives maskable versus non-maskable.

## Why the other options are incorrect

Maskable describes whether software or hardware can disable an interrupt, not its timing. Periodic describes how often an interrupt recurs. Division by zero is a cause of a synchronous exception, whereas the requested classification name is synchronous interrupt.
