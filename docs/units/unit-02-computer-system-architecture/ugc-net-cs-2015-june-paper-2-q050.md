# Question 50

*UGC NET CS · 2015 June Paper 2 · Multiprocessors and Multicomputers · MPI Programming Model and Communicators*

Which of the following is not valid with reference to Message Passing Interface (MPI) ?

- **1.** MPI can run on any hardware platform.
- **2.** The programming model is a distributed memory model.
- **3.** All parallelism is implicit.
- **4.** MPI_Comm_size returns the total number of MPI processes in the specified communicator.

> [!TIP]
> **Correct answer: 3. All parallelism is implicit.**

## Solution

MPI uses explicit parallelism: the programmer starts or runs multiple processes, partitions work, and calls message-passing routines to communicate and synchronize. The system does not automatically infer all parallel work from an ordinary sequential program. Thus `All parallelism is implicit` is the invalid statement.

## Key Points

- MPI exposes explicit process-level parallelism; `MPI_Comm_size` reports the number of processes in a communicator.

## Why the other options are incorrect

MPI is designed as a portable interface with implementations on many hardware platforms, and it naturally supports a distributed-memory programming model. `MPI_Comm_size(comm, &size)` returns the number of processes in the group belonging to the specified communicator, so option 4 is valid.
