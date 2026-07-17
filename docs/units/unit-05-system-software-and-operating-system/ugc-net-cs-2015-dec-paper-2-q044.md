# Question 44

*UGC NET CS · 2015 Dec Paper 2 · Operating-System Services · System Calls and Traps*

System calls are usually invoked by using :

- **1.** A privileged instruction
- **2.** An indirect jump
- **3.** A software interrupt
- **4.** Polling

> [!TIP]
> **Correct answer: 3. A software interrupt**

## Solution

A user program invokes a system call through a controlled trap into kernel mode, classically implemented as a software interrupt. The processor saves user context, transfers to the kernel's system-call handler, performs the service with privilege, and returns to user mode. Thus option 3 matches the conventional mechanism.

## Key Points

- System call = controlled software trap from user mode to kernel mode.

## Why the other options are incorrect

User code cannot simply execute an arbitrary privileged instruction. An indirect jump does not safely change privilege levels, and polling repeatedly checks state rather than entering the kernel. Modern architectures may use a dedicated `syscall`/`svc` instruction, but it serves the same trap-like transition.
