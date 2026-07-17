# Question 25

*UGC NET CS · 2015 June Paper 2 · Algorithm Analysis · Counting Key Operations*

To determine the efficiency of an algorithm the time factor is measured by :

- **1.** Counting micro seconds
- **2.** Counting number of key operations
- **3.** Counting number of statements
- **4.** Counting kilobytes of algorithm

> [!TIP]
> **Correct answer: 2. Counting number of key operations**

## Solution

Algorithm analysis chooses a dominant or key operation—such as a comparison in searching—and counts how often it executes as a function of input size. This abstracts away processor speed, programming language, and temporary system load, making the result useful across machines. Hence the time factor is measured by the number of key operations.

## Key Points

- Model running time with a machine-independent count of the algorithm's basic operation.

## Why the other options are incorrect

Microseconds are machine- and implementation-dependent. Counting every statement treats unequal-cost statements as identical and can obscure the dominant work. Kilobytes measure space or representation size, not running time.
