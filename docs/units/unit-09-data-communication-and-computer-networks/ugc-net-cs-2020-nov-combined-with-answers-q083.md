# Question 83

*UGC NET CS · 2020 Nov With Answers · Data-Link Layer Protocols · Stop-and-Wait Protocol*

Protocols in which the sender sends one frame and then waits for an acknowledgement before proceeding to the next frame are called

- **1.** Simplex protocols
- **2.** Unrestricted simplex protocols
- **3.** Simplex stop and wait protocols
- **4.** Restricted simplex protocols

> [!TIP]
> **Correct answer: 3. Simplex stop and wait protocols**

## Solution

In stop-and-wait operation, the sender transmits exactly one frame and pauses until it receives the acknowledgement for that frame. Only after the ACK arrives does it send the next frame. Under the terminology used in the question, this is the simplex stop-and-wait protocol, option 3.

## Key Points

- One outstanding frame followed by an ACK wait is the defining pattern of stop-and-wait.

## Why the other options are incorrect

An unrestricted simplex protocol assumes an ideal channel and does not require this per-frame waiting behavior. ‘Simplex protocol’ alone is too broad, while ‘restricted simplex protocol’ is not the standard name for the described acknowledgement-controlled scheme.
