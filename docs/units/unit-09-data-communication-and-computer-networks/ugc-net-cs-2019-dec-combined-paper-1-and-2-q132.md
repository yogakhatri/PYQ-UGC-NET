# Question 132

*UGC NET CS · 2019 Dec Paper 1 And 2 · OSI and TCP/IP Layer Functions · Layer Responsibilities*

Match List I with List II. List I: A. Physical layer; B. Transport layer; C. Session layer; D. Presentation layer. List II: I. provides token-management service; II. transmits raw bits over a communication channel; III. handles the syntax and semantics of transmitted information; IV. is the true end-to-end layer from source to destination.

- **1.** A-II, B-IV, C-III, D-I
- **2.** A-IV, B-III, C-II, D-I
- **3.** A-II, B-IV, C-I, D-III
- **4.** A-IV, B-I, C-II, D-III

> [!TIP]
> **Correct answer: 3. A-II, B-IV, C-I, D-III**

## Solution

Match each OSI layer by its defining responsibility. The physical layer transmits raw bits over the communication medium, so A-II. The transport layer provides process-to-process, end-to-end delivery from source to destination, so B-IV. The session layer establishes and controls dialogues and includes token management, so C-I. The presentation layer handles the representation, syntax, and semantics of exchanged information, including translation and encoding, so D-III. The complete mapping A-II, B-IV, C-I, D-III is option 3.

## Key Points

- OSI mnemonic by function: Physical=bits, Transport=end to end, Session=dialogue/token, Presentation=syntax and representation.

## Why the other options are incorrect

Option 1 swaps the session and presentation duties. Options 2 and 4 wrongly assign raw-bit transmission away from the physical layer and end-to-end delivery away from transport. Layer names should be tied to their scope: bits, end-to-end delivery, dialogue control, then representation.
