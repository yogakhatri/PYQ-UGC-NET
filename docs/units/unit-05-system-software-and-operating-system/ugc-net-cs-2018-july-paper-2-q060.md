# Question 60

*UGC NET CS · 2018 July Paper 2 · CPU Scheduling · Preemptive versus Non-preemptive Scheduling*

In which of the following scheduling criteria, context switching will never take place ?

- **1.** ROUND ROBIN
- **2.** Preemptive SJF
- **3.** Non-preemptive SJF
- **4.** Preemptive priority

> [!TIP]
> **Correct answer: 3. Non-preemptive SJF**

## Solution

Among the listed policies, non-preemptive SJF never forces the running process off the CPU because a shorter job arrives; the selected process keeps the CPU until it terminates or blocks. Round robin preempts at each time-quantum expiry, while preemptive SJF and preemptive priority may switch when a more eligible process arrives. The intended answer is therefore option 3.

## Key Points

- Non-preemptive scheduling does not involuntarily replace a running process; completion/blocking transitions still require dispatching another process.

## Why the other options are incorrect

All three other policies explicitly permit preemption and hence scheduling-driven context switches. Strictly speaking, even a non-preemptive scheduler still performs a context switch after a process finishes or blocks; the question's phrase `never` should be read as `never due to preemption while the process remains runnable`.
