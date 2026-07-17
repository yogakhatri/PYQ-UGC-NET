# Question 34

*UGC NET CS · 2014 Dec Paper 2 · System Software and Debugging · Debugger Capabilities*

Debugger is a program that

- **A.** allows to examine and modify the contents of registers
- **B.** does not allow execution of a segment of program
- **C.** allows to set breakpoints, execute a segment of program and di splay contents of register
- **D.** All of the above

> [!TIP]
> **Correct answer: Both A and C are true; C is the more complete description, but the question does not have a unique correct option.**

## Solution

A debugger normally lets a user inspect—and on many systems modify—registers, so A is true. It also supports breakpoints, stepping or continuing through a program segment, and displaying register state, so C is true and more comprehensive. B is false because controlled execution is a core debugger function. Consequently D cannot be true because 'all' includes B.

## Key Points

- Debugger capabilities include controlled execution, breakpoints, and inspection/modification of machine state.

## Why the other options are incorrect

B states the opposite of a debugger's execution-control capability. D includes false B. The remaining problem is not conceptual but format: both A and C correctly describe debugger features, so the stem should have asked for the best or most complete description.
