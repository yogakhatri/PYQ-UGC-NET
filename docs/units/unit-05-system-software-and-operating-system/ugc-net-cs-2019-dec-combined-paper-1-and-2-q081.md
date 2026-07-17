# Question 81

*UGC NET CS · 2019 Dec Paper 1 And 2 · Operating-System Services · Passing Parameters to System Calls*

Which of the following methods are used to pass any number of parameters to the operating system through system calls?

- **1.** Registers
- **2.** Block or table in main memory
- **3.** Stack
- **4.** Block in main memory and stack

> [!TIP]
> **Correct answer: 4. Block in main memory and stack**

## Solution

Registers can pass system-call arguments quickly, but their number is fixed and small. To support an arbitrary number of parameters, the process can place them in a block/table in memory and pass its address, or push them on the stack for the operating system to pop. Thus both the memory-block and stack methods meet the question's ‘any number’ requirement, giving option 4.

## Key Points

- System-call parameters may use registers, a referenced memory block, or a stack; only the latter two are not inherently limited by a fixed register count.

## Why the other options are incorrect

Option 1 is limited by the machine's available argument registers. Options 2 and 3 each name one valid scalable method but omit the other; the question asks which methods are used, and option 4 includes both.
