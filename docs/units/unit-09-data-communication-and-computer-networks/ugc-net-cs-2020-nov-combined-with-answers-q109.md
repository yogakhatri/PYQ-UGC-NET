# Question 109

*UGC NET CS · 2020 Nov With Answers · Application Layer · POP Delete and Keep Modes*

Post Office Protocol (POP) is used by a client to retrieve mail. Which statements are true? (A) POP has delete and keep modes. (B) In delete mode, mail is deleted from the mailbox after retrieval. (C) In delete mode, mail is deleted before retrieval. (D) In keep mode, mail is deleted before retrieval. (E) In keep mode, mail remains in the mailbox after retrieval.

- **1.** (A) and (B) only
- **2.** (A), (D) and (E) only
- **3.** (A), (B), (C) and (D) only
- **4.** (A), (B) and (E) only

> [!TIP]
> **Correct answer: 4. (A), (B) and (E) only**

## Solution

In the textbook POP model, a client can operate in delete mode or keep mode, so A is true. Delete mode retrieves a message and arranges for it to be removed from the server mailbox after retrieval/session completion, making B true and C false. Keep mode leaves the server copy in the mailbox after the client retrieves it, so E is true and D is false. Thus A, B, and E only, option 4.

## Key Points

- Delete mode removes the server copy after download; keep mode leaves that copy available after download.

## Why the other options are incorrect

Option 1 omits the defining keep-mode behaviour E. Options 2 and 3 include D, which contradicts keep mode; option 3 also includes C, which incorrectly places deletion before retrieval.
