# Question 49

*UGC NET CS · 2010 June Paper 2 · File and Input/Output Systems · File-System Structure and Implementation*

At any given time Parallel Virtual Machine (PVM) has ________ send buffer and ________ receive buffer.

- **A.** one-one
- **B.** one-two
- **C.** two-two
- **D.** two-one

> [!TIP]
> **Correct answer: A. one-one**

## Solution

PVM may manage multiple message buffers, but at any given instant a task designates exactly one active send buffer and one active receive buffer. Packing/sending operates on the active send buffer; receiving/unpacking operates on the active receive buffer.

## Key Points

- Multiple buffers can exist, but PVM exposes one active buffer in each direction at a time.

## Why the other options are incorrect

Options B–D claim two simultaneously active buffers on one side, contrary to PVM's active-buffer model.
