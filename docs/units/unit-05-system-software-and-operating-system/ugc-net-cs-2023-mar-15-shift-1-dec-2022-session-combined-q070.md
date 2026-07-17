# Question 70

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Threads · User-to-kernel thread mappings*

Degree of concurrency in thread can be arranged in the manner.

- **1.** one-to-one > many-to-one > many-to-many
- **2.** one-to-one > many-to-many > many-to-one
- **3.** many-to-many > many-to-one > one-to-one
- **4.** None of the above

> [!TIP]
> **Correct answer: 2. one-to-one > many-to-many > many-to-one**

## Solution

One-to-one maps each user thread to a kernel thread and permits the greatest parallelism. Many-to-many multiplexes user threads over multiple kernel threads and gives intermediate concurrency. Many-to-one maps all user threads to one kernel thread, so one blocking call blocks all and no multicore parallelism occurs. Order: one-to-one > many-to-many > many-to-one.

## Key Points

- Kernel-visible schedulable entities determine achievable thread concurrency.

## Why the other options are incorrect

Option 1 ranks many-to-one above many-to-many; option 3 reverses the ordering.
