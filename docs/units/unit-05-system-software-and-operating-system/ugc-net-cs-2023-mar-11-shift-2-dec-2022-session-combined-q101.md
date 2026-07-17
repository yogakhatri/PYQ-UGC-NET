# Question 101

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · CPU Scheduling · Multiple-Processor Scheduling*

Which of the following statements are true? A. Shortest remaining time first scheduling may cause starvation B. Preemptive scheduling may cause starvation C. Round robin is better than FFS in terms of response time Choose the correct answer from the options given below:

- **1.** Aonly
- **2.** B. C only
- **3.** A, B only
- **4.** A, B, C

> [!TIP]
> **Correct answer: 4. A, B, C**

## Solution

SRTF can indefinitely postpone a long job when shorter jobs keep arriving, so A is true. Priority-based preemptive policies can likewise starve low-priority work, so B's ‘may’ is true. Round robin gives every ready process an early time slice and normally improves interactive response time over FCFS, so C is true.

## Key Points

- Preemption improves responsiveness but does not itself guarantee freedom from starvation.

## Why the other options are incorrect

Options 1–3 omit at least one true statement.
