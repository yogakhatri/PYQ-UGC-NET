# Question 75

*UGC NET CS · 2013 Dec Paper 3 · Windows Operating Systems · Thread States*

Possible thread states in Windows 2000 operating system include :

- **A.** Ready, running and waiting
- **B.** Ready, standby, running, waiting, transition and terminated
- **C.** Ready, running, waiting, transition and terminated
- **D.** Standby, running, transition and terminated

> [!TIP]
> **Correct answer: Intended answer: B, the most complete listed set: ready, standby, running, waiting, transition and terminated. As written with 'include,' the question is not uniquely worded because the shorter options also list genuine states.**

## Solution

The Windows dispatcher distinguishes Ready (able to run), Standby (selected to run next), Running, Waiting (blocked for an event/resource), Transition (ready except that a needed resource such as the kernel stack is not resident), and Terminated. Option B is the only offered list containing all six of these named states. Microsoft's enumeration also includes Initialized, so B should be read as the intended most complete choice among the options, not a mathematically exhaustive list.

## Key Points

- Windows adds dispatcher states such as Standby and Transition beyond the basic ready-running-waiting model.

## Why the other options are incorrect

A omits standby, transition and terminated; C omits standby; D omits ready and waiting. However, because the stem says states 'include' rather than asking for the complete list, each shorter option contains only valid state names, creating a wording defect.

## References

- [Microsoft Learn - System.Diagnostics ThreadState](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.threadstate?view=netframework-4.8.1)
