# Question 48

*UGC NET CS · 2010 June Paper 2 · Multiprocessors · Interprocessor Communication and Synchronization*

CDMA Cell uses ________ carriers of 1.25 MHz.

- **A.** 9
- **B.** 18
- **C.** 22
- **D.** 64

> [!TIP]
> **Correct answer: D. 64**

## Solution

The intended IS-95 fact is that one 1.25-MHz CDMA forward carrier is channelized by 64 orthogonal Walsh codes, yielding 64 logical radio/code channels (including pilot, sync, paging, and traffic roles). Thus 64 is the intended count. The stem imprecisely calls these 'carriers'; technically it is one 1.25-MHz RF carrier containing up to 64 code channels.

## Key Points

- CDMA shares one wide RF carrier by orthogonal codes rather than assigning one separate carrier per user.

## Why the other options are incorrect

9, 18, and 22 are not the Walsh-code channelization count associated with an IS-95 1.25-MHz carrier.
