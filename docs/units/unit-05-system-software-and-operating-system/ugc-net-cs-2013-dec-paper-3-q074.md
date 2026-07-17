# Question 74

*UGC NET CS · 2013 Dec Paper 3 · Unix and Shell Programming · Background Job PID and Special Parameters*

Which command returns the process ID of a background sleep command?

- **A.** sleep 1 & echo $?
- **B.** sleep 1 & echo $#
- **C.** sleep 1 & echo $*
- **D.** sleep 1 & echo $!

> [!TIP]
> **Correct answer: D. sleep 1 & echo $!**

## Solution

The shell special parameter $! expands to the process ID of the most recent background pipeline. After starting sleep 1 in the background with &, echo $! prints that sleep job's PID. Thus the intended command is sleep 1 & echo $!.

## Key Points

- Shell special parameters: $!=last background PID, $$=shell PID, $?=last status, $#=argument count, $*=all arguments.

## Why the other options are incorrect

$? is the exit status of the most recent foreground pipeline, not a PID. $# is the number of positional parameters. $* expands the positional parameters. None identifies the latest background process.
