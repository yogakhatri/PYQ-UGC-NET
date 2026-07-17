# Question 79

*UGC NET CS · 2019 Dec Paper 1 And 2 · Processes and Threads · Message-Passing IPC*

Which of the following interprocess communication model is used to exchange messages among co-operative processes?

- **1.** Shared memory model
- **2.** Message passing model
- **3.** Shared memory and message passing model
- **4.** Queues

> [!TIP]
> **Correct answer: 2. Message passing model**

## Solution

In the message-passing IPC model, cooperating processes communicate by explicit send and receive operations. The operating system transfers or queues the messages without requiring the processes to share an address-space region. Since the question specifically asks for the model used to exchange messages, option 2 is correct.

## Key Points

- Two principal IPC models: shared memory exchanges data through common storage; message passing uses send/receive.

## Why the other options are incorrect

Shared-memory IPC communicates by reading and writing a common memory region, not by the model's explicit message exchange abstraction. Option 3 names both broad IPC models even though only one is the message-exchange model. A queue is one possible message-passing mechanism, not the general IPC model requested.
