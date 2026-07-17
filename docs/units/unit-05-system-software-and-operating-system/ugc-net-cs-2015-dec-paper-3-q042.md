# Question 42

*UGC NET CS · 2015 Dec Paper 3 · Process Management · Atomic operations*

In an operating system, indivisibility of operation means :

- **1.** Operation is interruptible
- **2.** Race - condition may occur
- **3.** Processor cannot be pre-empted
- **4.** All of the above

> [!TIP]
> **Correct answer: 3. Processor cannot be pre-empted**

## Solution

An indivisible, or atomic, operation must appear to execute as one uninterruptible unit: no other execution can observe a partially completed state. In the paper's single-processor wording, this corresponds to preventing pre-emption during the critical operation, so option 3 is intended.

## Key Points

- Atomicity means all-or-nothing execution with no observable intermediate state.

## Why the other options are incorrect

‘Interruptible’ is the opposite of indivisible, and correct atomic execution prevents the race window rather than saying a race may occur. Hence ‘all’ cannot be true. Modern systems may implement atomicity with hardware primitives without globally disabling processor pre-emption; the essential property is indivisible visibility.
