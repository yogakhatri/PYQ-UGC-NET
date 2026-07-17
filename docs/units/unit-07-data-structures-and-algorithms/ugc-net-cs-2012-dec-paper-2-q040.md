# Question 40

*UGC NET CS · 2012 Dec Paper 2 · Data Structures · Stack Operations*

Given an empty stack, after performing push(1), push(2), Pop, push(3), push(4), Pop, Pop, push(5), Pop, what is the value at the top of the stack?

- **1.** 4
- **2.** 3
- **3.** 2
- **4.** 1

> [!TIP]
> **Correct answer: 4. 1**

## Solution

Track the stack from bottom to top. push(1), push(2) gives [1,2]; Pop leaves [1]. push(3), push(4) gives [1,3,4]; two Pops leave [1]. push(5) gives [1,5], and the final Pop again leaves [1]. Therefore the top element is 1.

## Key Points

- For stack traces, write the stack after every operation and remember LIFO: push adds at the top, Pop removes only the current top.

## Why the other options are incorrect

4 and 3 are removed by the two consecutive Pop operations, and 2 is removed by the first Pop. A stack is LIFO, so each Pop removes the most recently pushed element still present; no Pop removes the bottom 1 in this sequence.
