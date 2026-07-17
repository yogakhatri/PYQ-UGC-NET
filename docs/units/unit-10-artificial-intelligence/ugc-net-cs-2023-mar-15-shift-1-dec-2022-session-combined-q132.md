# Question 132

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Approaches to AI · Best-first search*

Consider the graph given below. What is the order in which the nodes mentioned in the options are to be traversed to find the shortest path from A to Z using best first search? 10 2 15 N 6 A. Node-A B. Node-B C. Node-C D. Node-D E. Node-E F. Node-F Choose the correct answer from the options given below:

- **1.** A→C→F→D→E
- **2.** A-C→E→B
- **3.** A-C→F→E→B
- **4.** A-C→D→F

> [!TIP]
> **Correct answer: 1. A→C→F→D→E**

## Solution

Using the least available edge cost as the best-first choice: from A choose C (2 rather than F at 7); from C choose F (3 rather than B at 10); from F choose D (1 rather than E at 6); and from D choose E (2 rather than Z at 7). Thus the listed node order before reaching Z is A→C→F→D→E.

## Key Points

- Best-first search repeatedly expands the most promising available node according to its evaluation value.

## Why the other options are incorrect

The other sequences skip a currently better frontier choice: E is not selected immediately after C, F should precede E, and D cannot be preferred to F at the first relevant comparison.
