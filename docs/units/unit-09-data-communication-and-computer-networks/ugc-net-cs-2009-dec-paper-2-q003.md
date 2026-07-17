# Question 3

*UGC NET CS · 2009 Dec Paper 2 · OSI and TCP/IP Layer Functions · TCP/IP, OSI and Ethernet Framing*

If in an error detection and correction code a message M : “You are good students” is stored as M' : Youare areyou aregood goodare goodstudents studentsgood. Wha t is the space required to store M' in general ? (assume that ‘n’ is the length of M)

- **A.** 2n
- **B.** 3n
- **C.** 4n
- **D.** less than 4n

> [!TIP]
> **Correct answer: D. less than 4n**

## Solution

Let the message contain word blocks w₁,…,wₖ with total stored length n (ignoring unchanged separators). The encoding stores each adjacent pair in both orders. Interior blocks occur four times, but the first and last blocks occur only twice. Its length is 4n−2(|w₁|+|wₖ|), which is strictly less than 4n, although asymptotically Θ(n).

## Key Points

- Count how many times endpoint and interior message blocks are duplicated.

## Why the other options are incorrect

2n and 3n are not general totals because repetition depends on whether a block is an endpoint or interior. Exactly 4n overcounts the two endpoint blocks.
