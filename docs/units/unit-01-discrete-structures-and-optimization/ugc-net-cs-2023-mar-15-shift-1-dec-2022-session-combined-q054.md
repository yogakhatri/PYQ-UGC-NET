# Question 54

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Counting, Mathematical Induction and Discrete Probability · Generalized pigeonhole principle*

51087004 What is the minimum number of students in a discrete mathematics class to be sure that at least six will receive the same grade, if there are seven possible grades: S, A, B, C, D, P and F?

- **1.** 7
- **2.** 13
- **3.** 36
- **4.** 14

> [!TIP]
> **Correct answer: 3. 36**

## Solution

To avoid six equal grades as long as possible, place five students in each of seven grade categories: 7·5=35. The 36th student forces some category to contain at least six by the pigeonhole principle.

## Key Points

- To force r objects in one of k boxes, need k(r−1)+1.

## Why the other options are incorrect

7, 13, and 14 do not exhaust the possible distribution of five per grade.
