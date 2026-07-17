# Question 113

*UGC NET CS · 2018 Dec Paper 1 And 2 · OSI and TCP/IP Layer Functions · Session-Layer Services*

In the ISO-OSI reference model, the session layer offers dialog control, token management, and _____ as services.

- **1.** Synchronization
- **2.** Asynchronization
- **3.** Flow control
- **4.** Errors

> [!TIP]
> **Correct answer: 1. Synchronization**

## Solution

The OSI session layer manages conversations between application entities. Its classic services are dialog control, token management, and synchronization. Synchronization inserts checkpoints into a long exchange so that, after a failure, communication can resume from a known point rather than restarting the entire transfer. Hence option 1 is correct.

## Key Points

- Session layer: establish/manage dialogs, control whose turn it is with tokens, and recover using synchronization checkpoints.

## Why the other options are incorrect

Asynchronization is not the named OSI session-layer service. Flow control and error control are principally handled at lower layers such as data link and transport, not the missing member of this standard session-service trio.
