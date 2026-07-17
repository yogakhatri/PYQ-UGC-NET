# Question 9

*UGC NET CS · 2014 Dec Paper 3 · Database Recovery · Checkpointing*

_____ rules are used to limit the volume of log information that must be handled and processed after a system failure involving loss of volatile information.

- **A.** Write-ahead log
- **B.** Checkpointing
- **C.** Log buffer
- **D.** Thomas

> [!TIP]
> **Correct answer: B. Checkpointing**

## Solution

A checkpoint records a known recovery boundary and typically forces enough log/database state to stable storage that recovery need not scan and process the entire historical log. After a failure, the DBMS starts from the latest relevant checkpoint and handles only transactions active or logged after it, limiting recovery work.

## Key Points

- Checkpointing bounds recovery's log-processing horizon.

## Why the other options are incorrect

Write-ahead logging determines the safe ordering of log and data writes but does not by itself bound how far back recovery must scan. A log buffer is temporary staging. Thomas's write rule is a timestamp-ordering rule for obsolete writes, not a recovery-log truncation mechanism.
