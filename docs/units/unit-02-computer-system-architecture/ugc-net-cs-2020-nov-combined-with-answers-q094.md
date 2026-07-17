# Question 94

*UGC NET CS · 2020 Nov With Answers · Multiprocessors · Shared-Memory Multiprocessor Characteristics*

Which statements about a multiprocessor system are true? (A) A multiprocessor system is controlled by one operating system. (B) In a multiprocessor system, multiple computers are connected by communication lines. (C) A multiprocessor system is classified as a multiple-instruction-stream, multiple-data-stream system.

- **1.** (A) only
- **2.** (A) and (B) only
- **3.** (A) and (C) only
- **4.** (B) and (C) only

> [!TIP]
> **Correct answer: 3. (A) and (C) only**

## Solution

A tightly coupled multiprocessor contains multiple processors that share system resources and are managed as one computer by a single operating system, so A is true. The processors can execute different instruction streams on different data, placing a general multiprocessor in Flynn’s MIMD class, so C is true. Statement B instead describes a loosely coupled multicomputer or distributed system whose independent computers communicate over links. Thus A and C only, option 3.

## Key Points

- Multiprocessor means tightly coupled processors under one OS; networked independent computers form a multicomputer/distributed system.

## Why the other options are incorrect

B confuses processors inside one shared system with autonomous computers joined by a communication network. Any option containing B is therefore wrong, while option 1 omits the valid MIMD classification.
