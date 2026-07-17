# Question 52

*UGC NET CS · 2013 Dec Paper 3 · Memory Organization · Serial-Access Memory*

Serial access memories are useful in applications where

- **A.** Data consists of numbers
- **B.** Short access time is required
- **C.** Each stored word is processed differently.
- **D.** None of these

> [!TIP]
> **Correct answer: D. None of these**

## Solution

Serial-access memory is appropriate when records form an ordered stream and are processed sequentially, usually in the same manner. Its access time depends on how far the required item is from the current position, so it is not chosen for arbitrary fast access. None of the offered descriptions states the actual sequential-stream use case, making 'None of these' correct.

## Key Points

- Serial access follows storage order; use it for sequential streams, not rapid arbitrary lookup.

## Why the other options are incorrect

Whether data consists of numbers is irrelevant to the access method. Short access time is a strength of random-access memory, not serial access. Processing each word differently does not create a reason for sequential access; the usual application processes an ordered sequence uniformly or in turn.
