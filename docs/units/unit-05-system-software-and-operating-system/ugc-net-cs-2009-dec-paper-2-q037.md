# Question 37

*UGC NET CS · 2009 Dec Paper 2 · Memory Management · Page Replacement*

A page fault

- **A.** is an error specific page.
- **B.** is an access to the page not currently in memory.
- **C.** occur when a page program occur in a page memory.
- **D.** page used in the previous page reference.

> [!TIP]
> **Correct answer: B. is an access to the page not currently in memory.**

## Solution

A page fault occurs when a process references a virtual page that is not currently resident in physical memory. The operating system must locate/load it (or reject the access if invalid) before the instruction can continue.

## Key Points

- Valid virtual address + absent resident page triggers a page fault.

## Why the other options are incorrect

A page fault is not inherently a programming error, nor is it defined by the previous reference or the vague occurrence descriptions in the other choices.
