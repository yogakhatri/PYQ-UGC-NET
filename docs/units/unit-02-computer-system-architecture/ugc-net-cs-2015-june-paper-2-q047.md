# Question 47

*UGC NET CS · 2015 June Paper 2 · Multiprocessors and Multicomputers · PVM Message Passing and Ordering*

Which of the following statements is incorrect for Parallel Virtual Machine (PVM) ?

- **1.** The PVM communication model provides asynchronous blocking send, asynchronous blocking receive, and non-blocking receive function.
- **2.** Message buffers are allocated dynamically.
- **3.** The PVM communication model assumes that any task can send a message to any other PVM task and that there is no limit to the size or number of such messages.
- **4.** In the PVM model, message order is not preserved.

> [!TIP]
> **Correct answer: 4. In the PVM model, message order is not preserved.**

## Solution

PVM preserves point-to-point message order between the same sender and receiver: if task A sends message 1 and then message 2 to task B, message 1 arrives before message 2. Consequently, the statement that PVM does not preserve message order is incorrect, making option 4 the answer.

## Key Points

- PVM guarantees FIFO arrival order for messages sent successively between the same pair of tasks.

## Why the other options are incorrect

PVM provides asynchronous sends, blocking receives, and nonblocking receive facilities; it allocates message buffers dynamically; and its model permits tasks to message other PVM tasks with buffers sized dynamically subject to available resources. These are the intended true properties in options 1–3.
