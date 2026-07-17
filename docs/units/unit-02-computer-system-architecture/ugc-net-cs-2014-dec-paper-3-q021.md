# Question 21

*UGC NET CS · 2014 Dec Paper 3 · Multiprocessors · MPI Blocking and Nonblocking Communication*

Which of the following statements is not true ?

- **A.** MPI_Isend and MPI_Irecv are nonblocking message-passing routines of MPI.
- **B.** MPI_Issend and MPI_Ibsend are nonblocking message-passing routines of MPI.
- **C.** MPI_Send and MPI_Recv are nonblocking message-passing routines of MPI.
- **D.** MPI_Ssend and MPI_Bsend are blocking message-passing routines of MPI.

> [!TIP]
> **Correct answer: C. MPI_Send and MPI_Recv are nonblocking message-passing routines of MPI.**

## Solution

The `I` in MPI_Isend, MPI_Irecv, MPI_Issend, and MPI_Ibsend denotes the immediate/nonblocking form, so A and B are true. MPI_Send and MPI_Recv are blocking routines: the call does not return until MPI's completion condition for the user buffer is met, although a matching peer operation need not always have completed. Thus C is the statement that is not true. MPI_Ssend and MPI_Bsend are blocking-mode send calls, making D true.

## Key Points

- MPI routine names beginning with `MPI_I` are nonblocking; `MPI_Send`, `MPI_Recv`, `MPI_Ssend`, and `MPI_Bsend` are blocking calls.

## Why the other options are incorrect

A and B correctly identify the nonblocking `I...` routines. D correctly classifies the blocking synchronous and buffered send variants. The common trap is to confuse a blocking standard send with a necessarily synchronous rendezvous; blocking describes call completion, not one fixed transport protocol.
