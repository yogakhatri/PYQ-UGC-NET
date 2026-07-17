# Question 36

*UGC NET CS · 2012 Dec Paper 2 · CPU Scheduling · UNIX nice Command*

In UNIX, which command is used to set task priority?

- **1.** init
- **2.** nice
- **3.** kill
- **4.** ps

> [!TIP]
> **Correct answer: 2. nice**

## Solution

The UNIX nice command starts a process with an adjusted niceness value, which influences its scheduling priority. A larger nice value generally means the process is more willing to yield CPU time and therefore receives lower scheduling priority. Existing processes may be adjusted with renice on systems that provide it.

## Key Points

- UNIX scheduling cue: nice starts a command with adjusted niceness; higher niceness usually means lower CPU priority.

## Why the other options are incorrect

init is the traditional system-initialization process, kill sends signals to processes, and ps displays process information. None of those commands is specifically used to set the task's niceness/priority value.
