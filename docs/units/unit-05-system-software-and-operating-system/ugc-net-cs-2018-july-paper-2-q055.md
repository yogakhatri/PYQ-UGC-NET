# Question 55

*UGC NET CS · 2018 July Paper 2 · File and Input/Output Systems · UNIX chmod Permissions*

Which UNIX/Linux command is used to make all files and sub-direct ories in the directory “progs” executable by all users ?

- **1.** chmod− R a +x progs
- **2.** chmod −R 222 progs
- **3.** chmod−X a +x progs
- **4.** chmod −X 222 progs

> [!TIP]
> **Correct answer: 1. chmod− R a +x progs**

## Solution

`chmod -R a+x progs` changes permissions recursively (`-R`) for the directory `progs` and everything below it. The symbolic mode `a+x` adds (`+`) execute (`x`) permission for all user classes (`a`: owner, group, and others). Therefore option 1 is correct.

## Key Points

- `chmod -R a+x directory` means recursively add execute permission for everyone.

## Why the other options are incorrect

Numeric mode `222` grants write-only permission, not execute permission. `-X` is not the recursive traversal option; uppercase `X` is a conditional execute-permission symbol when used inside a mode, and the printed options 3 and 4 also put it in the wrong role.
