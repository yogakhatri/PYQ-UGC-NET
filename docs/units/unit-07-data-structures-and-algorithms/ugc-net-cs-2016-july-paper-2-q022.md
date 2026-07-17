# Question 22

*UGC NET CS · 2016 July Paper 2 · Data Structures · Stack Push, Pop, Underflow and Overflow*

Starting from an empty stack of capacity 5, perform: Push(a), Pop(), Push(b), Push(c), Pop(), Push(d), Pop(), Pop(), Push(e). What happens?

- **1.** Underflow occurs
- **2.** Stack operations are performed smoothly
- **3.** Overflow occurs
- **4.** None of the above

> [!TIP]
> **Correct answer: 2. Stack operations are performed smoothly**

## Solution

Track the stack sizes from zero: push a→1, pop→0, push b→1, push c→2, pop→1, push d→2, pop→1, pop→0, push e→1. The size never becomes negative and never exceeds the capacity 5, so every operation succeeds smoothly.

## Key Points

- For stack-safety questions, trace the size after every operation and compare it with 0 and capacity.

## Why the other options are incorrect

Underflow would require popping at size 0, which never occurs; the second consecutive pop removes b after d has already been removed. Overflow would require a sixth element, while the maximum size reached is only 2.
