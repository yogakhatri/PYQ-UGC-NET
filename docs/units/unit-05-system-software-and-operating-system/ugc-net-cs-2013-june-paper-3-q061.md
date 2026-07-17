# Question 61

*UGC NET CS · 2013 June Paper 3 · Process Synchronization and Deadlocks · Banker's Safety Algorithm*

An operating system using banker’s algorithm for deadlock avoidance has ten dedicated devices (of same type) and has three processes P1, P2 and P3 with maximum resource requirements of 4, 5 and 8 respectively. There are two states of allocation of devices as follows : State 1 Processes P1 P2 P3 Devices allocated 2 3 4 State 2 Processes P1 P2 P3 Devices allocated 0 2 4 Which of the following is correct ?

- **A.** State 1 is unsafe and state 2 is safe.
- **B.** State 1 is safe and state 2 is unsafe.
- **C.** Both, state 1 and state 2 are safe.
- **D.** Both, state 1 and state 2 are unsafe.

> [!TIP]
> **Correct answer: A. State 1 is unsafe and state 2 is safe.**

## Solution

There are 10 devices. In state 1, allocations are (2,3,4), so only 1 device is available; remaining needs are (2,2,4). No process can satisfy its remaining need with 1, so no safe sequence starts and state 1 is unsafe. In state 2, allocations are (0,2,4), leaving 4 available; needs are (4,3,4). P2 can finish first and release its 2 allocated devices, raising the work count to 6, after which P1 and P3 can finish. Thus state 2 is safe.

## Key Points

- A Banker state is safe only if repeated need≤work tests can produce a completion order for every process.

## Why the other options are incorrect

B reverses the two classifications. C overlooks that state 1 has no process with need≤available. D overlooks the safe sequence in state 2, such as P2→P1→P3.
