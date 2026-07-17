# Question 45

*UGC NET CS · 2015 Dec Paper 2 · System Software · Program Loading*

The __________ transfers the executable image of a C++ program from hard disk to main memory.

- **1.** Compiler
- **2.** Linker
- **3.** Debugger
- **4.** Loader

> [!TIP]
> **Correct answer: 4. Loader**

## Solution

The loader reads an executable image from secondary storage, places its code and data into main memory, performs any required relocation/dynamic linking support, establishes the process image, and transfers control to its entry point. Therefore the loader performs the stated transfer.

## Key Points

- Compile source → link objects → load executable → run.

## Why the other options are incorrect

The compiler translates source code, the linker combines object modules and resolves symbols to create an executable, and the debugger observes or controls execution. None of them is the component whose primary job is loading the executable into memory.
