# Question 22

*UGC NET CS · 2017 Jan Paper 2 · Data Structures · Combined Stack and Queue Operations*

The seven elements A, B, C, D, E, F and G are pushed onto a stack in reverse order, i.e., starting from G. The stack is popped five times and each element is inserted into a queue. Two elements are deleted from the queue and pushed back onto the stack. Now, one element is popped from the stack. The popped item is ________.

- **1.** A
- **2.** B
- **3.** F
- **4.** G

> [!TIP]
> **Correct answer: 2. B**

## Solution

Pushing in reverse order gives the stack bottom-to-top as G,F,E,D,C,B,A. Five pops produce A,B,C,D,E, which enter the queue in that order; the stack then contains G,F with F on top. Dequeue A and push it, then dequeue B and push it. The stack is now G,F,A,B from bottom to top. The next pop therefore returns B, option 2.

## Key Points

- Write each container explicitly after every phase: stack reverses order; queue preserves order.

## Why the other options are incorrect

A was pushed back first and lies immediately below B. F was the old stack top before the two queue items were restored. G remains at the bottom throughout. Confusing FIFO queue order with LIFO stack order leads to the other choices.
