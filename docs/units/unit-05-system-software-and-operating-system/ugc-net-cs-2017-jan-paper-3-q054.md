# Question 54

*UGC NET CS · 2017 Jan Paper 3 · Process Management · Traditional Unix init Process*

Which statement is not correct about “init” process in Unix ?

- **1.** It is generally the parent of the login shell.
- **2.** It has PID 1.
- **3.** It is the first process in the system.
- **4.** Init forks and execs a ‘getty’ process at every port connected to a terminal.

> [!TIP]
> **Correct answer: 3. It is the first process in the system.**

## Solution

In traditional Unix, the kernel's process 0 (the swapper/scheduler) exists before and creates the process that becomes init. Init has PID 1, starts getty processes for terminal lines, and becomes an ancestor or adoptive parent of login sessions and orphaned processes. Therefore saying init is the first process in the system is not correct; option 3 is the required answer.

## Key Points

- Classic Unix boot order distinguishes kernel process 0 from init, the first user-space process with PID 1.

## Why the other options are incorrect

Options 1, 2, and 4 describe the classic System V/BSD-era init model intended by the paper. Modern systems may use replacements such as systemd, but that does not change the historical Unix question.
