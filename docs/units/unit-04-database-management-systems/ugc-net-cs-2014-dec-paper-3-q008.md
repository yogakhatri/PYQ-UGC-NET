# Question 8

*UGC NET CS · 2014 Dec Paper 3 · Concurrency Control · Pessimistic 2PL and Optimistic Timestamp Ordering*

Which statements are correct? I. Two-phase locking is optimistic. II. Two-phase locking is pessimistic. III. Timestamp ordering is optimistic. IV. Timestamp ordering is pessimistic.

- **A.** I and III
- **B.** II and IV
- **C.** I and IV
- **D.** II and III

> [!TIP]
> **Correct answer: D. II and III**

## Solution

Two-phase locking acquires locks before conflicts occur and may make transactions wait; it is therefore pessimistic, making II true and I false. Timestamp-ordering protocols let operations proceed according to timestamps and abort/restart a transaction when an ordering conflict is detected; in the question's standard classification this is optimistic, making III true and IV false. Thus II and III are correct.

## Key Points

- Pessimistic control prevents conflicts with locks; optimistic-style timestamp ordering detects order violations and aborts.

## Why the other options are incorrect

A labels 2PL optimistic. B labels timestamp ordering pessimistic. C gets both classifications reversed. D contains the correct pair.
