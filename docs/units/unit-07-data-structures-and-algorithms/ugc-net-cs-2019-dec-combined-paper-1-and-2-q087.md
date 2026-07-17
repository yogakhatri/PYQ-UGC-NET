# Question 87

*UGC NET CS · 2019 Dec Paper 1 And 2 · Performance Analysis and Recurrences · Time and Space Complexity*

What is the worst case running time of Insert and Extract-min. in an implementation of a priority queue using an unsorted array? Assume that all insertions can be accomodated.

- **1.** Theta(1), Theta(n)
- **2.** Theta(n), Theta(1)
- **3.** Theta(1), Theta(1)
- **4.** Theta(n), Theta(n)

> [!TIP]
> **Correct answer: 1. Theta(1), Theta(n)**

## Solution

In an unsorted array with spare capacity, insertion appends the new item at the next free position, requiring Theta(1) time. Extract-min must inspect all n items because the smallest item could be anywhere, so finding it takes Theta(n); removal can then be completed without changing that asymptotic bound. The pair is Theta(1), Theta(n), option 1.

## Key Points

- Unsorted priority queue: cheap append, expensive search for the extremal element.

## Why the other options are incorrect

Theta(n),Theta(1) is the trade-off for a suitably sorted representation, not an unsorted one. Constant-time extract-min is impossible without separately maintaining the minimum, which the question does not specify. Insert need not scan the array, eliminating option 4.
