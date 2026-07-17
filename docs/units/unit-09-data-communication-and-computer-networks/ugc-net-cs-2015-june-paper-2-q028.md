# Question 28

*UGC NET CS · 2015 June Paper 2 · OSI and TCP/IP Layer Functions · Session-Layer Responsibilities*

Which of the following is not associated with the session layer ?

- **1.** Dialog control
- **2.** Token management
- **3.** Semantics of the information transmitted
- **4.** Synchronization

> [!TIP]
> **Correct answer: 3. Semantics of the information transmitted**

## Solution

The OSI session layer organizes the dialog between applications: it controls who may transmit, manages tokens, and inserts synchronization checkpoints so a disrupted exchange can resume. The meaning, representation, translation, compression, and encryption of transmitted information belong to the presentation layer. Therefore semantics is not a session-layer responsibility.

## Key Points

- Session layer manages the conversation; presentation layer manages the representation and meaning of data.

## Why the other options are incorrect

Dialog control, token management, and synchronization are the three standard textbook services associated with the session layer, so options 1, 2, and 4 do not satisfy the word `not`.
