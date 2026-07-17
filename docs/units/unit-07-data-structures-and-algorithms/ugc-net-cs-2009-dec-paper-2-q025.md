# Question 25

*UGC NET CS · 2009 Dec Paper 2 · Performance Analysis and Recurrences · Time and Space Complexity*

A hash function f defined as f(key) = key mod 7, with linear probing used to resolve collisions. Insert the keys 37, 38, 72, 48, 98 and 11 into the table indexe d from 0 to 6. What will be the location of 11 ?

- **A.** 3
- **B.** 4
- **C.** 5
- **D.** 6

> [!TIP]
> **Correct answer: C. 5**

## Solution

Insert in order: 37→2, 38→3, 72 hashes to 2 and probes to 4, 48→6, and 98→0. Key 11 hashes to 4, finds it occupied by 72, and moves by linear probing to index 5. Thus 11 is stored at 5.

## Key Points

- Linear probing checks h(k),h(k)+1,… cyclically until the first empty slot.

## Why the other options are incorrect

Indices 3 and 4 are already occupied when 11 arrives, while index 6 is not reached because index 5 is the first free probe position.
