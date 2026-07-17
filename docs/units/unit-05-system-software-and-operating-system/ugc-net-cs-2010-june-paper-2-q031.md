# Question 31

*UGC NET CS · 2010 June Paper 2 · System Software · Linking and Relocation*

In an absolute loading scheme, which loader function is accomplished by a loader ?

- **A.** Re-allocation
- **B.** Allocation
- **C.** Linking
- **D.** Loading

> [!TIP]
> **Correct answer: D. Loading**

## Solution

An absolute loader's task is deliberately simple: it reads absolute object code and places it into the exact memory addresses already specified. Thus the function actually performed by the loader is loading.

## Key Points

- Absolute loader = copy object words to predetermined addresses.

## Why the other options are incorrect

Allocation, linking, and relocation/address assignment must have been resolved before the absolute loader runs, by the programmer/translator toolchain.
