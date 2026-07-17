# Question 119

*UGC NET CS · 2018 Dec Paper 1 And 2 · Process Synchronization · Readers-Writers Problem*

In the readers-writers problem, which statements are true? (i) Writers are given exclusive access to shared objects. (ii) Readers are given exclusive access to shared objects. (iii) Both readers and writers are given exclusive access to shared objects.

- **1.** (i) only
- **2.** (ii) only
- **3.** (iii) only
- **4.** Both (ii) and (iii)

> [!TIP]
> **Correct answer: 1. (i) only**

## Solution

In the readers-writers problem, a writer must have exclusive access: while it modifies the shared object, neither another writer nor any reader may access that object. Readers, however, may read concurrently with other readers because they do not modify it. Therefore (i) is true, while (ii) and (iii) are false; option 1 is correct.

## Key Points

- Many readers may coexist; a writer must be alone with respect to both readers and other writers.

## Why the other options are incorrect

Option 2 incorrectly makes each reader exclusive, destroying the concurrency the problem is designed to permit. Statement (iii) likewise claims that both classes always receive exclusive access, whereas only writers require exclusivity against all other access. Options 3 and 4 therefore fail.
