# Question 24

*UGC NET CS · 2016 July Paper 2 · Data Structures · Applications of Stacks*

Which of the following is not an inherent application of stack ?

- **1.** Implementation of recursion
- **2.** Evaluation of a postfix expression
- **3.** Job scheduling
- **4.** Reverse a string

> [!TIP]
> **Correct answer: 3. Job scheduling**

## Solution

Job scheduling normally needs a queue, priority queue, or heap so that jobs are selected by arrival order, priority, deadline, or another policy. LIFO order is not an inherent scheduling requirement, so job scheduling is the exception.

## Key Points

- Stacks serve nested/LIFO work; schedulers usually need FIFO or priority-based selection.

## Why the other options are incorrect

Recursive calls are stored on a call stack. Postfix evaluation pushes operands and pops them when an operator arrives. Pushing a string's characters and popping them reverses their order. These are direct, standard stack applications.
