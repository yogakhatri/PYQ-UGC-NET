# Question 64

*UGC NET CS · 2019 Dec Paper 1 And 2 · Programming in C · Nested Loops and Break*

What is the output of this C program? int i,j,x=0; for (i=0; i<5; ++i) for (j=0; j<i; ++j) { x += (i+j-1); break; } printf("%d",x);

- **1.** 6
- **2.** 5
- **3.** 4
- **4.** 3

> [!TIP]
> **Correct answer: 1. 6**

## Solution

The break exits only the inner loop. For i=0, j<i is false, so nothing is added. For each i=1,2,3,4, the inner loop runs once with j=0, adds i+0−1, and immediately breaks. Therefore x=0+(0+1+2+3)=6, so option 1 is printed.

## Key Points

- An unlabelled C break terminates the nearest enclosing loop only.

## Why the other options are incorrect

The additions are not performed i times because break stops the inner loop after its first iteration. The outer loop continues because that break does not apply to it. Values 5, 4, and 3 result from omitting or miscounting one of the four outer-loop cases.
