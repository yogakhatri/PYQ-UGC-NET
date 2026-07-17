# Question 39

*UGC NET CS · 2016 July Paper 2 · UNIX Commands · Creating Nested Directories with mkdir*

In UNIX, _________ creates three subdirectories : ‘PIS’ and two subdirectories ‘progs’ and ‘data’ from just created subdirectory ‘PIS’.

- **1.** mkdir PIS/progs PIS/data PIS
- **2.** mkdir PIS progs data
- **3.** mkdir PIS PIS/progs PIS/data
- **4.** mkdir PIS/progs data

> [!TIP]
> **Correct answer: 3. mkdir PIS PIS/progs PIS/data**

## Solution

The parent directory must exist before its children can be created. In `mkdir PIS PIS/progs PIS/data`, the first operand creates PIS, and the next two create progs and data inside it. The resulting hierarchy is PIS/{progs,data}, so option 3 is correct.

## Key Points

- Without `mkdir -p`, create a parent directory before naming child paths beneath it.

## Why the other options are incorrect

Option 1 tries to create PIS/progs and PIS/data before PIS exists. Option 2 creates PIS, progs, and data as three siblings in the current directory. Option 4 also addresses PIS/progs before creating PIS and places data at the current level.
