# Question 68

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Basics of Operating Systems · Microkernel architecture*

BID: 87018 The main function of the microkernel is to provide a communication facility between the program and that are also running in user space.

- **1.** Virtual, Processes
- **2.** System, Processes
- **3.** Client, Services
- **4.** Virtual, Services

> [!TIP]
> **Correct answer: 3. Client, Services**

## Solution

In a microkernel architecture, many operating-system services execute as user-space server processes. The microkernel’s central job is to provide interprocess communication so that a client program can request those services. The blanks are therefore ‘client’ and ‘services.’

## Key Points

- A microkernel keeps only essential mechanisms in kernel space and connects user-space clients and service servers through IPC.

## Why the other options are incorrect

‘Virtual program’ is not the client/server terminology used for microkernels. Although the communicating entities are processes, the sentence specifically contrasts the client program with user-space services, making option 3 the precise completion.
